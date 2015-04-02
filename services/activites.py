from bottle import route, run, request, response
import sys
sys.path.append("../model")
from dao import Dao
import json

@route('/activite')
def recherche():
    # Store HTTP GET arguments
    resultat=[]
    myDataBase=Dao()
    #myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    cur = myDataBase.getCursor()
    cur.execute("Select nom from activite")
    rows = cur.fetchall()
    for membre in rows:
        sort={}
        sort['activite']=(membre[0])
        resultat.append(sort)
    return json.dumps(resultat)