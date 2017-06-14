#!/bin/bash
### Author: Yufei
### Date: 2017.06.14
### Desc: shell for fetch auto scaling init shell

## set exit when meet error
set -e

export AWS_DEFAULT_REGION=`curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}'`
echo "AWS_DEFAULT_REGION = ${AWS_DEFAULT_REGION}"

instance_id=`curl -s http://169.254.169.254/latest/meta-data/instance-id`
echo "instance_id = ${instance_id}"

box_type="`aws ec2 describe-tags --filters "Name=resource-id,Values=$instance_id" "Name=key,Values=box_type" --output=text --query Tags[].Value`"
env="`echo $box_type |cut -f 1 -d "_"`"
box_type_no_env="`echo $box_type |cut -f 2- -d "_"`"
echo "box_type = ${box_type}, env = ${env}, box_type_no_env = ${box_type_no_env}"

rm -rf /tmp/${box_type_no_env}-init.sh
aws configure set default.s3.signature_version s3v4
s3_init_sh="s3://${env}-auto-scaling-metadata/${box_type_no_env}-init.sh"

if [ $(aws s3 ls ${s3_init_sh}  | wc -l) == 1 ]; then
  aws s3 cp ${s3_init_sh} /tmp/${box_type_no_env}-init.sh
  chmod a+x /tmp/${box_type_no_env}-init.sh
  /tmp/${box_type_no_env}-init.sh
else
  echo "no auto scaling init shell found : ${s3_init_sh}" 
fi

