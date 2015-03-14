#!/usr/bin/env python3

import bottle # Web server
from bottle import route, static_file, run, request
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
    resultat=[]
    if ((activite is not None) and (ville is not None)):
        myUtiles=utiles.Utiles()
        myDataBase=Dao.Dao()
        myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
        cur = myDataBase.getCursor()
        villeBis=myUtiles.cleanString(ville)
        activiteBis=myUtiles.cleanString(activite)
        #print("activiteBis = "+activiteBis)
        cur.execute("Select i.nom, i.numero, i.ville, i.adresse, a.nom from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
        rows = cur.fetchall()
        for membre in rows:
            sort={}
            sort['installation']=str((membre[0]),"UTF-8")
            sort['numeroInstallation']=(membre[1])
            sort['ville']=str((membre[2]),"UTF-8")
            sort['adresse']=str((membre[3]),"UTF-8")
            sort['activite']=str((membre[4]),"UTF-8")
            #print (json.dumps(sort))
            resultat.append(sort)
    #print ({'installation':resulat})
    print (json.dumps({'installation':resultat}))
    return (json.dumps({'installation':resultat}))
    #return 	(json.dumps(resultat))

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host='localhost', port=8080)

"""
if __name__ == '__main__':        
    # To run the server, type-in $ python server.py
    bottle.debug(True) # display traceback 
    run(host='localhost', port=8080, reloader=True) 
"""