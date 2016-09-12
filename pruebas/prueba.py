from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    mascotas = db.relationship('Mascota', backref='propietario', lazy='dynamic')

class Mascota(db.Model):
    __tablename__ = 'mascota'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    new = db.Column(db.String(20))
    propietario_id = db.Column(db.Integer, db.ForeignKey('persona.id'))



if __name__ == '__main__':
    manager.run()
