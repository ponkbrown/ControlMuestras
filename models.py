from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Orden(db.Model):
    __tablename__ = 'orden'
    id = db.Column(db.Integer, primary_key=True)
    muestra_id = db.Column(db.Integer, db.ForeignKey('muestra.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    tipo = db.Column(db.String(7), nullable=False) # Entrada o Salida
    timestamp = db.Column(db.DateTime)

class Muestra(db.Model):
    __tablename__ = 'muestra'

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20))
    rfid = db.Column(db.String(20))
    cantidad = db.Column(db.Integer)
    ordenes = db.relationship('Orden', backref='muestra')

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    numero = db.Column(db.Integer)
    rfid = db.Column(db.String(20))
    ordenes = db.relationship('Orden', backref='usuario')

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    numero = db.Column(db.Integer)
    rfid = db.Column(db.String(20))
    ordenes = db.relationship('Orden', backref='admin')
