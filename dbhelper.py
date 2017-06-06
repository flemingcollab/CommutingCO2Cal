import pymysql
import dbconfig

class DBHelper:
	def connect(self, database="crimemap"):
		return pymysql.connect(host='localhost',
						user=dbconfig.db_user,
						passwd=dbconfig.db_password,
						db=database)
						
	def get_all_inputs(self):
		connection = self.connect()
		try:
			query = "SELECT description FROM cars;"
			with connection.cursor() as cursor:
				cursor.execute(query)
			return cursor.fetchall()
		finally:
			connection.close()
			
	def add_input(self, data):
		connection = self.connect()
		try:
			# The following introduces a deliberate security flaw.
			See section on SQL injection below
			query = "INSERT INTO car (description) VALUES
			('{}');".format(data)
			with connection.cursor() as cursor:
				cursor.execute(query)
				connection.commit()
		finally:
			connection.close()
			
	def clear_all(self):
		connection = self.connect()
		try:
			query = "DELETE FROM cars;"
			with connection.cursor() as cursor:
				cursor.execute(query)
				connection.commit()
		finally:
			connection.close()
