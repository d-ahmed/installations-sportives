import installation
import Dao
import csv
import equipement
import equipements_activites_table




"""
Création dela base de donnée
"""
myDataBase=Dao.Dao()
inst=installation.Installation(myDataBase.getCursor())
inst.createTableInstallation();

equip=equipement.Equipement(myDataBase.getCursor())
equip.createTableEquipement();

equip_activ=equipements_activites_table.Equipements_activites(myDataBase.getCursor())
equip_activ.createTableEquipements_activites();
equip_activ.createTableEquipements_Assoc_activites();


"""
Ajout de contrainte
"""
equip_activ.addCle_Etrangere();
equip.addCle_Etrangere();


"""
	test de la classe Installation
"""
with open('./csv/installations_table.csv','rt') as csvfile:
	installations_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in installations_tableReader:
		inst.insertInTableInstallation(row[1],row[0])
		myDataBase.commit()
csvfile.close()


"""
	test de la classe Equipement
"""
with open('./csv/equipements.csv','rt') as csvfile:
	equipement_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in equipement_tableReader:
		equip.insertInTableEquipement(row[4],row[5],row[2])
		myDataBase.commit()
csvfile.close()


"""
	test de la classe Equipements_activites
"""
with open('./csv/equipements_activites_table.csv','rt') as csvfile:
	equipements_activites_tableReader=csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in equipements_activites_tableReader:
		equip_activ.insertInTableEquipements_activites(row[4],row[5],row[2])
		equip_activ.insertInTableEquipements_Assoc_activites(row[4],row[2])
		myDataBase.commit()
csvfile.close()




myDataBase.deconnexion()



