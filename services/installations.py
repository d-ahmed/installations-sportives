from bottle import route, run, request, response
import sys
sys.path.append("../model")
from dao import Dao
from installation import Installation
from equipement import Equipement
from activite import Activite
import json

def toInstallations(argument):
    installation = Installation(argument[0],argument[1],argument[2],argument[3],argument[4],argument[5],argument[6])
    dao = Dao()
    dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    cur = dao.getCursor()
    cur.execute("Select * from equipement where numeroInstallation = %s ",(argument[0],))
    rows = cur.fetchall()
    equipement = list(map(toEquipement, rows))
    for equipement in equipement:
        installation.addEquipement(equipement)
    return installation

def act(argument):
    dao = Dao()
    dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    cur = dao.getCursor()
    cur.execute("Select * from activite where numero = %s ",(argument[0],))
    row = cur.fetchone()
    return row

def toEquipement(argument):
    equipement = Equipement(argument[0],argument[1],argument[2])
    dao = Dao()
    dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    cur = dao.getCursor()
    rows = cur.execute("Select numeroActivite from equipements_Assoc_activites where numeroEquipement = %s ",(argument[0],))
    rows = cur.fetchall()
    listActivite = list(map(act,rows))
    activite = list(map(toActivite, listActivite))
    for activite in activite:
        equipement.addActivite(activite)
    return equipement

def toActivite(argument):
    activite = Activite(argument[0],argument[1],argument[2])
    return activite

def todic(installation):
    equip = []
    activit = []
    for equipement in installation.equipement:
        for activite in equipement.activite:
            activit.append(activite.__dict__)
        dictEquipement = equipement.__dict__
        dictEquipement['activite']=activit
        equip.append(dictEquipement)
    inst=installation.__dict__
    #del inst[equipement]
    inst['equipement']=equip
    return inst

def installation(activite, ville):
    dao = Dao()
    dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    cur = dao.getCursor()
    cur.execute("Select  i.numero, i.nom, i.adresse, i.codePostal, i.ville,  i.latitude, i.longitude from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
    rows = cur.fetchall()
    installation = list(map(toInstallations, rows))

    #print (installation)
    return installation

@route('/installation')
def recherche():
    # Récuperation des argument passé en paramètre dans l'url
    activite   = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)
    items = installation(activite,ville)
    myDictionary = (list(map(todic,items)))
    #print (myDictionary)
    return {'installations' : myDictionary}

"""
@route('/installation')
def recherche():
    # Récuperation des argument passé en paramètre dans l'url
    activite   = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)

    resultat=[]
    if ((activite is not None) and (ville is not None)):

        myDataBase=Dao()
        # Connexion a la base de donnés
        myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
        #myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
        # Recuperation du cursseur
        cur = myDataBase.getCursor()
        # Exécution de la requette qui vas récuperer le nom, le numero, la ville, le code postale l'adresse
        # de l'installation, le nom de l'activite et le numero d'equipement
        cur.execute("Select i.nom, i.numero, i.ville, i.adresse, a.nom, i.codePostal, e.numero from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
        # Récuperation du resultat sous forme de tableau
        rows = cur.fetchall()
        for membre in rows:
            sort={}
            sort['installation']=(membre[0]).decode()
            sort['numeroInstallation']=(membre[1])
            sort['ville']=(membre[2]).decode()
            sort['adresse']=(membre[3]).decode()
            sort['activite']=(membre[4]).decode()
            sort['code_postal']=(membre[5])
            sort['numeroEquipement']=(membre[6])
            resultat.append(sort)
    return {'installations':resultat}
"""

@route('/ville')
def recherche():
    resultat=[]
    myDataBase=Dao()
    myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    #myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    cur = myDataBase.getCursor()
    cur.execute("Select ville from installation")
    rows = cur.fetchall()
    for membre in rows:
        sort={}
        sort['ville']=(membre[0]).decode()
        resultat.append(sort)
    print(resultat)
    return json.dumps(resultat)