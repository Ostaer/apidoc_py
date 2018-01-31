# -*- coding: utf-8 -*-

import os
import logging
from exec_command import execute_command
static_apidocs = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "apidocs")


class BuildService:
    '''
    api doc 构建服务类
    '''

    def build(self, base_path, project_name, extend_path=''):
        lg = logging.getLogger(project_name)

        if extend_path is None:
            extend_path = ''

        if not base_path:
            return ' base_path is not allow empty'

        if not project_name:
            return ' project_name is not allow empty'

        file_path = os.path.join(base_path, extend_path, project_name)
        if os.path.exists(file_path) is False:
            msg = 'File is not exists：' + str(file_path)
            lg.error(msg)
            return msg

        # cmd = 'apidoc -i ' + file_path + ' -c ' + file_path + ' -o ./static/apidocs/' + project_name
        lg.info("Start generate api document...")
        cmd = 'apidoc -c "{}" -i "{}" -o "{}"'.format(file_path, file_path, os.path.join(static_apidocs, project_name))
        lg.info("Exec command {}".format(cmd))
        status, stdoutinfo, stderrinfo = execute_command(cmd)
        lg.info("Exec result {} {}".format(stdoutinfo, stderrinfo))
        return status, stdoutinfo, stderrinfo