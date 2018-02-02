# -*- coding: utf-8 -*-
'''
apidoc python
   ps：集成apidoc，支持 http request build、crontab build、browse
'''
import os
import time
import urlparse
import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from services.IndexService import IndexService
from services.BuildService import BuildService
from services.ConfigService import ConfigService
from services.CodeSerivice import CodeService
from services.loggingcus import logger

app = Flask(__name__)
# CROS
CORS(app)
# support socketio
socketio = SocketIO()
socketio.init_app(app)

# angular conflict
app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'
app.jinja_env.block_start_string = '/%'
app.jinja_env.block_end_string = '%/'
app.jinja_env.comment_start_string = '{//'
app.jinja_env.comment_end_string = '//}'

# static docs directory
static_apidocs = os.path.join(app.root_path, "static", "apidocs")


@app.route("/")
@app.route("/apidoc/")
@app.route("/index/")
def index( ):
    '''
    Display static directory content
    '''
    _listdir = IndexService().get_path_dirs(static_apidocs)
    return render_template('/index.html', listdir=_listdir)


ASKLOCK = {}


@socketio.on('ask_for_logger', namespace='/log')
def give_log(data):
    project_name = data.get('project_name')

    # init lock
    ASKLOCK[project_name] = True

    logfile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs",
                           "{}.log".format(project_name))
    # init project logger
    if project_name not in logging.Logger.manager.loggerDict:
        logger(logfile)

    with open(logfile, 'r') as f:
        f.seek(0, 2)
        read_position = f.tell()

    while True:
        with open(logfile, 'r') as f:
            f.seek(read_position, 0)
            ret = f.read()
            if ret != "":
                ret_json = {"product_name": project_name, "result": ret}
                emit('response', {'code': '200', 'project_name': project_name, 'msg': ret_json})
            read_position = f.tell()
        # lock
        if not ASKLOCK[project_name]: break
        time.sleep(0.1)


@socketio.on('stop_for_log', namespace='/log')
def give_log(data):
    project_name = data.get('project_name')
    # disable lock
    ASKLOCK[project_name] = False


@app.route("/build", methods=['POST'])
def build( ):
    """
    @api {post}  /build Generate Project API Docment
    @apiDescription git-address，project_name GenerateAPIDocument
    @apiGroup Apidoc-Build



    @apiParam {String} project_name project name
    @apiParam {String} remote_origin_url git address
    @apiParamExample {json} Request-Example:
        /build
        {
            "project_name": "apidoc-test",
            "remote_origin_url": "https://github.com/Ostaer/apidocs-test.git"
        }
    @apiVersion 1.0.0
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "build_error": null,
            "build_result": null,
            "build_status": null,
            "clone_error": null,
            "clone_result": null,
            "clone_status": null,
            "exception": "[Error 145] : u'D:\\\\WORK SPACE\\\\apidocs-test'"
        }
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "build_error": "\u001b[32minfo\u001b[39m: Done.\r\n",
            "build_result": "",
            "build_status": 0,
            "clone_error": "",
            "clone_result": "Cloning into 'apidocs-test'...\n",
            "clone_status": 0,
            "exception": null
        }
    """
    # parase parameters
    if request.is_json:
        data = request.json
    elif request.form:
        data = request.form
    else:
        data = dict([(k, v[0]) for k, v in urlparse.parse_qs(request.data).items()])

    project_name = data.get('project_name')
    remote_origin_url = data.get('remote_origin_url')
    extend_path = request.args.get('extend_path')

    # verified parameters
    if not (project_name, remote_origin_url):
        return jsonify(status=500, msg="Parameters Required: project_name remote_original_url")

    # get project logger
    lg = logging.getLogger(project_name)

    try:
        # download code from git
        new_code_service = CodeService(remote_origin_url=remote_origin_url, work_dir=ConfigService().project_path,
                                       project_name=project_name)
        clone_status, clone_ret, clone_err = new_code_service.clone()
        # generate project api document
        build_status, build_ret, build_err = BuildService().build(ConfigService().project_path, project_name,
                                                                  extend_path)
        _exception = None
    except Exception as e:
        _exception = str(e)
        clone_status = clone_ret = clone_err = build_status = build_ret = build_err = None
        lg.exception(exc_info=1)
    finally:
        return jsonify(clone_status=clone_status, clone_result=clone_ret, clone_error=clone_err,
                       build_status=build_status, build_result=build_ret, build_error=build_err, exception=_exception)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
