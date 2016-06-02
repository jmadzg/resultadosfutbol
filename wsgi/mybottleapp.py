# -*- coding: utf-8 -*- 
import requests
import json
from bottle import request, get, post, run, debug, route, template, error, TEMPLATE_PATH, default_app, static_file
import bottle

application=default_app()









@route('/')
def buscar():
	return template('index.tpl')







# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 




