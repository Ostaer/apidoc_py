# -*- coding:utf-8 -*-
'''
Created on 2018/1/28
@author: banbanqiu
'''
import sys
import os
import multiprocessing

path_of_current_file = os.path.abspath(__file__)
path_of_current_dir = os.path.split(path_of_current_file)[0]

_file_name = "gunicorn"


worker_class = 'sync'
workers = multiprocessing.cpu_count() * 2 + 1

chdir = os.path.dirname(path_of_current_dir)

worker_connections = 1000
timeout = 30
max_requests = 2000
graceful_timeout = 30

loglevel = 'info'

reload = True
debug = False

bind = "%s:%s" % ("0.0.0.0", 5000)
pidfile = '%s/%s.pid' % (chdir, _file_name)
errorlog = '%s/logs/%s_error.log' % (chdir, _file_name)
accesslog = '%s/logs/%s_access.log' % (chdir, _file_name)