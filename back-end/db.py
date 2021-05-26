import os
from dotenv import load_dotenv
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
load_dotenv()

app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DB_DB')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('DB_HOST')
mysql.init_app(app)