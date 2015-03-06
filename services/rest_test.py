import bottle # Web server
from bottle import run, route, request
import json
import mysql.connector as mysql
from mysql.connector import Error
import sys
sys.path.append("/home/daniel/Documents/Creation_D_application/with_mysql/model")
import Dao


@route('')


@route('/installation', method='GET')
def recherche():
	return 	"""
				<form action="/installation" method="post">
					Ville : <input name="ville" type="text"/>
					Activite : <input name="activite" />
					<input type="submit" value="envoyer"/>
				</form>
			"""



@route('/installation', method='POST')
def getInstallation():
    """ 
    Convert given text to uppercase
    (as a plain argument, or from a textfile's URL)
    Returns an indented JSON structure
    """
    
    # Store HTTP GET arguments
    activite   = request.POST.get('activite',default=None)
    ville = request.POST.get('ville', default=None)
    #textfile_url = request.GET.get('URL', default=None)

    # Execute WebService specific task
    # here, converting a string to upper-casing
    if ((activite is not None) and (ville is not None)):
    	myDataBase=Dao.Dao()
    	myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    	cur = myDataBase.getCursor()
    	cur.execute("Select inst.nomInstallation, inst.adresse, inst.code_postal FROM installations inst WHERE ville LIKE %s and inst.numeroInstallation in(Select equip.numeroInstallation_activite from equipement equip, equipements_Assoc_activites equipActivite where equip.idEquipement=equipActivite.idEquipement_Activite and equipActivite.codeActivite in (select codeActivite from activite where libeleActivite LIKE %s))",(ville,activite))
    	rows = cur.fetchall()
    	sort={}
    	for membre in rows:
    		sort['installation']=(membre[0])
    		sort['adresse']=(membre[1])
    		sort['code_postal']=(membre[2])
    		sort['ville']=(ville)
    		sort['activite']=(activite)
    		print (sort)

    	if rows:
    		#return json.dumps(sort,indent=0)
    		return json.dumps(sort,indent=0)
    	else:
    		return """
    					<p>Non trouvé</p>
    				"""
    else:
    	return """
    			<h1>Ne fonctionne pas</h1>
    			"""



if __name__ == '__main__':        
    # To run the server, type-in $ python server.py
    bottle.debug(True) # display traceback 
    run(host='localhost', port=8080, reloader=True) 