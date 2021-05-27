import os
import mysql.connector
import xlrd
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

try:
	connection = mysql.connector.connect(host=os.environ.get('DB_HOST'), database=os.environ.get('DB_DB'), user=os.environ.get('DB_USER'), password=os.environ.get('DB_PASSWORD'))
	if connection.is_connected():
		table = xlrd.open_workbook('bancos.xls')
		sheet1 = table.sheet_by_index(0)
		cursor = connection.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS BANCOS (CODIGO INT NOT NULL, NOME VARCHAR(100), PRIMARY KEY (CODIGO))')
		for row in range(1, sheet1.nrows):
			query = 'INSERT INTO BANCOS (CODIGO, NOME) VALUES (%s, %s)'
			record = (sheet1.cell_value(rowx=row, colx=0), sheet1.cell_value(rowx=row, colx=1))
			result = cursor.execute(query, record)
			connection.commit()
			print('({codigo}, {nome}) inserted into table'.format(codigo=sheet1.cell_value(rowx=row, colx=0), nome=sheet1.cell_value(rowx=row, colx=1)))
except mysql.connector.Error as error:
	print('Failed to create table in MySQL: {}'.format(error))
finally:
	if connection.is_connected():
		cursor.close()
		connection.close()
		print('MySQL connection is closed')
