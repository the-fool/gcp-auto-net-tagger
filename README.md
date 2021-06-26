# Auto Network Tagger

This tool watches VMs, and adds default network tags to them

## To deploy

Fill out the `.tfvars` file, and then apply the Terraform:

```bash
terraform init
terraform apply -var-file .tfvars
```

This will deploy:

- Asset Inventory Feed
- Cloud Function
- PubSub Topic
- Org IAM for the Cloud Function to perform VM administration


### Permissions needed

To deploy this, the account running the Terraform will need:

- Org level `cloudasset.owner`
- Org level `iam.securityAdmin`
- Project level `pubsub.admin`
- Project level `cloudfunctions.admin`
- Project level `storage.admin`
- Project level `serviceusage.serviceUsageAdmin`


## Design

A Cloud Asset Inventory Feed watches for updates of VMs.  Each event will trigger a Cloud Function that inspects the VM and adds tags as appropriate.

In `function/main.py` edit the `subnetwork_tags_map` dict to create rules for tagging VMs.

