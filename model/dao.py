import mysql.connector as mysql
from decimal import *
import mysql.connector.errors as Error
import time
import sys
sys.path.append("../logs")

class Dao:

	def __init__(self):
		self = self

	def connexion(self, host, database, user, password):
		
		try:
			self.conn=mysql.connect(host=host, database=database, user=user,password=password)
			self.cur=self.conn.cursor()
		except Error.ProgrammingError:
			print("CONNEXION : mauvais mot de passe")
 

	def deconnexion(self):
		self.cur.close()
		self.conn.close()


	def commit(self):
		self.conn.commit()


	def getCursor(self):
		return (self.cur)


	def createTableActivite(self):
		'''
			Cree une table activite
				numero - type integer, l'identifiant et la clef primaire de la table
				nom - type text, le nom de l'activite
				numeroEquipement - type integer, l'identifiant de l'equipement utilise
		'''
		try:
			self.cur.execute("CREATE TABLE activite(numero integer ,nom text, numeroEquipement integer, PRIMARY KEY (numero))")
		except Error.ProgrammingError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE activite : creation impossible car la table existe deja\n")
			log_activite.close()
			

	def insertInTableActivite(self, numero, nom, numeroEquipement):
		'''
			Insere une activite
		'''
		try:
			self.cur.execute("INSERT INTO activite (numero,nom, numeroEquipement) VALUES (%s,%s,%s)",(numero,nom,numeroEquipement))
		except Error.IntegrityError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE activite : impossible d'inserer l'activite n° "+numero+" car elle est deja presente dans la table\n")
			log_activite.close()

                        
	def deleInTableActivite(self,numero):
		try:
			delf.database.execute("DELETE FROM activite WHERE activite.numero=(%s)",(numero,))
		except Exception:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" Ce numero n'existe pas\n")
			log_activite.close()

                       
	def dropTableActivite(self):
		'''
			Supprime la table activite
		'''
		try:
			self.cur.execute("DROP TABLE IF EXISTS activite")
		except Error.IntegrityError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE activite : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes\n")
			log_activite.close()
		except AttributeError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE activite : ne peut etre supprimee car vous n'êtes pas connecté\n")
			log_activite.close()


	def createTableEquipement(self):
		'''
			Cree la table equipement
				numero - type integer, l'identifiant et la clef primaire d'un equipement
				nom - type text, le nom de l'equipement
				numeroInstallation - type integer, le numero de l'installation liee a la table
		'''	
		try:
			self.cur.execute("CREATE TABLE equipement(numero integer NOT NULL,nom text, numeroInstallation integer, PRIMARY KEY (numero))")
		except Error.ProgrammingError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipement : creation impossible car la table existe deja\n")
			log_equipement.close()


	def insertInTableEquipement(self, numero, nom, numeroInstallation):
		'''
			Insere un equipement 
				numero - type integer, l'identifiant et la clef primaire d'un equipement
				nom - type text, le nom de l'equipement
				numeroInstallation - type integer, le numero de l'installation liee a la table
		'''
		try:
			self.cur.execute("INSERT INTO equipement (numero,nom,numeroInstallation) VALUES (%s,%s,%s)",(numero,nom,numeroInstallation))
		except Error.IntegrityError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipement : impossible d'inserer l'equipement n° "+numero+" car elle est deja presente dans la table\n")
			log_equipement.close()

                                        
	def deleInTableEquipement(self,numero):
		try:
			self.cur.execute("DELETE FROM equipement WHERE equipement.numero=(%s)",(numero,))
		except Exception:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" Ce numero n'existe pas\n")
			log_equipement.close()
                        

	# AJOUT DE LA CLEF ETRANGERE

	def addForeignKeyInstallation(self):
		'''
			Ajoute une clef etrangere 'FK_Installation' sur la table equipement
				numeroInstallation de la table equipement fait reference a la clef primaire numero de la table installation 
		'''
		try:
			self.cur.execute("ALTER TABLE equipement ADD CONSTRAINT FK_Installation FOREIGN KEY  (numeroInstallation) REFERENCES installation(numero)")
		except Error.DatabaseError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipement : impossible d'ajouter la clef etrangere 'FK_Installation' car elle existe deja\n")
			log_installation.close()
		

	# DROP

	def dropForeignKeyInstallation(self):
		'''	
			Supprime la clef etrangere FK_Installation
		'''
		try:
			self.cur.execute("ALTER TABLE equipement DROP FOREIGN KEY FK_Installation")
		except Error.DatabaseError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipement : impossible de supprimer la clef etrangere 'FK_Installation' car elle n'existe pas\n")
			log_installation.close()
		except AttributeError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE installation : impossible de supprimer la clef etrangere 'FK_Installation' car vous n'êtes pas connecté\n")
			log_installation.close()


	def dropTableEquipement(self):
		'''
			Supprime la table equipement
		'''
		try:
			self.cur.execute("DROP TABLE IF EXISTS equipement")
		except Error.IntegrityError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes\n")
			log_equipement.close()
		except AttributeError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements : ne peut etre supprimee car vous n'êtes pas connecté\n")
			log_equipement.close()


	def createTableEquipements_Assoc_activites(self):
		'''
			Cree la table equipements_Assoc_activites, la table association entre les tables equipement et activite
				numeroActivite - type integer, l'identifiant et la clef primaire de la table activite
				numeroEquipement - type integer, l'identifiant de l'equipement utilisé par une activite
		'''
		try:
			self.cur.execute("CREATE TABLE equipements_Assoc_activites(numeroActivite integer NOT NULL, numeroEquipement integer NOT NULL)")
		except Error.ProgrammingError:
			log_equip_activ = open("logs/log_equip_activ.txt", "a")
			log_equip_activ.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : creation impossible car la table existe deja\n")
			log_equip_activ.close()
			

	def insertInTableEquipements_Assoc_activites(self, numeroActivite, numeroEquipement):
		'''
			Insere une ligne dans la table equipements_Assoc_activites
				numeroActivite - type integer, l'identifiant et la clef primaire de la table activite
				numeroEquipement - type integer, l'identifiant de l'equipement utilisé par une activite
		'''
		try:
			self.cur.execute("INSERT INTO equipements_Assoc_activites (numeroActivite, numeroEquipement) VALUES (%s,%s)",(numeroActivite,numeroEquipement))
		except Error.IntegrityError:
			log_equip_activ = open("logs/log_equip_activ.txt", "a")
			log_equip_activ.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : impossible s'inserer la ligne numeroActivite="+numeroActivite+" et numeroEquipement="+numeroEquipement+"car elle est deja presente dans la table\n")
			log_equip_activ.close()


	def deleInTableEquipements_Assoc_activites(self,numeroActivite):
		try:
			self.cur.execute("DELETE FROM equipements_Assoc_activites WHERE equipements_activites.numeroActivite=(%s)",(numeroActivite,))
		except Exception:
			log_equip_activ = open("logs/log_equip_activ.txt", "a")
			log_equip_activ.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" Ce numeroActivite n'existe pas\n")
			log_equip_activ.close()

	
	# AJOUT DES CLEFS ETRANGERES

	def addForeignKeyEquipement(self):
		'''
			Ajoute une clef etrangere 'FK_Equipement' sur la table equipements_activites
				numeroEquipement de la table equipements_activites fait reference a la clef primaire 'numero' de la table equipement 
		'''
		try:
			self.cur.execute("ALTER TABLE equipements_Assoc_activites ADD CONSTRAINT FK_Equipement FOREIGN KEY (numeroEquipement) REFERENCES equipement(numero)")
		except Error.DatabaseError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_activites : impossible d'ajouter la clef etrangere 'FK_Equipement' car elle existe deja\n")
			log_equipement.close()


	def addForeignKeyActivite(self):
		'''
			Ajoute une clef etrangere 'FK_Activite' sur la table equipements_activites
				numeroActivite de la table equipements_activites fait reference a la clef primaire 'numero' de la table activite 
		'''
		try:
			self.cur.execute("ALTER TABLE equipements_Assoc_activites ADD CONSTRAINT FK_Activite FOREIGN KEY (numeroActivite) REFERENCES activite(numero)")
		except Error.DatabaseError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_activites : impossible d'ajouter la clef etrangere 'FK_Activite' car elle existe deja\n")
			log_activite.close()


	# DROP
			
	def dropForeignKeyEquipement(self):
		'''
			Supprime la clef etrangere 'FK_Equipement'
		'''
		try:
			self.cur.execute("ALTER TABLE equipements_Assoc_activites DROP FOREIGN KEY FK_Equipement")
		except Error.DatabaseError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : impossible de supprimer la clef etrangere 'FK_Equipement' car elle n'existe pas\n")
			log_equipement.close()
		except AttributeError:
			log_equipement = open("logs/log_equipement.txt", "a")
			log_equipement.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipement : impossible de supprimer la clef etrangere 'FK_Equipement' car vous n'êtes pas connecté\n")
			log_equipement.close()


	def dropForeignKeyActivite(self):
		'''
			Supprime la clef etrangere 'FK_Activite'
		'''
		try:
			self.cur.execute("ALTER TABLE equipements_Assoc_activites DROP FOREIGN KEY FK_Activite")
		except Error.DatabaseError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : impossible de supprimer la clef etrangere 'FK_Activite' car elle n'existe pas\n")
			log_activite.close()
		except AttributeError:
			log_activite = open("logs/log_activite.txt", "a")
			log_activite.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : impossible de supprimer la clef etrangere 'FK_Activite' car elle n'existe pas\n")
			log_activite.close()


	def dropTableEquipements_Assoc_activites(self):
		'''
			Supprime la table equipements_Assoc_activites
		'''
		try:
			self.cur.execute("DROP TABLE IF EXISTS equipements_Assoc_activites")
		except Error.IntegrityError:
			log_equip_activ = open("logs/log_equip_activ.txt", "a")
			log_equip_activ.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes\n")
			log_equip_activ.close()
		except AttributeError:
			log_equip_activ = open("logs/log_equip_activ.txt", "a")
			log_equip_activ.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE equipements_Assoc_activites : impossible de supprimer la clef etrangere 'FK_Equipement' car vous n'êtes pas connecté\n")
			log_equip_activ.close()


	def createTableInstallation(self):
		'''
			Cree la table installation
				numero - type integer, l'identifiant et la clef primaire de la table
				nom - type text, le nom de l'installation
				voie - type integer, le numero de la voie
				adresse - type text, l'adresse de l'installation
				codePostal - type integer, le code postal de l'installation
				ville - type text, la ville de l'installation
				latitude - type float, la latitude de la position de l'installation
				longitude - type float, la longitude de la position de l'installation
		'''
		try:
			self.cur.execute("CREATE TABLE installation(numero integer NOT NULL,nom text, voie integer, adresse text, codePostal integer, ville text, latitude float ,longitude float, PRIMARY KEY (numero))")
		except Error.ProgrammingError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE installation : creation impossible car la table existe deja\n")
			log_installation.close()


	def insertInTableInstallation(self, numero, nom, voie, adresse, codePostal, ville, latitude, longitude):
		'''
			Insere une installation
				numero - type integer, l'identifiant et la clef primaire de la table
				nom - type text, le nom de l'installation
				voie - type integer, le numero de la voie
				adresse - type text, l'adresse de l'installation
				codePostal - type integer, le code postal de l'installation
				ville - type text, la ville de l'installation
				latitude - type float, la latitude de la position de l'installation
				longitude - type float, la longitude de la position de l'installation
		'''
		try:
			self.cur.execute("INSERT INTO installation (numero, nom, voie, adresse, codePostal, ville, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(numero,nom,voie,adresse,codePostal,ville,latitude,longitude))
		except Error.IntegrityError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE installation : impossible d'inserer l'installation n° "+numero+" car elle est deja presente dans la table\n")
			log_installation.close()

                        
	def deleInTableInstallation(self,numero):
		try:
			delf.database.execute("DELETE FROM installation WHERE installation.numero=(%s)",(numero,))
		except Exception:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" Ce numero n'existe pas\n")
			log_installation.close()
			

	def modiffierTableInstallation(self, numero, nom, voie, adresse, codePostal, ville, latitude, longitude):
		try:
			self.cur.execute("UPDATE installations SET numero=%s , nom=%s, voie=%s adresse=%s ,codePostal=%s ,ville=%s ,latitude=%s ,longitude=%s  WHERE numero = installations.numero",(numero,nom,voie,adresse,code_postal,ville,latitude,longitude))
		except Exception:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" Ce numero n'existe pas\n")
			log_installation.close()


	def dropTableInstallation(self):
		'''
			Supprime la table installation
		'''
		try:
			self.cur.execute("DROP TABLE IF EXISTS installation")
		except Error.IntegrityError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE installation : ne peut etre supprimee car une ou plusieurs clefs etrangeres sont presentes\n")
			log_installation.close()
		except AttributeError:
			log_installation = open("logs/log_installation.txt", "a")
			log_installation.write(time.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")+" TABLE installation : ne peut etre supprimee car vous n'êtes pas connecté\n")
			log_installation.close()			
			