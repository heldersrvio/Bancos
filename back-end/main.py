from app import app
from db import mysql
from flask import Flask, request

@app.route('/')
def index():
    return '<p>Hello</p>'

@app.route('/bankslist', methods=['GET'])
def banksList():
    cursor = mysql.get_db().cursor()
    query = 'SELECT NOME FROM BANCOS'
    cursor.execute(query)
    nomes = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return {
        'list': nomes
    }

@app.route('/bankname/<bank_code>', methods=['GET'])
def bankCode(bank_code):
    cursor = mysql.get_db().cursor()
    print(bank_code)
    query = 'SELECT NOME FROM BANCOS WHERE CODIGO = %s'
    cursor.execute(query, bank_code)
    nome = None if len(cursor.fetchall()) == 0 else cursor.fetchall()[0][0]
    cursor.close()
    return {
        'name': nome
    }