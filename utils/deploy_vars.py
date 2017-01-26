#!/usr/bin/env python

# coding: utf-8

__Author__ = 'Yufei'
__Date__ = 'Jan 26, 2017'


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


if __name__ == '__main__':
    style = bcolors()
    print style.header('hi, you are running deploy_vars.py!')
