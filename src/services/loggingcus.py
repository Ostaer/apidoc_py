# -*- coding:utf-8 -*-
'''
Created on 2017/12/5
@author: banbanqiu

Recod the log
BASEDIR = os.path.dirname(os.path.abspath(__file__))
from loggingcus import logger,retmodule
calcu_logger = logger(os.path.join(BASEDIR,"logs","calcu_item.log"),mtype=0)
@retmodule(BASEDIR.split('/')[-1])
def main():

if __name__ == '__main__':
    main()
'''
import logging
import os, sys
import commands
import re
import datetime
from logging.handlers import TimedRotatingFileHandler

LogKeepDays = 3


def logger(logfile, mtype=1):
    '''
    Return a logger handler.
    '''
    logname = logfile.split(os.sep)[-1]
    logbase = os.path.dirname(logfile)
    _name = '.'.join(logname.split('.')[:-1])
    if not os.path.exists(logbase): os.makedirs(logbase)
    if mtype:
        LOG_FILENAME = logfile
    else:
        LOG_FILENAME = logfile + '.' + datetime.datetime.now().strftime('%Y-%m-%d')
        if datetime.datetime.now().hour == 0:
            _status, _output = commands.getstatusoutput('cd %s && /usr/bin/ls %s.*' % (logbase, logname))
            if _status == 0:
                oldlogfilelist = _output.split('\n')
                logdate = []
                datefmt = re.compile(r'%s.(20\d{2}-\d{2}-\d{2})' % logname)
                for i in oldlogfilelist:
                    m = re.match(datefmt, i)
                    if m:
                        logdate.append(m.group(1))
                logdate = sorted(logdate)
                needremovelogdate = logdate[0:-LogKeepDays]
                for _logdate in needremovelogdate:
                    try:
                        os.remove('%s.%s' % (logfile, _logdate))
                    except:
                        continue

    LEVELS = {'noset': logging.DEBUG, 'debug': logging.DEBUG, 'info': logging.INFO, \
              'warning': logging.WARNING, 'error': logging.ERROR, 'critial': logging.CRITICAL, \
              'exception': logging.exception}
    logger = logging.getLogger(_name)
    logger.setLevel(LEVELS.get('noset'))
    fh = TimedRotatingFileHandler(LOG_FILENAME, when='D', interval=1, backupCount=LogKeepDays)
    datefmt = '%Y-%m-%d %H:%M:%S'
    format_str = '[%(asctime)s %(levelname)s]  %(message)s'
    formatter = logging.Formatter(format_str, datefmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
