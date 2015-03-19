from model import installation
from model import Dao 
import csv
from model import equipement
from model import activite
from model import equipements_activites


# connexion a la base de donnee en fonction de l'utilisateur
print ("daniel ou aurelie ?")
prenom = input()
print ("Entrer votre mots de passe")
password = input()

dao=Dao.Dao()
if(prenom=="aurelie"):
	dao.connexion('infoweb', 'E134705T', 'E134705T', password)
else:
	dao.connexion('localhost', 'CreationService', 'root', password)

# On récupère les curseurs pour l'initialisation des classes
curseurInstallation = installation.Installation(dao.getCursor())
curseurEquipement = equipement.Equipement(dao.getCursor())
curseurEquipementActivite = equipements_activites.Equipements_activites(dao.getCursor())
curseurActivite = activite.Activite(dao.getCursor())


def createTables():
	'''
		Cree les tables installation, equipement et equipements_activites
	'''
	# Création des tables
	curseurInstallation.createTableInstallation()
	curseurEquipement.createTableEquipement()
	curseurEquipementActivite.createTableEquipements_Assoc_activites()
	curseurActivite.createTableActivite()


def dropTables():
	'''
		Supprime les tables installation, equipement et equipements_activites
	'''

	curseurInstallation.dropTableInstallation()
	curseurEquipement.dropTableEquipement()
	curseurEquipementActivite.dropTableEquipements_Assoc_activites()
	curseurActivite.dropTableActivite()
	

def addForeignKeys():
	'''	
		Ajoute les clefs etrangeres sur les tables equipement et equipements_Assoc_activites
	'''
	curseurEquipement.addForeignKeyInstallation()
	curseurEquipementActivite.addForeignKeyEquipement()
	curseurEquipementActivite.addForeignKeyActivite()


def dropForeignKeys():
	'''
		Supprime les clefs etrangeres des tables equipement et equipements_Assoc_activites
	'''
	curseurEquipement.dropForeignKeyInstallation()
	curseurEquipementActivite.dropForeignKeyEquipement()
	curseurEquipementActivite.dropForeignKeyActivite()


def insertIntoTables():
	"""
		Insere les donnees dans les tables installation, equipement, equipements_Assoc_activites et activite
	"""

	# Table activite
	with open('./csv/equipements_activites_table.csv','rt') as csvfile:
		activite_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(activite_tableReader,None)
		for row in activite_tableReader:
			curseurActivite.insertInTableActivite(row[4],row[5],row[2])
			#equip_activ.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()

	# Table installation
	with open('./csv/installations_table.csv','rt') as csvfile:
		installations_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(installations_tableReader,None)
		for row in installations_tableReader:
			curseurInstallation.insertInTableInstallation(row[1],row[0],row[7],row[4],row[2],row[10],row[9])
	csvfile.close()

	
	# Table equipement
	with open('./csv/equipements.csv','rt') as csvfile:
		equipement_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(equipement_tableReader,None)
		for row in equipement_tableReader:
			curseurEquipement.insertInTableEquipement(row[4],row[5],row[2])
	csvfile.close()


	# Table equipements_Assoc_activites
	with open('./csv/equipements_activites_table.csv','rt') as csvfile:
		equipements_activites_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(equipements_activites_tableReader,None)
		for row in equipements_activites_tableReader:
			curseurEquipementActivite.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()

	dao.commit()
	dao.deconnexion()



createTables()
addForeignKeys()
insertIntoTables()
#dropForeignKeys()
#dropTables()
