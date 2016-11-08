#!/usr/bin/env python
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import argparse
import subprocess
import json
import boto3
import urllib2
from subprocess import call

# coding: utf-8

__Author__ = 'yren'
__Date__ = 'Nov 8, 2016'

USAGE = '''
Usage:
    python {script_name} {env} {container} {tag}

Example:
    python deploy.py qa container-name tag
'''

PLAYBOOK_DIR = "./playbook/"