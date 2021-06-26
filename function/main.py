import base64
import json
import typing
from googleapiclient.discovery import build

compute = build('compute', 'v1')


class NetworkInterface(typing.TypedDict):
    subnetwork: str


class Tags(typing.TypedDict):
    fingerprint: str
    items: typing.List[str]


class VM(typing.TypedDict):
    name: str
    zone: str
    networkInterfaces: typing.List[NetworkInterface]
    tags: Tags


class Resource(typing.TypedDict):
    parent: str
    data: VM


class Asset(typing.TypedDict):
    resource: Resource


class Payload(typing.TypedDict):
    asset: Asset


# Edit this to apply tags by subnet
# If the VM is on a subnet, it will gain the tags.
# Note: this process is additive.  It does not remove any prior tags
subnetwork_tags_map = {
    'https://www.googleapis.com/compute/v1/projects/sc-jbh-sandbox/regions/us-central1/subnetworks/default': ['central1'],
    'https://www.googleapis.com/compute/v1/projects/sc-jbh-sandbox/regions/us-west4/subnetworks/default': ['west4', 'western']
}


def main(event, ctx):
    if 'data' not in event:
        raise

    payload = base64.b64decode(event['data']).decode('utf-8')
    payload: Payload = json.loads(payload)

    print(payload)

    if should_ignore(payload):
        print("Ignoring")
        return

    adjust_tags(payload)


def should_ignore(payload: Payload) -> bool:
    """
    Is there a rule pertaining to this VM's network?
    """
    nics = get_network_interfaces(payload=payload)
    subnets = map(lambda nic: nic['subnetwork'], nics)
    return not any(subnet in subnetwork_tags_map for subnet in subnets)


def adjust_tags(payload: Payload):
    tags = set(get_network_tags(payload))
    new_tags = set(tags)

    nics = get_network_interfaces(payload)
    subnets = map(lambda nic: nic['subnetwork'], nics)

    for subnet in subnets:
        target_tags = set(subnetwork_tags_map.get(subnet, []))
        new_tags |= target_tags

    if tags == new_tags:
        print("Nothing to change - aborting")
        return

    set_tags(payload=payload, tags=list(new_tags))


def set_tags(payload: Payload, tags: Tags):
    data = payload['asset']['resource']['data']

    instance = data['name']

    # https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a
    zone = data['zone'].split('/')[-1]

    # '//cloudresourcemanager.googleapis.com/projects/163454223397'
    project = payload['asset']['resource']['parent'].split('/')[-1]
    args = {
        'instance': instance,
        'zone': zone,
        'project': project
    }
    vm = compute.instances().get(**args).execute()
    old_tags = vm['tags']
    fingerprint = old_tags['fingerprint']
    new_tags = {
        'items': tags,
        'fingerprint': fingerprint
    }
    print('Updating VM')
    print(new_tags)
    compute.instances().setTags(**args, body=new_tags).execute()


def get_network_interfaces(payload: Payload) -> typing.List[NetworkInterface]:
    return payload['asset']['resource']['data']['networkInterfaces']


def get_network_tags(payload: Payload) -> Tags:
    return payload['asset']['resource']['data']['tags'].get('items', [])
