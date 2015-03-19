from bottle import route, run, request, response
import sys
sys.path.append("../model")
import Dao
import json
import main


@route('/equipement')
def recherche():
    # Store HTTP GET arguments
    numeroEquipement   = request.GET.get('id',default=None)
    resultat=[]

    if (numeroEquipement is not None):
        #myDataBase=Dao.Dao()
        #myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
        #cur = myDataBase.getCursor()
        main.cur.execute("Select nom from equipement where numero = %s ",(numeroEquipement,))
        responce = main.cur.fetchone()
        print (responce[0])
       	return json.dumps(str(responce[0],"UTF-8"))