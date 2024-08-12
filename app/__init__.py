from flask import Flask
import mysql.connector
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configurar la conexión a la base de datos
    app.mysql = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    
    with app.app_context():
        from . import rutas
        
        return app
