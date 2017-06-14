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

def read_container_vars(container):
    """this function returns a list of container deployments"""

    fe_data = read_all_containers()

    if container not in fe_data:
        container_names = fe_data.keys()
        container_names.sort()
        raise ValueError(bcolors.FAIL + 'Invalid container : ' + container + bcolors.ENDC + '\n'
                         'Valid containers : ' + '%s' % ' '.join(map(str, container_names)))
    else:
        container_vars = fe_data[container]

    if isinstance(container_vars, list):
        for container_var in container_vars:
            _complete_default_container_vars(container, container_var)
        return container_vars
    else:
        _complete_default_container_vars(container, container_vars)
        return [container_vars]

def _complete_default_container_vars(container, container_vars):
    if "image" not in container_vars:
        container_vars.update(dict(image=container))
    if "hostname" not in container_vars:
        container_vars.update(dict(hostname=container))
    if "container" not in container_vars:
        container_vars.update(dict(container=container))
    
def read_env_vars(env):
    with open("group_vars/all", 'r') as stream:
        try:
            env_data = yaml.load(stream)['env_vars']
        except yaml.YAMLError as exc:
            print(exc)

    if env not in env_data:
        raise ValueError(bcolors.FAIL + 'Invalid env : ' + env + bcolors.ENDC + '\n'
                                                                                'Valid env : ' + '%s' % ' '.join(
            map(str, env_data.keys())))
    else:
        return env_data[env]
        
def env_list():
    with open("group_vars/all", 'r') as stream:
        try:
            env_data = yaml.load(stream)['env_vars']
            result = []
            for env in env_data:
                result.append(env)
            return result
        except Exception as exc:
            raise exc
            
def export_env_vars(env=None):
    # 1. read conf for container info
    if env is None:
        env = get_current_instance_environment()
    env_vars = read_env_vars(env)
    # 2. export env vars
    os.environ["http_proxy"] = env_vars['proxy']['http_proxy']
    os.environ["https_proxy"] = env_vars['proxy']['https_proxy']
    os.environ["no_proxy"] = env_vars['proxy']['no_proxy']
    if "aws_account" in env_vars:
        if "AWS_ACCESS_KEY_ID" in env_vars['aws_account']:
            os.environ["AWS_ACCESS_KEY_ID"] = env_vars['aws_account']['AWS_ACCESS_KEY_ID']
        else:
            os.unsetenv('AWS_ACCESS_KEY_ID')
        if "AWS_SECRET_ACCESS_KEY" in env_vars['aws_account']:
            os.environ["AWS_SECRET_ACCESS_KEY"] = env_vars['aws_account']['AWS_SECRET_ACCESS_KEY']
        else:
            os.unsetenv('AWS_SECRET_ACCESS_KEY')
        if "AWS_DEFAULT_REGION" in env_vars['aws_account']:
            os.environ["AWS_DEFAULT_REGION"] = env_vars['aws_account']['AWS_DEFAULT_REGION']
        else:
            os.unsetenv('AWS_DEFAULT_REGION')
            
print bcolors.OKBLUE + 'hello blue world' + bcolors.ENDC
print bcolors.FAIL + 'hello fail' + bcolors.ENDC
print bcolors.OKGREEN + 'hello green world' + bcolors.ENDC
print bcolors.BOLD + 'hello bold world' + bcolors.ENDC
print bcolors.WARNING + 'hello warn ' + bcolors.ENDC
print bcolors.HEADER + 'hello header' + bcolors.ENDC
print bcolors.FAIL + bcolors.BOLD + 'hello underline' + bcolors.ENDC
