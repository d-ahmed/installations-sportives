import mysql.connector.errors as Error

class Equipements_activites:

	def __init__(self,database):
		self.database=database

	def createTableEquipements_Assoc_activites(self):
		try:
			self.database.execute("CREATE TABLE equipements_Assoc_activites(codeActivite integer , idEquipement_Activite integer, PRIMARY KEY (codeActivite))")
		except Exception:
			print ("La table existe déjà")


	def insertInTableEquipements_Assoc_activites(self,codeActivite,idEquipement_Activite):
		try:
			self.database.execute("INSERT INTO equipements_Assoc_activites (codeActivite, idEquipement_Activite) VALUES (%s,%s)",(codeActivite,idEquipement_Activite))
		except Exception:
			print("Vous ne pouvez pas rentrer deux codeActivite identique")


	def dropTableEquipements_Assoc_activites(self):
		try:
			self.database.execute("DROP TABLE IF EXISTS equipements_Assoc_activites")
		except Exception:
			print ("Table inexistante")


	def deleInTableEquipements_Assoc_activites(self,codeActivite):
		try:
			self.database.execute("DELETE FROM equipements_Assoc_activites WHERE equipements_activites.codeActivite=(%s)",(codeActivite,))
		except Exception:
			print("Ce codeActivite n'existe pas")

