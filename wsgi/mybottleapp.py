# -*- coding: utf-8 -*- 
import requests
import json
from bottle import request, get, post, run, debug, route, template, error, TEMPLATE_PATH, default_app, static_file
import bottle

application=default_app()


@route('/')
def buscar():
	return template('index')



@get('/bbva')
def bbva():
    return template('bbva')

@route('/bbva/clasificaciones')
def clasif_bbva():
	parametros_bbva = {'key':'6ae96db918c2f299ae2f3eaf752594dd','format':'json','league':'1','req':'tables'}
	r = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params=parametros_bbva)
	datos = json.loads(r.text.encode("utf-8"))
	return template('clasificaciones',datos=datos)

    
@get('/adelante')
def adelante():
	return template('adelante')




@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')
    

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 