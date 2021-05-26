from app import app
from db import mysql
from flask import Flask, request

@app.route('/bankslist')
def banksList():
    cursor = mysql.get_db().cursor()
    query = 'SELECT NOME FROM BANCOS'
    cursor.execute(query)
    nomes = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return {
        'list': nomes
    }

@app.route('/bankcode/<bank_name>')
def bankCode(bank_name):
    cursor = mysql.get_db().cursor()
    print(bank_name)
    query = 'SELECT CODIGO FROM BANCOS WHERE NOME = %s'
    cursor.execute(query, bank_name)
    codigo = cursor.fetchall()[0][0]
    cursor.close()
    return {
        'codigo': codigo
    }