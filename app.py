from flask import Flask, render_template, g, redirect, url_for, flash
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, Muestra, Usuario, Orden, Admin
from formas import FormaBuscar, FormaSalida, FormaEntrada
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
    g.buscador = FormaBuscar()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if not g.buscador.validate_on_submit():
        return redirect(url_for('main'))

    lista = sanMuestras(g.buscador.buscar.data) # sanizamos la busqueda para buscarlo en la base de datos
    for item in range(len(lista)):
        muestraObj = db.session.query(Muestra).filter_by(sku=lista[item]).first() # buscamos cada sku
        try:
            if muestraObj.cantidad < 0: lista[item] = muestraObj  # y si la cantidad es -1 lo agregamos a la lista que hay quey devolver
        except:
            continue
    return render_template('buscar.html', query = lista)

@app.route('/entrada/<pieza>', methods=['GET','POST'])
def entrada(pieza):
    forma = FormaEntrada()
    muestraObj = db.session.query(Muestra).filter_by(sku=pieza).first()

    if forma.validate_on_submit():
        usuario = int(forma.empleado.data)
        admin = int(forma.encargado.data)

        usuarioObj = db.session.query(Usuario).filter_by(numero=usuario).first()
        if not usuarioObj:
            usuarioObj = Usuario(numero=usuario)
        adminObj = db.session.query(Admin).filter_by(numero=admin).first()
        if not adminObj:
            adminObj = Admin(numero=admin)

        muestraObj.cantidad = 1
        ordenEntrega = Orden(muestra=muestraObj, usuario= usuarioObj, admin=adminObj, tipo='Entrada', timestamp = datetime.now())
        db.session.add(ordenEntrega)
        db.session.commit()
        flash('Se entrego la pieza: {}'.format(muestraObj.sku))
        return redirect(url_for('main'))

    return render_template('entrada.html', entrada=forma, pieza=muestraObj)

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
            muestraObj = db.session.query(Muestra).filter_by(sku=a).first()

            if not muestraObj:
                muestraObj = Muestra(sku=a)
                db.session.add(muestraObj)

            if muestraObj.cantidad == -1:
                db.session.rollback()
                flash('La muestra {} no esta en stock.'.format(muestraObj.sku))
                return redirect(url_for('salida'))

            muestraObj.cantidad = -1
            orden = Orden(timestamp=datetime.now(), tipo='Salida', admin=adminObj, usuario=usuarioObj, muestra=muestraObj)
            db.session.add(orden)
            flash('Se dio de alta la SALIDA: {}'.format(muestraObj.sku))
        db.session.commit()
        return redirect(url_for('main'))

    return render_template('salida.html', salida=forma)

@app.route('/reporte')
def reporte():
    flash('mensaje de prueba')
    flash('mensaje de prueba dos')
    flash('uno mas de curas', 'errors')
    return render_template('reporte.html')

if __name__ == '__main__':
    manager.run()
