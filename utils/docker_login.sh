#!/bin/bash
### Author: Yufei
### Date: 2017.06.14
### Desc: This shell used for docker ecr login

if [ "$#" -gt 1 ]; then
  LOGIN_STRING=`aws ecr get-login --registry-ids $1 --region $2`
else
  LOGIN_STRING=`aws ecr get-login`
fi

${LOGIN_STRING}