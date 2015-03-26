from bottle import route, run, request, response
import sys
sys.path.append("../model")
import Dao
import json
@route('/installation')
def recherche():
    # Récuperation des argument passé en paramètre dans l'url
    activite   = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)

    resultat=[]
    if ((activite is not None) and (ville is not None)):

        myDataBase=Dao.Dao()
        # Connexion a la base de donnés
        # myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
        myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
        # Recuperation du cursseur
        cur = myDataBase.getCursor()
        # Exécution de la requette qui vas récuperer le nom, le numero, la ville, le code postale l'adresse
        # de l'installation, le nom de l'activite et le numero d'equipement
        cur.execute("Select i.nom, i.numero, i.ville, i.adresse, a.nom, i.codePostal, e.numero, i.voie from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
        # Récuperation du resultat sous forme de tableau
        rows = cur.fetchall()
        for membre in rows:
            sort={}
            sort['nom']=(membre[0])
            sort['numeroInstallation']=(membre[1])
            sort['ville']=(membre[2])
            sort['adresse']=(membre[3])
            sort['activite']=(membre[4])
            sort['codePostal']=(membre[5])
            sort['numeroEquipement']=(membre[6])
            sort['voie']=(membre[7])
            resultat.append(sort)
    return {'installations':resultat}



@route('/ville')
def recherche():
    resultat=[]
    myDataBase=Dao.Dao()
    # myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    cur = myDataBase.getCursor()
    cur.execute("Select ville from installation")
    rows = cur.fetchall()
    for membre in rows:
        sort={}
        sort['ville']=(membre[0])
        resultat.append(sort)
    print(resultat)
    return json.dumps(resultat)