import mysql.connector as mysql

from mysql.connector import Error


class Dao:

	def __init__(self):

		#self.conn=mysql.connector.connect('host=infoweb','user=E134705T','password=E134705T','db=CreationService',)
		#self.connexion(host, database, user, password)
		self = self


	def connexion(self, host, database, user, password):
		try:

			self.conn=mysql.connect(host=host, database=database, user=user,password=password)
			self.cur=self.conn.cursor()
		except Error as e:
			print(e)
 

	def deconnexion(self):
		self.conn.close()


	def commit(self):
		self.conn.commit()


	def getCursor(self):
		return (self.cur)