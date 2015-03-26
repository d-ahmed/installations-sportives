from model import Dao 
import csv


# connexion a la base de donnee en fonction de l'utilisateur
print ("daniel ou aurelie ?")
prenom = input()

while (prenom != "daniel" and prenom != "aurelie"):
	print ("daniel ou aurelie ?")
	prenom = input()

print ("Entrer votre mots de passe")
password = input()

dao=Dao.Dao()
if(prenom=="aurelie"):
	dao.connexion('infoweb', 'E134705T', 'E134705T', password)
else:
	dao.connexion('localhost', 'CreationService', 'root', password)


def createTables():
	'''
		Cree les tables installation, equipement et equipements_activites
	'''
	# Création des tables
	dao.createTableInstallation()
	dao.createTableEquipement()
	dao.createTableEquipements_Assoc_activites()
	dao.createTableActivite()


def dropTables():
	'''
		Supprime les tables installation, equipement et equipements_activites
	'''

	dao.dropTableInstallation()
	dao.dropTableEquipement()
	dao.dropTableEquipements_Assoc_activites()
	dao.dropTableActivite()
	

def addForeignKeys():
	'''	
		Ajoute les clefs etrangeres sur les tables equipement et equipements_Assoc_activites
	'''
	dao.addForeignKeyInstallation()
	dao.addForeignKeyEquipement()
	dao.addForeignKeyActivite()


def dropForeignKeys():
	'''
		Supprime les clefs etrangeres des tables equipement et equipements_Assoc_activites
	'''
	dao.dropForeignKeyInstallation()
	dao.dropForeignKeyEquipement()
	dao.dropForeignKeyActivite()


def insertIntoTables():
	"""
		Insere les donnees dans les tables installation, equipement, equipements_Assoc_activites et activite
	"""

	# Table activite
	with open('./csv/equipements_activites_table.csv','rt') as csvfile:
		activite_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(activite_tableReader,None)
		for row in activite_tableReader:
			dao.insertInTableActivite(row[4],row[5],row[2])
			#equip_activ.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()

	# Table installation
	with open('./csv/installations_table.csv','rt') as csvfile:
		installations_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(installations_tableReader,None)
		for row in installations_tableReader:
			dao.insertInTableInstallation(row[1],row[0], row[6], row[7],row[4],row[2],row[10],row[9])
	csvfile.close()

	
	# Table equipement
	with open('./csv/equipements.csv','rt') as csvfile:
		equipement_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(equipement_tableReader,None)
		for row in equipement_tableReader:
			dao.insertInTableEquipement(row[4],row[5],row[2])
	csvfile.close()


	# Table equipements_Assoc_activites
	with open('./csv/equipements_activites_table.csv','rt') as csvfile:
		equipements_activites_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(equipements_activites_tableReader,None)
		for row in equipements_activites_tableReader:
			dao.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()

	dao.commit()
	dao.deconnexion()



createTables()
addForeignKeys()
insertIntoTables()
#dropForeignKeys()
#dropTables()
