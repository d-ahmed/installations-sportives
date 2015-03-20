import mysql.connector.errors as Error

class Equipement:

	def __init__(self, numero, nom, numeroInstallation):
		self.numero = numero
		self.nom = nom
		self.numeroInstallation = numeroInstallation

		
	def __repr__(self):
        return "{} - {} - {}".format(self.numero, self.nom, self.numeroInstallation)	
		