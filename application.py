import installation
import Dao
import csv
import equipement
import equipements_activites_table


def creeBaseAndTables():
	myDataBase=Dao.Dao()
	inst=installation.Installation(myDataBase.getCursor())
	inst.createTableInstallation()

	equip=equipement.Equipement(myDataBase.getCursor())
	equip.createTableEquipement()

	equip_activ=equipements_activites_table.Equipements_activites(myDataBase.getCursor())
	equip_activ.createTableEquipements_activites()
	equip_activ.createTableEquipements_Assoc_activites()

	

def dropTables():
	myDataBase=Dao.Dao()
	inst=installation.Installation(myDataBase.getCursor())
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites_table.Equipements_activites(myDataBase.getCursor())

	inst.dropTableInstallation()
	equip.dropTableEquipement()
	equip_activ.dropTableEquipements_Assoc_activites()
	equip_activ.dropTableEquipements_activites()

	

def addConstraintKeys():
	myDataBase=Dao.Dao()
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites_table.Equipements_activites(myDataBase.getCursor())

	equip_activ.addCle_Etrangere()
	equip.addCle_Etrangere()

def dropConstraintKeys():
	myDataBase=Dao.Dao()
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites_table.Equipements_activites(myDataBase.getCursor())

	equip_activ.dropCle_Etrangere()
	equip.dropCle_Etrangere()


def application():
	"""
		test de la classe Installation
	"""
	myDataBase=Dao.Dao()
	inst=installation.Installation(myDataBase.getCursor())
	equip=equipement.Equipement(myDataBase.getCursor())
	equip_activ=equipements_activites_table.Equipements_activites(myDataBase.getCursor())

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
			equip_activ.insertInTableEquipements_activites(row[4],row[5],row[2])
			equip_activ.insertInTableEquipements_Assoc_activites(row[4],row[2])	
	csvfile.close()



	myDataBase.commit()
	myDataBase.deconnexion()


creeBaseAndTables()
addConstraintKeys()
application()
#dropConstraintKeys()
#dropTables()
