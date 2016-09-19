from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Orden(db.Model):
    __tablename__ = 'orden'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    pieza = db.relationship('Pieza', backref='orden', lazy='dynamic')
    encargado = db.relationship('Encargado', backref='orden', lazy='dynamic')
    empleado = db.relationship('Empleado', backref='orden', lazy='dynamic')

class Pieza(db.Model):
    __tablename__ = 'pieza'
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20))
    rfid = db.Column(db.String(20))
    vol = db.Column(db.Integer)
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'))

class Encargado(db.Model):
    __tablename__ =  'encargado'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    rfid = db.Column(db.String(20))
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'))

class Empleado(db.Model):
    __tablename__ =  'empleado'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    rfid = db.Column(db.String(20))
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'))

    def __repr__(self):
        return '<Muestra %r>' % self.sku
