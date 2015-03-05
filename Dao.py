import mysql.connector as mysql


class Dao:

	def __init__(self):
		#self.conn=self.connexion('localhost','root','elnida','CreationService',)
		#self.cur=self.conn.cursor()

	def connexion(self,host,user,passwd,db):
		try:
			self.conn=mysql.connect(host=host,database=db,user=user,password=password)
			self.cur=self.conn.cursor()
		except Exception:
			print ("e.str")
		


	def deconnexion(self):
		self.conn.close()

	def commit(self):
		self.conn.commit()

	def getCursor(self):
		return (self.cur)