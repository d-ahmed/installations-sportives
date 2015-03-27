import mysql.connector.errors as Error

class Equipement:

	def __init__(self, numero, nom, numeroInstallation):
		self.numero = numero
		self.nom = nom.decode()
		self.numeroInstallation = numeroInstallation
		self.activite = []

	def addActivite(self,activite):
		self.activite.append(activite)
	
	def __repr__(self):
		return "{} - {} - {} - {}".format(self.numero, self.nom, self.numeroInstallation, self.activite)	
		