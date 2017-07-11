#!/usr/bin/env python
import argparse

# coding: utf-8

__Author__ = 'Yufei Ren'
__Date__ = '2017.07.11'

USAGE = '''
Usage:
    deploy.py {env} {container} {tag}
    
Example:
    deploy.py dev kiwi-ghost 0.0.1
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'deploy.py', 
        description='this command for deploy docker image to aws')
    parser.add_argument('env', help = 'environment: dev, qa, ppe, prod')