from bottle import route, run, request, response
import sys
sys.path.append("../model")
from dao import Dao
from installation import Installation
from equipement import Equipement
from activite import Activite
import json
import unittest
import mysql.connector.errors as Error
from reparation import Reparation

def toInstallation(argument):
    '''
        fonction qui convertit une ligne de la base de données en objet Installation
    '''
    objectInstallation = Installation(argument[0],argument[1],argument[2],argument[3],argument[4],argument[5],argument[6],argument[7])
    
    # connexion
    dao = Dao()
    # dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    cur = dao.getCursor()
    try:
        cur.execute("Select * from equipement where numeroInstallation = %s ",(argument[0],))
        rows = cur.fetchall()
        listObjectEquipement = list(map(toEquipement, rows))
        for equipement in listObjectEquipement:
            objectInstallation.addEquipement(equipement)
    except Error.ProgrammingError:
        reparation = Reparation(dao)
        reparation.updateAll()

    return objectInstallation

def toEquipement(argument):
    '''
        fonction qui convertit une ligne de la base de données en objet Equipement
    '''
    objectEquipement = Equipement(argument[0],argument[1],argument[2])
    
    # connexion
    dao = Dao()
    # dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    cur = dao.getCursor()
    try:
        rows = cur.execute("Select numeroActivite from equipements_Assoc_activites where numeroEquipement = %s ",(argument[0],))
        rows = cur.fetchall()
        listActivite = list(map(getActivite,rows))

        # récupération de toutes les activite pour un installation
        listObjectActivite = list(map(toActivite, listActivite))
        
        for activite in listObjectActivite:
            objectEquipement.addActivite(activite)
    except Error.ProgrammingError:
        reparation = Reparation(dao)
        reparation.updateAll()

    return objectEquipement

def toActivite(argument):
    '''
        fonction qui convertit une ligne de la base de données en objet Activite
    '''
    activite = Activite(argument[0][0],argument[0][1],argument[0][2])

    return activite


def getActivite(argument):
    '''
        fonction qui prend en argument un équipement retourne les lignes de la table Activite associé à l'équipement
    '''
    # connexion
    dao = Dao()
    # dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    cur = dao.getCursor()
    cur.execute("Select numero, nom, numeroEquipement from activite where numero = %s ",(argument[0],))
    row = cur.fetchall()

    return row


def todic(installation):
    '''
        fonction qui prend en argument un objet Installation et retourne le dictionnaire
    '''
    listEquipement = []
    listActivite = []

    for equipement in installation.equipement:
        for activite in equipement.activite:
            listActivite.append(activite.__dict__)
        dictEquipement = equipement.__dict__

        # On remplace l'objet activite en dictionnaire
        dictEquipement['activite'] = listActivite
        listEquipement.append(dictEquipement)
        
        # Vider la liste d'activités
        listActivite=[]
    dictInstallation = installation.__dict__
    dictInstallation['equipement']=listEquipement

    return dictInstallation


def installation(activite, ville):
    '''
        fonction qui prend en argument une activité et une ville, et retourne une liste d'objets Installation
    '''
    # connexion
    dao = Dao()
    # dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    cur = dao.getCursor()
    try:
        cur.execute("Select  i.numero, i.nom, i.voie, i.adresse, i.codePostal, i.ville,  i.latitude, i.longitude from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where ville like %s and a.nom like %s",(ville,"%"+activite+"%"))
        rows = cur.fetchall()

        # Pour éviter les doublons
        rowsbis = list(set(rows))
        installation = list(map(toInstallation, rowsbis))
    except Error.ProgrammingError:
        reparation = Reparation(dao)
        reparation.updateAll()

    return installation

def installationAvecCodePostal(activite, codePostal):
    '''
        fonction qui prend en argument une activité et un code postal, et retourne une liste d'objets Installation
    '''

    # connexion
    dao = Dao()
    # dao.connexion('localhost', 'CreationService', 'root', 'elnida')
    dao.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    cur = dao.getCursor()
    try:
        cur.execute("Select  i.numero, i.nom, i.voie, i.adresse, i.codePostal, i.ville,  i.latitude, i.longitude from installation i JOIN equipement e on i.numero=e.numeroInstallation JOIN equipements_Assoc_activites ea on e.numero=ea.numeroEquipement JOIN activite a on a.numero=ea.numeroActivite where codePostal like %s and a.nom like %s",(codePostal,"%"+activite+"%"))
        rows = cur.fetchall()
        # Pour éviter les doublons
        rowsbis = list(set(rows))
        installation = list(map(toInstallation, rowsbis))
    except Error.ProgrammingError:
        reparation = Reparation(dao)
        reparation.updateAll()  
    
    return installation

@route('/installation')
def recherche():
    '''
        fonction qui permet de récupérer les paamètres passés dans l'url et renvoit un objet json
    '''

    # Récuperation des argument passé en paramètre dans l'url
    activite = request.GET.get('activite',default=None)
    ville = request.GET.get('ville', default=None)
    items = installation(activite,ville)
    myDictionary = (list(map(todic,items)))
 
    return {'installations' : myDictionary}

@route('/ville')
def recherche():
    '''
        fonction qui permet de récupérer les paamètres passés dans l'url et renvoit un objet json
    '''
    resultat = []

    # connexion
    myDataBase = Dao()
    # myDataBase.connexion('localhost', 'CreationService', 'root', 'elnida')
    myDataBase.connexion('infoweb', 'E134705T', 'E134705T', 'E134705T')
    
    cur = myDataBase.getCursor()
    try:
        cur.execute("Select ville from installation")
        rows = cur.fetchall()
        for membre in rows:
            sort={}
            sort['ville']=(membre[0])
            resultat.append(sort)
    except Error.ProgrammingError:
        reparation = Reparation(dao)
        reparation.updateAll()
        
    return json.dumps(resultat)


class Test(unittest.TestCase):
    '''
        classe qui teste nos fonctions
    '''
    def test_toInstallation(self):
        argument = toInstallation([440010002, 'Terrain de Sports', 0, 'Le Bois Vert', 44170, 'Abbaretz', 47.5523, -1.53263])
        assert isinstance(argument, Installation)    

    def test_toEquipement(self):
        argument = toEquipement([66124, 'Court de Tennis', 723820001])
        assert isinstance(argument, Equipement) 
            
    def test_todic(self):
        argument = todic(toInstallation([440010002, 'Terrain de Sports', 0, 'Le Bois Vert', 44170, 'Abbaretz', 47.5523, -1.53263]))
        assert isinstance(argument, dict) 

if __name__ == '__main__':
    unittest.main()


