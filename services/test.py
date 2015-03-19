import bottle # Web server
from bottle import route, run, request, response
import sys
sys.path.append("/home/daniel/Documents/Creation_D_application/with_mysql/model")

import Dao

class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)

        return _enable_cors


app = bottle.app()

@app.route('/cors', method=['OPTIONS', 'GET'])
def lvambience(arg):
    response.headers['Content-type'] = 'application/json'
    return arg

@app.route('/installation', method=['OPTIONS', 'GET'])
def recherche():
    # Store HTTP GET arguments
    activite   = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)
    resultat=[]
    if ((activite is not None) and (ville is not None)):
        myDataBase=Dao.Dao()
        myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
        cur = myDataBase.getCursor()
        cur.execute("Select i.nom, i.numero, i.ville, i.adresse, a.nom, i.codePostal from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
        rows = cur.fetchall()
        for membre in rows:
            sort={}
            sort['installation']=str((membre[0]),"UTF-8")
            sort['numeroInstallation']=(membre[1])
            sort['ville']=str((membre[2]),"UTF-8")
            sort['adresse']=str((membre[3]),"UTF-8")
            sort['activite']=str((membre[4]),"UTF-8")
            sort['code_postal']=(membre[5])
            #print (json.dumps(sort))
            resultat.append(sort)
    response.headers['Content-type'] = 'application/json'
    return {'installations':resultat}

app.install(EnableCors())

app.run(port=8001)