
import mysql.connector.errors as Error


class Equipements_activites:

	def __init__(self,database):
		self.database=database

	def createTableEquipements_Assoc_activites(self):
		try:
			self.database.execute("CREATE TABLE equipements_Assoc_activites(codeActivite integer , idEquipement_Activite integer)")
		except Exception:
			print ('La table existe déjà')


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

	
	def addCle_Etrangere_Equipement(self):
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites ADD CONSTRAINT idEquipement_Activite FOREIGN KEY (idEquipement_Activite) REFERENCES equipement(idEquipement)")
		except Exception :
			print("this key is already exist")


	def dropCle_Etrangere_Equipement(self):
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites DROP FOREIGN KEY idEquipement_Activite ")
		except Error.DatabaseError:
			print("TABLE activite : clef etrangere inexistante")


	def addCle_Etrangere_Activite(self):
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites ADD CONSTRAINT codeActivite FOREIGN KEY (codeActivite) REFERENCES activite(codeActivite)")
		except Exception :
			print("this key is already exist")


	def dropCle_Etrangere_Activite(self):
		try:
			self.database.execute("ALTER TABLE equipements_Assoc_activites DROP FOREIGN KEY codeActivite ")
		except Error.DatabaseError:
			print("TABLE activite : clef etrangere inexistante")	
	
