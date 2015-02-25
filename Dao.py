import pymysql as mysql


class Dao:

	def __init__(self):
		self.conn=self.connexion('localhost','root','elnida','CreationService',)
		self.cur=self.conn.cursor()


	def connexion(self,host,user,passwd,db):
		try:
			connect=mysql.connect(host=host,user=user,passwd=passwd,db=db)
		except Exception:
			print ("e.str")
		return connect


	def deconnexion(self):
		self.conn.close()

	def commit(self):
		self.conn.commit()

	def getCursor(self):
		return (self.cur)