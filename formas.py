from flask_wtf import Form as FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, DateTimeField, BooleanField
from wtforms.validators import DataRequired

class FormaBuscar(FlaskForm):
    buscar = StringField('Buscar', validators=[DataRequired()])

class FormaSalida(FlaskForm):
    muestras = TextAreaField('Muestras', validators=[DataRequired()])
    empleado = DecimalField('Empleado', validators=[DataRequired()])
    encargado = DecimalField('Encargado', validators=[DataRequired()])

class FormaEntrada(FlaskForm):
    empleado = DecimalField('Empleado', validators=[DataRequired()])
    encargado = DecimalField('Encargado', validators=[DataRequired()])
