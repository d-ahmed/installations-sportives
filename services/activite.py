from bottle import route, run, request, response
import sys
sys.path.append("../model")
import Dao
import json
import main

@route('/activite')
def recherche():
    # Store HTTP GET arguments
    resultat=[]
    myDataBase=Dao.Dao()
    myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    cur = myDataBase.getCursor()
    main.cur.execute("Select nom from activite")
    rows = main.cur.fetchall()
    for membre in rows:
        sort={}
        sort['activite']=str((membre[0]),"UTF-8")
        resultat.append(sort)
    #print (resultat)
    return json.dumps(resultat)