#!/usr/bin/env python
import os
import yaml
import json
import boto3
import urllib2
from jinja2 import Template

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir('..')

# coding: utf-8

#     1. command vars
#     2. container vars
#     3. env vars

__Author__ = 'Yufei'
__Date__ = 'Jun 8, 2017'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __getattr__(self, attr):
        def wrap(line):
            return self.__class__.__dict__[attr.upper()] + line + self.__class__.__dict__['ENDC']

        return wrap

def read_all_containers():
    """ read all container's deployment spec"""
    with open("group_vars/container/container_frontend.yml", 'r') as stream:
        try:
            fe_data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    with open("group_vars/container/container_backend.yml", 'r') as stream:
        try:
            be_data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    fe_data.update(be_data)
    return fe_data
    
print read_all_containers()