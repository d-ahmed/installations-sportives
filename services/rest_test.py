#!/usr/bin/env python3

import bottle # Web server
from bottle import run, route, request
import json
import mysql.connector as mysql
from mysql.connector import Error
import sys
sys.path.append("/home/daniel/Documents/Creation_D_application/with_mysql/model")
bottle.TEMPLATE_PATH.insert(0, "/home/daniel/Documents/Creation_D_application/with_mysql/vue/html/")

import Dao
import utiles


@route('/installation', method='GET')
def recherche():
    # Store HTTP GET arguments
    activite   = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)
    resulat=[]
    if ((activite is not None) and (ville is not None)):
        myUtiles=utiles.Utiles()
        myDataBase=Dao.Dao()
        myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
        cur = myDataBase.getCursor()
        villeBis=myUtiles.cleanString(ville)
        activiteBis=myUtiles.cleanString(activite)
        #print("activiteBis = "+activiteBis)
        cur.execute("Select i.nomInstallation, i.numeroInstallation, i.ville, i.adresse, a.libeleActivite from installations i JOIN equipement e on i.numeroInstallation=e.numeroInstallation_activite JOIN equipements_Assoc_activites ea on e.idEquipement=ea.idEquipement_Activite JOIN activite a on a.codeActivite=ea.codeActivite where i.ville= %s and a.libeleActivite like %s",(ville,"%"+activite+"%"))
        rows = cur.fetchall()
        for membre in rows:
<<<<<<< HEAD
            sort={}
            sort['installation']=str((membre[0]),"UTF-8")
            sort['numeroInstallation']=(membre[1])
            sort['ville']=str((membre[2]),"UTF-8")
            sort['adresse']=str((membre[3]),"UTF-8")
            sort['activite']=str((membre[4]),"UTF-8")
            print (json.dumps(sort))
            resulat.append(sort)
    #print ({'installation':resulat})
    return 	({'installations':resulat})

@route('/<filepath:path>')
    def server_static(filepath):
    return static_file(filepath, root='./static')
=======
            sort['installation']=(membre[0])
            sort['adresse']=(membre[1])
            sort['codePostal']=(membre[2])
            sort['ville']=(ville)
            sort['activite']=(activite)
            #print (sort)
            sortStr=sortStr+bottle.template('affiche', installation=(membre[0]),ville=ville,activite=activite,adresse=(membre[1]),code_postal=(membre[2]))
        sortStr=sortStr+bottle.template('fin')
        if rows:
        #return json.dumps(sort,indent=0)
        #json.dumps(sort,indent=0)
            return """<html>"""+sortStr+""" </html>"""
        else:
            return """
    					<p>Non trouvé</p>
    				"""


>>>>>>> 032ec7846aa2ab52292855833ebbb9862a35eca4

if __name__ == '__main__':        
    # To run the server, type-in $ python server.py
    bottle.debug(True) # display traceback 
    run(host='localhost', port=8080, reloader=True) 
