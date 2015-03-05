
class Equipement:

	def __init__(self,database):
		self.database=database


	def createTableEquipement(self):
		try:
			self.database.execute("CREATE TABLE equipement(idEquipement integer ,nomEquipement text, numeroInstallation_activite integer, PRIMARY KEY (idEquipement))")
		except Exception:
			print ("La table existe déjà")

	def insertInTableEquipement(self,idEquipement,nomEquipement,numeroInstallation_activite):
		try:
			self.database.execute("INSERT INTO equipement (idEquipement,nomEquipement,numeroInstallation_activite) VALUES (%s,%s,%s)",(idEquipement,nomEquipement,numeroInstallation_activite))
		except Exception:
			print("Vous ne pouvez pas rentrer deux idEquipement identique")


                        
	def dropTableEquipement(self):
                try:
                        self.database.execute("DROP TABLE IF EXISTS equipement")
                except Exception:
                        print ("Table inexistante")

                        
	def deleInTableEquipement(self,idEquipement):
                try:
                        delf.database.execute("DELETE FROM equipement WHERE equipement.idEquipement=(%s)",(idEquipement,))
                except Exception:
                        print("Ce idEquipement n'existe pas")

                        

	def afficheEquipement(self):
		for row in self.database.execute('SELECT * FROM equipement ORDER BY nomEquipement'):
			print (row)

	def addCle_Etrangere(self):
		try:
			self.database.execute("ALTER TABLE equipement ADD CONSTRAINT numeroInstallation_activite FOREIGN KEY  (numeroInstallation_activite) REFERENCES installations(numeroInstallation)")
		except Exception :
			print("this key is already exist")
		

	def dropCle_Etrangere(self):
		self.database.execute("ALTER TABLE equipement DROP FOREIGN KEY numeroInstallation_activite")