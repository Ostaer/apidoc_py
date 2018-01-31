define({ "api": [
  {
    "type": "post",
    "url": "/build",
    "title": "Generate Project API Docment",
    "description": "<p>git-address，project_name GenerateAPIDocument</p>",
    "group": "Apidoc_Build",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "project_name",
            "description": "<p>project name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "remote_origin_url",
            "description": "<p>git address</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "/build\n{\n    \"project_name\": \"apidoc-test\",\n    \"remote_origin_url\": \"https://github.com/Ostaer/apidocs-test.git\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "1.0.0",
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"build_error\": null,\n    \"build_result\": null,\n    \"build_status\": null,\n    \"clone_error\": null,\n    \"clone_result\": null,\n    \"clone_status\": null,\n    \"exception\": \"[Error 145] : u'D:\\\\\\\\WORK SPACE\\\\\\\\apidocs-test'\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"build_error\": \"\\u001b[32minfo\\u001b[39m: Done.\\r\\n\",\n    \"build_result\": \"\",\n    \"build_status\": 0,\n    \"clone_error\": \"\",\n    \"clone_result\": \"Cloning into 'apidocs-test'...\\n\",\n    \"clone_status\": 0,\n    \"exception\": null\n}",
          "type": "json"
        }
      ]
    },
    "filename": "D:/WORK SPACE/ApiDocs/src/app.py",
    "groupTitle": "Apidoc_Build",
    "name": "PostBuild",
    "sampleRequest": [
      {
        "url": "http://127.0.0.1:5000/build"
      }
    ]
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "D:/WORK SPACE/ApiDocs/src/static/apidocs/ApiDocs/main.js",
    "group": "D__WORK_SPACE_ApiDocs_src_static_apidocs_ApiDocs_main_js",
    "groupTitle": "D__WORK_SPACE_ApiDocs_src_static_apidocs_ApiDocs_main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "D:/WORK SPACE/ApiDocs/src/static/apidocs/+ADD+/main.js",
    "group": "D__WORK_SPACE_ApiDocs_src_static_apidocs__ADD__main_js",
    "groupTitle": "D__WORK_SPACE_ApiDocs_src_static_apidocs__ADD__main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "D:/WORK SPACE/ApiDocs/src/static/apidocs/apidocs-test/main.js",
    "group": "D__WORK_SPACE_ApiDocs_src_static_apidocs_apidocs_test_main_js",
    "groupTitle": "D__WORK_SPACE_ApiDocs_src_static_apidocs_apidocs_test_main_js",
    "name": ""
  }
] });
