
class Equipements_activites:

	def __init__(self,database):
		self.database=database


	def createTableEquipements_activites(self):
		try:
			self.database.execute("CREATE TABLE equipements_activites(codeActivite integer ,libeleActivite text, idEquipement_Activite integer, PRIMARY KEY (codeActivite))")
		except Exception:
			print ("La table existe déjà")


	def createTableEquipements_Assoc_activites(self):
		try:
			self.database.execute("CREATE TABLE equipements_Assoc_activites(codeActivite integer , idEquipement_Activite integer, PRIMARY KEY (codeActivite))")
		except Exception:
			print ("La table existe déjà")



	def insertInTableEquipements_activites(self,codeActivite,libeleActivite, idEquipement_Activite):
		try:
			self.database.execute("INSERT INTO equipements_activites (codeActivite,libeleActivite, idEquipement_Activite) VALUES (%s,%s,%s)",(codeActivite,libeleActivite,idEquipement_Activite))
		except Exception:
			print("Vous ne pouvez pas rentrer deux codeActivite identique")


	def insertInTableEquipements_Assoc_activites(self,codeActivite,idEquipement_Activite):
		try:
			self.database.execute("INSERT INTO equipements_Assoc_activites (codeActivite, idEquipement_Activite) VALUES (%s,%s)",(codeActivite,idEquipement_Activite))
		except Exception:
			print("Vous ne pouvez pas rentrer deux codeActivite identique")


                        
	def dropTableEquipements_activites(self):
		try:
			self.database.execute("DROP TABLE IF EXISTS equipements_activites")
		except Exception:
			print ("Table inexistante")

	def dropTableEquipements_Assoc_activites(self):
		try:
			self.database.execute("DROP TABLE IF EXISTS equipements_Assoc_activites")
		except Exception:
			print ("Table inexistante")

                        
	def deleInTableEquipements_activites(self,codeActivite):
		try:
			delf.database.execute("DELETE FROM equipements_activites WHERE equipements_activites.codeActivite=(%s)",(codeActivite,))
		except Exception:
			print("Ce codeActivite n'existe pas")

	def deleInTableEquipements_Assoc_activites(self,codeActivite):
		try:
			delf.database.execute("DELETE FROM equipements_Assoc_activites WHERE equipements_activites.codeActivite=(%s)",(codeActivite,))
		except Exception:
			print("Ce codeActivite n'existe pas")

                        

	def afficheEquipements_activites(self):
		for row in self.database.execute('SELECT * FROM equipements_activites ORDER BY libeleActivite'):
			print (row)



	def modiffierTableInstallation(self,codeActivite,libeleActivite, idEquipement_Activite):
		try:
			self.database.execute("UPDATE equipements_activites SET codeActivite=%s , libeleActivite=%s idEquipement_Activite=%s WHERE numero,  = equipements_activites.codeActivite",(codeActivite,libeleActivite, idEquipement_Activite))
		except Exception:
			print("le numero n'existe pas")

	def addCle_Etrangere(self):
		try:
			self.database.execute("ALTER TABLE equipements_activites ADD CONSTRAINT idEquipement_Activite FOREIGN KEY (idEquipement_Activite) REFERENCES equipement(idEquipement)")
		except Exception :
			print("this key is already exist")

	def dropCle_Etrangere(self):
		self.database.execute("ALTER TABLE equipements_activites DROP FOREIGN KEY idEquipement_Activite ")