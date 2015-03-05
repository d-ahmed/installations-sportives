import installation
import Dao
import csv
import equipement
import activite
import equipements_activites


print ("daniel ou aurelie ?")
prenom = input()
print ("Entrer votre mots de passe")
password = input()

myDataBase=Dao.Dao()
if(prenom=="aurelie"):
	myDataBase.connexion('infoweb', 'E134705T', 'E134705T', password)
else:
	myDataBase.connexion('localhost', 'CreationService', 'root', password)



def createTables():
	'''
		Fonction qui cree les tables installation, equipement et equipements_activites
	'''

	# On récupère les curseurs pour l'initialisation des classes
	inst=installation.Installation(myDataBase.getCursor())
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites.Equipements_activites(myDataBase.getCursor())
	activit=activite.Activite(myDataBase.getCursor())

	# Création des tables
	inst.createTableInstallation()
	equip.createTableEquipement()
	equip_activ.createTableEquipements_Assoc_activites()
	activit.createTableActivite()


def dropTables():
	'''
		Fonction qui detruit les tables installation, equipement et equipements_activites
	'''

	# On récupère les curseurs pour l'initialisation des classes
	inst=installation.Installation(myDataBase.getCursor())
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites.Equipements_activites(myDataBase.getCursor())
	activit=activite.Activite(myDataBase.getCursor())

	inst.dropTableInstallation()
	equip.dropTableEquipement()
	equip_activ.dropTableEquipements_Assoc_activites()
	activit.dropTableActivite()

	

def addConstraintKeys():
	
	equip=equipement.Equipement(myDataBase.getCursor())
	activit=activite.Activite(myDataBase.getCursor())

	activit.addCle_Etrangere()
	equip.addCle_Etrangere()

def dropConstraintKeys():
	
	equip=equipement.Equipement(myDataBase.getCursor())
	activit=activite.Activite(myDataBase.getCursor())

	equip.dropCle_Etrangere()
	activit.dropCle_Etrangere()


def application():
	"""
		test de la classe Installation
	"""
	
	inst=installation.Installation(myDataBase.getCursor())
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites.Equipements_activites(myDataBase.getCursor())
	activit=activite.Activite(myDataBase.getCursor())

	with open('./csv/installations_table.csv','rt') as csvfile:
		installations_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(installations_tableReader,None)
		for row in installations_tableReader:
			inst.insertInTableInstallation(row[1],row[0],row[7],row[4],row[2],row[10],row[9])
	csvfile.close()


	"""
		test de la classe Equipement
	"""

	with open('./csv/equipements.csv','rt') as csvfile:
		equipement_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(equipement_tableReader,None)
		for row in equipement_tableReader:
			equip.insertInTableEquipement(row[4],row[5],row[2])
	csvfile.close()


	"""
		test de la classe Equipements_activites
	"""

	with open('./csv/equipements_activites_table.csv','rt') as csvfile:
		equipements_activites_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(equipements_activites_tableReader,None)
		for row in equipements_activites_tableReader:
			equip_activ.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()



	"""
		test de la classe Activite
	"""

	with open('./csv/equipements_activites_table.csv','rt') as csvfile:
		activite_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
		next(activite_tableReader,None)
		for row in activite_tableReader:
			activit.insertInTableActivite(row[4],row[5],row[2])
			#equip_activ.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()
	


	myDataBase.commit()
	myDataBase.deconnexion()


createTables()
addConstraintKeys()
application()
#dropConstraintKeys()
#dropTables()
