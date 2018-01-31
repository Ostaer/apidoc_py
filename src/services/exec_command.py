# -*- coding:utf-8 -*-
'''
Created on 2018/1/31
@author: banbanqiu
'''
import time
import subprocess


class TimeoutError(Exception):
    def __init__(self, cmd, timeout):
        Exception.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def __str__(self):
        return "cmd={} timeout={}".format(self.cmd, self.timeout)


def execute_command(cmd, timeout=600):
    # print('start executing cmd...')
    s = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    # 判断超时
    begin_time = time.time()
    while s.poll() is None:
        second_passed = time.time() - begin_time
        if second_passed > timeout:
            s.terminate()
            raise TimeoutError(cmd, timeout)
        time.sleep(0.1)

    stderrinfo, stdoutinfo = s.communicate()
    # print('stderrinfo is -------> %s and stdoutinfo is -------> %s' % (stderrinfo, stdoutinfo))
    # print('finish executing cmd....')
    return s.returncode, stdoutinfo, stderrinfo
