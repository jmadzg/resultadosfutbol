from bottle import route, default_app,run
import os
import mybottleapp
application=default_app()



os.environ['OPENSHIFT_REPO_DIR']=""




@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return '<strong>Hello World!</strong>'

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 



run(host='0.0.0.0', port=8080)

debug='TRUE'
