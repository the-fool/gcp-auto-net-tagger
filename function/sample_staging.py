sample = {
    "asset": {
        "ancestors": [
            "projects/163454223397",
            "organizations/673763744309"
        ],
        "assetType": "compute.googleapis.com/Instance",
        "name": "//compute.googleapis.com/projects/sc-vice-test/zones/us-central1-a/instances/instance-1",
        "resource": {
            "data": {
                "allocationAffinity": {
                    "consumeAllocationType": "ANY_ALLOCATION"
                },
                "canIpForward": False,
                "confidentialInstanceConfig": {
                    "enableConfidentialCompute": False
                },
                "cpuPlatform": "Unknown CPU Platform",
                "creationTimestamp": "2021-04-22T13:51:49.576-07:00",
                "deletionProtection": False,
                "description": "",
                "disks": [
                    {
                        "autoDelete": True,
                        "boot": True,
                        "deviceName": "instance-1",
                        "diskSizeGb": "10",
                        "guestOsFeatures": [
                            {
                                "type": "UEFI_COMPATIBLE"
                            },
                            {
                                "type": "VIRTIO_SCSI_MULTIQUEUE"
                            }
                        ],
                        "index": 0,
                        "interface": "SCSI",
                        "licenses": [
                            "https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-10-buster"
                        ],
                        "mode": "READ_WRITE",
                        "source": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a/disks/instance-1",
                        "type": "PERSISTENT"
                    }
                ],
                "displayDevice": {
                    "enableDisplay": False
                },
                "fingerprint": "kklxPt7MzL8=",
                "id": "4486036186437803787",
                "labelFingerprint": "42WmSpB8rSM=",
                "machineType": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a/machineTypes/e2-medium",
                "name": "instance-1",
                "networkInterfaces": [
                    {
                        "accessConfigs": [
                            {
                                "name": "External NAT",
                                "natIP": "108.59.84.233",
                                "networkTier": "PREMIUM",
                                "type": "ONE_TO_ONE_NAT"
                            }
                        ],
                        "fingerprint": "3XxnerGjaPY=",
                        "name": "nic0",
                        "network": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/global/networks/default",
                        "networkIP": "10.128.0.2",
                        "subnetwork": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/regions/us-central1/subnetworks/default"
                    }
                ],
                "scheduling": {
                    "automaticRestart": True,
                    "onHostMaintenance": "MIGRATE",
                    "preemptible": False
                },
                "selfLink": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a/instances/instance-1",
                "serviceAccounts": [
                    {
                        "email": "163454223397-compute@developer.gserviceaccount.com",
                        "scopes": [
                            "https://www.googleapis.com/auth/devstorage.read_only",
                            "https://www.googleapis.com/auth/logging.write",
                            "https://www.googleapis.com/auth/monitoring.write",
                            "https://www.googleapis.com/auth/servicecontrol",
                            "https://www.googleapis.com/auth/service.management.readonly",
                            "https://www.googleapis.com/auth/trace.append"
                        ]
                    }
                ],
                "shieldedInstanceConfig": {
                    "enableIntegrityMonitoring": True,
                    "enableSecureBoot": False,
                    "enableVtpm": True
                },
                "shieldedInstanceIntegrityPolicy": {
                    "updateAutoLearnPolicy": True
                },
                "startRestricted": False,
                "status": "STAGING",
                "tags": {
                    "fingerprint": "42WmSpB8rSM="
                },
                "zone": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a"
            },
            "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest",
            "discoveryName": "Instance",
            "location": "us-central1-a",
            "parent": "//cloudresourcemanager.googleapis.com/projects/163454223397",
            "version": "v1"
        },
        "updateTime": "2021-04-22T20:51:50.801629Z"
    },
    "priorAsset": {
        "ancestors": [
            "projects/163454223397",
            "organizations/673763744309"
        ],
        "assetType": "compute.googleapis.com/Instance",
        "name": "//compute.googleapis.com/projects/sc-vice-test/zones/us-central1-a/instances/instance-1",
        "resource": {
            "data": {
                "allocationAffinity": {
                    "consumeAllocationType": "ANY_ALLOCATION"
                },
                "canIpForward": False,
                "confidentialInstanceConfig": {
                    "enableConfidentialCompute": False
                },
                "cpuPlatform": "Unknown CPU Platform",
                "creationTimestamp": "2021-04-22T13:51:49.576-07:00",
                "deletionProtection": False,
                "description": "",
                "disks": [
                    {
                        "autoDelete": True,
                        "boot": True,
                        "deviceName": "instance-1",
                        "diskSizeGb": "10",
                        "guestOsFeatures": [
                            {
                                "type": "UEFI_COMPATIBLE"
                            },
                            {
                                "type": "VIRTIO_SCSI_MULTIQUEUE"
                            }
                        ],
                        "index": 0,
                        "interface": "SCSI",
                        "licenses": [
                            "https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-10-buster"
                        ],
                        "mode": "READ_WRITE",
                        "source": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a/disks/instance-1",
                        "type": "PERSISTENT"
                    }
                ],
                "displayDevice": {
                    "enableDisplay": False
                },
                "fingerprint": "IbogiVywfFU=",
                "id": "4486036186437803787",
                "labelFingerprint": "42WmSpB8rSM=",
                "machineType": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a/machineTypes/e2-medium",
                "name": "instance-1",
                "networkInterfaces": [
                    {
                        "accessConfigs": [
                            {
                                "name": "External NAT",
                                "networkTier": "PREMIUM",
                                "type": "ONE_TO_ONE_NAT"
                            }
                        ],
                        "fingerprint": "bQWv9c5Re9E=",
                        "name": "nic0",
                        "network": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/global/networks/default",
                        "subnetwork": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/regions/us-central1/subnetworks/default"
                    }
                ],
                "scheduling": {
                    "automaticRestart": True,
                    "onHostMaintenance": "MIGRATE",
                    "preemptible": False
                },
                "selfLink": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a/instances/instance-1",
                "serviceAccounts": [
                    {
                        "email": "163454223397-compute@developer.gserviceaccount.com",
                        "scopes": [
                            "https://www.googleapis.com/auth/devstorage.read_only",
                            "https://www.googleapis.com/auth/logging.write",
                            "https://www.googleapis.com/auth/monitoring.write",
                            "https://www.googleapis.com/auth/servicecontrol",
                            "https://www.googleapis.com/auth/service.management.readonly",
                            "https://www.googleapis.com/auth/trace.append"
                        ]
                    }
                ],
                "shieldedInstanceConfig": {
                    "enableIntegrityMonitoring": True,
                    "enableSecureBoot": False,
                    "enableVtpm": True
                },
                "shieldedInstanceIntegrityPolicy": {
                    "updateAutoLearnPolicy": True
                },
                "startRestricted": False,
                "status": "PROVISIONING",
                "tags": {
                    "fingerprint": "42WmSpB8rSM="
                },
                "zone": "https://www.googleapis.com/compute/v1/projects/sc-vice-test/zones/us-central1-a"
            },
            "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest",
            "discoveryName": "Instance",
            "location": "us-central1-a",
            "parent": "//cloudresourcemanager.googleapis.com/projects/163454223397",
            "version": "v1"
        },
        "updateTime": "2021-04-22T20:51:49.759449Z"
    },
    "priorAssetState": "PRESENT",
    "window": {
        "startTime": "2021-04-22T20:51:50.801629Z"
    }
}