from bottle import route, run, request, response
import sys
sys.path.append("../model")
import Dao
import json

@route('/activite')
def recherche():
    # Store HTTP GET arguments
    resultat=[]
    myDataBase=Dao.Dao()
    myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    cur = myDataBase.getCursor()
    cur.execute("Select nom from activite")
    rows = cur.fetchall()
    for membre in rows:
        sort={}
        sort['activite']=str((membre[0]),"UTF-8")
        resultat.append(sort)
    return json.dumps(resultat)