from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Orden(db.Model):
    __tablename__ = 'orden'
    id = db.Column(db.Integer, primary_key=True)
    muestra = db.Column(db.String(20), unique=True)
    empleado = db.Column(db.Integer)
    encargado = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Muestra %r>' % self.muestra
