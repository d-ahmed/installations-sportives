from bottle import route, static_file, run
import installations
import equipements
import activites


@route('/<filepath:path>')
def server_static(filepath):
	print (filepath)
	return static_file(filepath, root='../vue')

run(host='localhost', port=8080, reloader=True)