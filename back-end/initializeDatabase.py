from db import mysql
import xlrd

try:
	table = xlrd.open_workbook('bancos.xls')
	sheet1 = table.sheet_by_index(0)
	cursor = mysql.get_db().cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS BANCOS (CODIGO INT NOT NULL, NOME VARCHAR(100), PRIMARY KEY (CODIGO))')
	for row in range(1, sheet1.nrows):
		query = 'INSERT INTO BANCOS (CODIGO, NOME) VALUES (%s, %s)'
		record = (sheet1.cell_value(rowx=row, colx=0), sheet1.cell_value(rowx=row, colx=1))
		result = cursor.execute(query, record)
		print('({codigo}, {nome}) inserted into table'.format(codigo=sheet1.cell_value(rowx=row, colx=0), nome=sheet1.cell_value(rowx=row, colx=1)))
except Exception as error:
	print('Failed to create table in MySQL: {}'.format(error))
finally:
	cursor.close()
	print('Cursor is closed')
