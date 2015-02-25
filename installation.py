
class Installation :


	def __init__(self,database):
		self.database=database


	def createTableInstallation(self):
		try:
			self.database.execute("CREATE TABLE installations(numeroInstallation integer ,nomInstallation text, PRIMARY KEY (numeroInstallation))")
		except Exception:
			print ("La table existe déjà")



	def insertInTableInstallation(self,numeroInstallation,nomInstallation):
		try:
			self.database.execute("INSERT INTO installations (numeroInstallation,nomInstallation) VALUES (%s,%s)",(numeroInstallation,nomInstallation))
		except Exception:
			print("Vous ne pouvez pas rentrer deux numeroInstallation identique")


                        
	def dropTableInstallation(self):
                try:
                        self.database.execute("DROP TABLE IF EXISTS installations")
                except Exception:
                        print ("Table inexistante")

                        
	def deleInTableInstallation(self,numeroInstallation):
                try:
                        delf.database.execute("DELETE FROM installations WHERE installations.numeroInstallation=(%s)",(numeroInstallation,))
                except Exception:
                        print("Ce numeroInstallation n'existe pas")

                        

	def afficheInstallation(self):
		for row in self.database.execute('SELECT * FROM installations ORDER BY nomInstallation'):
			print (row)


	def modiffierTableInstallation(self,numeroInstallation,nomInstallation):
		try:
			self.database.execute("UPDATE installations SET numeroInstallation=%s , nomInstallation=%s WHERE numeroInstallation = installations.numeroInstallation",(numeroInstallation,nomInstallation))
		except Exception:
			print("le numeroInstallation n'existe pas")