from bottle import route, template, run

@route('/hello/<name>')
def autre(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('installation/<name>')
def installation(name):
	

run(host='localhost', port=8080)