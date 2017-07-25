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


def init_args(args):
    command_vars = {}
    command_vars.update(vars(args))
    
    if not args.host_limit:
        command_vars['host_limit'] = ''
    
    if not args.ip_limit:
        command_vars['ip_limit'] = ''
    
    if args.no_cache:
        command_vars['cache'] = 'disable'
    else:
        command_vars['cache'] = 'enable'
    
    command_vars.pop('no_cache')
    
    if args.debug:
        command_vars['command'] = '/bin/bash'
        command_vars['tty'] = 'true'
    else:
        command_vars['command'] = ''
        command_vars['tty'] = 'false'
        
    command_vars.pop('debug')
    
    print command_vars

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'deploy.py', 
        description='this command for deploy docker image to aws')
    parser.add_argument('env', help = 'environment: dev, qa, ppe, prod')
    parser.add_argument('container', help = 'docker container: kiwi-ghost ...')
    parser.add_argument('tag', help = 'docker image tag: 0.0.1, CKB-1000 ...')
    parser.add_argument('-host', '--host_limit', help = 'limit host name to install, without env: -host blog')
    parser.add_argument('-ip', '--ip_limit', help = 'limit ip to install: -ip 10.10.1.2')
    parser.add_argument('-n', '--no_cache', action = 'store_true', help = 'disable apache page cache, works only for apache container')
    parser.add_argument('-d', '--debug', action = 'store_true', help = 'enable debug model for container, start with container with /bin/bash')
    args = parser.parse_args()
    command_vars = init_args(args)
