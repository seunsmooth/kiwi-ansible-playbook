#!/usr/bin/env python
import os
import argparse
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# coding: utf-8

__Author__ = 'Yufei'
__Date__ = 'Nov 8, 2016'

USAGE = '''
Usage:
    python {script_name} {env} {container} {tag}

Example:
    python deploy.py qa container-name tag
'''

PLAYBOOK_DIR = './playbook/'


def main():
    print 'hello deploy'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='deploy',
        description='The command for deploying module to AWS'
    )
    parser.add_argument('env', help='environment : dev,qa,ppe,prod ')
    parser.add_argument('container', help='container : ... ')
    parser.add_argument('tag', help='docker image tag: ... ')
    main()
