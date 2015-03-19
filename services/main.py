from bottle import route, static_file, run
import installation
import equipement
import activite

@route('/<filepath:path>')
def server_static(filepath):
	print (filepath)
	return static_file(filepath, root='/home/daniel/Documents/Creation_D_application/with_mysql/vue')


run(host='localhost', port=8080, reloader=True)