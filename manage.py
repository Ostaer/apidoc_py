# -*- coding:utf-8 -*-
'''
Created on 2018/2/2
@author: banbanqiu
'''
import os
import sys
from src.services.BuildService import BuildService
from src.services.loggingcus import logger

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
project_name = os.path.basename(current_dir)
record_log = os.path.join(current_dir, "logs", "{}.log".format(project_name))
lg = logger(record_log)


def execute_from_command_line(paras):
    if len(paras) < 2:
        Usage()

    subcmd = paras[1]
    if subcmd.lower() == "config":
        build_service = BuildService()
        build_service.build(project_dir, project_name)
        build_service.copy(project_dir, project_name)
        build_service.delete(project_dir, project_name)

    if subcmd.lower() == "run":
        from src.app import socketio, app
        if len(paras) == 2:
            socketio.run(app, debug=False, host='0.0.0.0', port=5000)
        elif len(paras) == 3:
            s = paras[2]
            import re
            try:
                p = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})')
                ret = re.match(p, s)
                if ret:
                    host, port = ret.groups()
                    socketio.run(app, debug=False, host=host, port=int(port))
                else:
                    Usage()
            except:
                lg.exception("parameter error: {}".format(s), exc_info=1)
                Usage()
        else:
            Usage()


def Usage( ):
    print '''Help:
    python {} {{subcommand}}
        subcommand:
            config config your environment
            run [0.0.0.0:8000] startup with optional listen address and port
                    default is 0.0.0.0:5000
'''.format(sys.argv[0])
    sys.exit()


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
