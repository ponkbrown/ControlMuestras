# Sistema de muestras

Sistema para el control de muestras
es un sistema de bitacora para llevar el control de las muestras desde una 
base de datos


mié sep 21 14:20:45 MST 2016
Ya esta practicamente funcionando, para iniciar la base de datos
configura las credenciales:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://muestras:muestras@localhost/muestras'

y despues ejecuta:
python app.py db upgrade

con esto inicializas la base de datos y ya estas listo para capturar.
