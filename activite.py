import mysql.connector.errors as Error

class Activite:

	def __init__(self,database):
		self.database=database


	def createTableActivite(self):
		try:
			self.database.execute("CREATE TABLE activite(codeActivite integer ,libeleActivite text, idEquipement_Activite integer, PRIMARY KEY (codeActivite))")
		except Exception:
			print ("La table existe déjà")


	def insertInTableActivite(self,codeActivite,libeleActivite, idEquipement_Activite):
		try:
			self.database.execute("INSERT INTO activite (codeActivite,libeleActivite, idEquipement_Activite) VALUES (%s,%s,%s)",(codeActivite,libeleActivite,idEquipement_Activite))
		except Exception:
			print("Vous ne pouvez pas rentrer deux codeActivite identique")

                        
	def dropTableActivite(self):
		self.database.execute("DROP TABLE IF EXISTS activite")

                        
	def deleInTableActivite(self,codeActivite):
		try:
			delf.database.execute("DELETE FROM activite WHERE activite.codeActivite=(%s)",(codeActivite,))
		except Exception:
			print("Ce codeActivite n'existe pas")

                       
	def afficheActivite(self):
		for row in self.database.execute('SELECT * FROM activite ORDER BY libeleActivite'):
			print (row)


	def addCle_Etrangere(self):
		try:
			self.database.execute("ALTER TABLE activite ADD CONSTRAINT idEquipement_Activite FOREIGN KEY (idEquipement_Activite) REFERENCES equipement(idEquipement)")
		except Exception :
			print("this key is already exist")


	def dropCle_Etrangere(self):
		try:
			self.database.execute("ALTER TABLE activite DROP FOREIGN KEY idEquipement_Activite ")
		except Error.DatabaseError:
			print("TABLE activite : clef etrangere inexistante")	