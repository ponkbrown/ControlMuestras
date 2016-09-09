from flask import Flask, render_template
from flask_script import Manager
from models import db
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'muestras.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)
db.init_app(app)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/entrada')
def entrada():
    return render_template('entrega.html')

@app.route('/salida', methods=['GET','POST'])
def salida():
    return render_template('salida.html')

@app.route('/reporte')
def reporte():
    return render_template('reporte.html')


if __name__ == '__main__':
    manager.run()
