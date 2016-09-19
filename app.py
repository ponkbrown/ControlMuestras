from flask import Flask, render_template, g, redirect, url_for
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, Muestra, Usuario, Orden, Admin
from formas import FormaBuscar, FormaSalida
from datetime import datetime
import os
from funciones import sanMuestras

# Borra esta linea, es para usar el debugger
import pdb

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'esta es una llave secreta'
#app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'muestras.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://muestras:muestras@localhost/muestras'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@app.before_request
def before_request():
    g.buscar = FormaBuscar()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if not g.buscar.validate_on_submit():
        return redirect(url_for('main'))
    return render_template('buscar.html', query = g.buscar.buscar.data)

@app.route('/entrada')
def entrada():
    return render_template('entrega.html')

@app.route('/salida', methods=['GET','POST'])
def salida():
    forma = FormaSalida()
    if forma.validate_on_submit():
        # Agarramos los datos de la forma
        usuario = int(forma.empleado.data)
        admin = int(forma.encargado.data)
        muestras = sanMuestras(forma.muestras.data) # sanizamos las muestras reviza el archivo de funciones en caso de que cambie el formato

        usuarioObj = db.session.query(Usuario).filter_by(numero=usuario).first()
        if not usuarioObj:
            usuarioObj = Usuario(numero=usuario)

        adminObj = db.session.query(Admin).filter_by(numero=admin).first()
        if not adminObj:
            adminObj = Admin(numero=admin)

        db.session.add_all([usuarioObj, adminObj])

        for a in muestras:
            muestraObj = Muestra(sku=a)
            db.session.add(muestraObj)
            orden = Orden(timestamp=datetime.now(), admin=adminObj, user=usuarioObj, muestra=muestraObj)
            db.session.add(orden)
        db.session.commit()
        return redirect(url_for('main'))

    return render_template('salida.html', salida=forma)

@app.route('/reporte')
def reporte():
    return render_template('reporte.html')

if __name__ == '__main__':
    manager.run()
