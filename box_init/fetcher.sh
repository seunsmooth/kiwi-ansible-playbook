#!/bin/bash

### This shell fetch box init.sh from s3

### set exit when return non-zero code
set -e

### set proxy for aws cli
#export http_proxy=
#export htts_proxy=$http_proxy
#export no_proxy=localhost,169.254.169.254

export instance_id=`curl http://169.254.169.254/latest/meta-data/instance-id`
export AWS_DEFAULT_REGION=`curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}'`
echo "instance_id=$instance_id, AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION"

box_type="`aws ec2 describe-tags --filters "Name=resource-id,Values=$instance_id" "Name=key,Values=box_type" --output=text --query Tags[].Value`"
env="`echo $box_type | cut -f 1 -d "_"`"
box_type_no_env="`echo $box_type | cut -f 2- -d "_"`"
echo "box_type $box_type ,env $env , box_type_no_env $box_type_no_env"

### fetch init.sh for this instance type
rm -rf /tmp/${box_type_no_env}-init.sh
echo "aws configure set default.s3.signature_version s3v4"
aws configure set default.s3.signature_version s3v4
s3_init_sh="s3://${env}-auto-scaling-metadata/${box_type_no_env}-init.sh"
if [ $(aws s3 ls ${s3_init_sh} | wc -l) == 1 ]; then
  aws s3 cp ${s3_init_sh} /tmp/${box_type_no_env}-init.sh
  chmod a+x /tmp/${box_type_no_env}-init.sh
  /tmp/${box_type_no_env}-init.sh
else
  echo "no init shell found : ${s3_init_sh}" 
fi
