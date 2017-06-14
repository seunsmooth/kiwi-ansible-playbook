#!/bin/bash
### Author: Yufei
### Date: 2017.06.14
### Desc: This shell use for aws jump util

## echo colorful text
red="\033[31m"
blue="\033[35m"
normal="\033[m"


export AWS_DEFAULT_REGION=`curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}'`
instance_id=`curl -s http://169.254.169.254/latest/meta-data/instance-id`
env="`aws ec2 describe-tags --filters "Name=resource-id,Values=$instance_id" "Name=key,Values=Environment" --output=text --query Tags[].Value`"

jump() {
  if [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo -e "input is ip"
    ip_list=$1
  elif [[ $1 == i-* ]]; then
    echo -e "input is instance_id"
    ip_list=$(aws ec2 describe-instances --instance-ids $instance_id --query='Reservations[].Instances[].PrivateIpAddress' --output text)
  else
    echo -e "input is box_type"
    box_type=$1
    ip_list=$(aws ec2 describe-instances --filters "Name=tag:box_type, Values=$box_type" "Name=instance-state-name, Values=running" --query='Reservations[].Instances[].PrivateIpAddress' --output text)
  fi
}

echo -e "${red}hello red world${normal}"
echo -e "${blue}hello blue world${normal}"
echo -e "hello world"