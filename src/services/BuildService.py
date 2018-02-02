# -*- coding: utf-8 -*-

import os
import logging
import shutil
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

    def copy(self, base_path, project_name):
        lg = logging.getLogger(project_name)
        CList = ['api_data.js', 'api_data.json', 'api_project.js', 'api_project.json']

        cur_static_apidocs = os.path.join(base_path, project_name, "src", "static", "apidocs")
        src_project_dir = os.path.join(cur_static_apidocs, project_name)
        dest_project_dir = os.path.join(cur_static_apidocs, "+AddProject")
        for f in CList:
            src_file = os.path.join(src_project_dir, f)
            dest_file = os.path.join(dest_project_dir, f)
            try:
                shutil.copy(src_file, dest_file)
                lg.debug("Copy src={} dest={}".format(src_file, dest_file))
            except:
                lg.exception("Copy src={} dest={}".format(src_file, dest_file), exc_info=1)
                continue

    def delete(self,base_path, project_name):
        lg = logging.getLogger(project_name)
        cur_static_apidocs = os.path.join(base_path, project_name, "src", "static", "apidocs")
        src_project_dir = os.path.join(cur_static_apidocs, project_name)
        shutil.rmtree(src_project_dir)
        lg.debug("delete {}".format(src_project_dir))