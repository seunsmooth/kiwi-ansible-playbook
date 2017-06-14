#!/bin/bash
### Author: Yufei
### Date: 2017.06.14
### Desc: This shell use for aws jump util

pem_file="yufei_aws2.pem"

## echo colorful text
red="\033[31m"
normal="\033[m"

echo -e "${red}hello red world${normal}"

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
  
  if [ -z "$ip_list" ]; then
    echo -e "${red}No host found!${normal}"
  fi
  
  echo -e "${red}add new feature: run \"dssh container\" for docker attach into container on host${normal}"
  
  for ip in $ip_list; do
      ssh -o StrictHostKeyChecking=no -i ~/.ssh/${pem_file} $ip " type dssh  || echo 'dssh() { docker exec -it \$1 /bin/bash; }' >> .bashrc" > /dev/null
  done
  
  for ip in $ip_list; do
      echo -e "${red}jumping into $ip ${normal}"
      screen -t $1-$ip ssh -t -o StrictHostKeyChecking=no -i ~/.ssh/${pem_file} $ip
  done
  
}


