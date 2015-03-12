import mysql.connector.errors as Error

class Activite:

	def __init__(self,database):
		self.database=database


	def createTableActivite(self):
		'''
			Cree une table activite
				numero - type integer, l'identifiant et la clef primaire de la table
				nom - type text, le nom de l'activite
				numeroEquipement - type integer, l'identifiant de l'equipement utilise
		'''
		try:
			self.database.execute("CREATE TABLE activite(numero integer ,nom text, numeroEquipement integer, PRIMARY KEY (numero))")
		except Error.ProgrammingError:
			print ("TABLE activite : creation impossible car la table existe deja")


	def insertInTableActivite(self, numero, nom, numeroEquipement):
		'''
			Insere une activite
		'''
		try:
			self.database.execute("INSERT INTO activite (numero,nom, numeroEquipement) VALUES (%s,%s,%s)",(numero,nom,numeroEquipement))
		except Error.IntegrityError:
			print("TABLE activite : impossible d'inserer l'activite n° "+numero+" car elle est deja presente dans la table")

                        
	def deleInTableActivite(self,numero):
		try:
			delf.database.execute("DELETE FROM activite WHERE activite.numero=(%s)",(numero,))
		except Exception:
			print("Ce numero n'existe pas")

                       
	def afficheActivite(self):
		for row in self.database.execute('SELECT * FROM activite ORDER BY libeleActivite'):
			print (row)


	def dropTableActivite(self):
		'''
			Supprime la table activite
		'''
		try:
			self.database.execute("DROP TABLE IF EXISTS activite")
		except Error.IntegrityError:
			print("TABLE activite : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes")			