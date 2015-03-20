import mysql.connector.errors as Error

class Activite:

	def __init__(self, numero, nom, numeroEquipement):
		self.numero = numero
		self.nom = nom 
		self.numeroEquipement = numeroEquipement


	def __repr__(self):
        return "{} - {} - {}".format(self.numero, self.nom, self.numeroEquipement)	