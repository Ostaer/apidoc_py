# -*- coding:utf-8 -*-
'''
Created on 2018/1/29
@author: banbanqiu
'''
import os
import time
import logging
from exec_command import execute_command

class CodeService:
    def __init__(self, remote_origin_url="", work_dir="", project_name=""):
        self.remote_origin_url = remote_origin_url
        self.work_dir = work_dir
        self.project_name = project_name
        self.lg = logging.getLogger(self.project_name)


    def pull(self):
        if self.is_exist():
            cmd = "cd {} && git pull {}".format(self.work_dir, self.remote_origin_url)
            self.lg.info("Exec command {}".format(cmd))
            status, stdoutinfo, stderrinfo = execute_command(cmd)
            self.lg.info("Exec result {} {}".format(stdoutinfo, stderrinfo))
            return status, stdoutinfo, stderrinfo
        else:
            self.clone()

    def clone(self):
        self.lg.info("Start pull project")
        if self.is_exist(): self.delete()
        cmd = "cd {} && git clone {}".format(self.work_dir, self.remote_origin_url)
        self.lg.info("Exec command {}".format(cmd))
        status, stdoutinfo, stderrinfo = execute_command(cmd)
        self.lg.info("Exec result {} {}".format(stdoutinfo, stderrinfo))
        return status, stdoutinfo, stderrinfo

    def delete(self):
        if self.is_exist():
            self.lg.info("Older directory is exist!")
            old_dir = os.path.join(self.work_dir, self.project_name)
            self.lg.info("Remove older directory {}".format(old_dir))
            os.removedirs(old_dir)
        else:
            self.lg.info("Older directory is not exist!")

    def is_exist(self):
        old_dir = os.path.join(self.work_dir, self.project_name)
        self.lg.info("If older directory is exist? {}".format(old_dir))
        ret = os.path.isdir(old_dir)
        return ret
