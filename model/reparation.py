import csv

class Reparation:
	'''
		fonction qui met à jour toute la base de données
	'''
	def __init__(self, dao):
		self.dao = dao

	def updateAll(self):
		print("========== Suppression des clefs ==========")
		self.dao.dropForeignKeyInstallation()
		self.dao.dropForeignKeyEquipement()
		self.dao.dropForeignKeyActivite()

		print("========== Suppression des tables ==========")
		self.dao.dropTableInstallation()
		self.dao.dropTableEquipement()
		self.dao.dropTableEquipements_Assoc_activites()
		self.dao.dropTableActivite()

		print("========== Création des tables ==========")
		self.dao.createTableInstallation()
		self.dao.createTableEquipement()
		self.dao.createTableEquipements_Assoc_activites()
		self.dao.createTableActivite()
		
		print("==========  Création des clefs ==========")
		self.dao.addForeignKeyInstallation()
		self.dao.addForeignKeyEquipement()
		self.dao.addForeignKeyActivite()	

		print("========== Insertion dans les tables ==========")
		with open('./csv/equipements_activites_table.csv','rt') as csvfile:
			activite_tableReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(activite_tableReader,None)
			for row in activite_tableReader:
				self.dao.insertInTableActivite(row[4],row[5],row[2])			
		csvfile.close()

		with open('./csv/installations_table.csv','rt') as csvfile:
			installations_tableReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(installations_tableReader,None)
			for row in installations_tableReader:
				self.dao.insertInTableInstallation(row[1],row[0], row[6], row[7],row[4],row[2],row[10],row[9])
		csvfile.close()

		with open('./csv/equipements.csv','rt') as csvfile:
			equipement_tableReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(equipement_tableReader,None)
			for row in equipement_tableReader:
				self.dao.insertInTableEquipement(row[4],row[5],row[2])
		csvfile.close()

		with open('./csv/equipements_activites_table.csv','rt') as csvfile:
			equipements_activites_tableReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(equipements_activites_tableReader,None)
			for row in equipements_activites_tableReader:
				self.dao.insertInTableEquipements_Assoc_activites(row[4],row[2])	
		csvfile.close()

		self.dao.commit()		
