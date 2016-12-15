#!/bin/bash

### This shell fetch box init.sh from s3

set -e

### set proxy for aws cli
#export http_proxy=
#export htts_proxy=
export no_proxy=localhost,169.254.169.254

export instance_id=`curl http://169.254.169.254/latest/meta-data/instance-id`
export AWS_DEFAULT_REGION=`curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}'`



