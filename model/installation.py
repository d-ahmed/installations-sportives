from equipement import Equipement
class Installation:
	def __init__(self, numero, nom, voie, adresse, codePostal, ville, latitude, longitude):
		self.numero = numero
		self.nom = nom
		self.voie=voie
		self.adresse = adresse
		self.codePostal = codePostal
		self.ville = ville
		self.latitude = latitude
		self.longitude = longitude
		self.equipement = []

	def addEquipement(self,equipement):
		self.equipement.append(equipement)

	def __repr__(self):
	 	return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.numero, self.nom, self.adresse, self.codePostal, self.ville, self.latitude, self.longitude, self.equipement)	