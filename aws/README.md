# OpenUnison on AWS

This playbooks assumes that you're using OpenUnison with S3 to store artifacts and EC2 Param Store for storing environment specific data.

## Prerequisites

This playbook assumes that the AWS cli is available and has built in credentials (whether from an IAM role or directly configured).

## S3 Structure
Where `ROOT` is your top-level bucket.

`/ROOT/util` - The contents of the `util` directory in this directory

Where `ENV` is which environment to use and `CLUSTER` is the name of the cluster:
`/ROOT/ENV/jks/CLUSTER/` - The keystore for the deployment
`/ROOT/ENV/bin/` - The OpenUnison war file
`/ROOT/conf/CLUSTER` - The `openunison.yaml` file for network configuration

## EC2 Param Store

All entries for the param store must have a root in the form of `/ROOT/ENV/CLUSTER/parameter`.  The playbook will generate an `ou.env` file based on these parmameters.


## Inventory

Each combination of environment (ie dev/test/prod/etc) and cluster (identity provider, provisioning, etc, ...) should have its own inventory file.  The `[openunison]` section should list the ip/host for each server.  The `[openunison:vars]` section needs to be updated accordingly.

## Playbook

The openunison.yaml playbook will download all of the artifacts, deploy and start OpenUnison.
