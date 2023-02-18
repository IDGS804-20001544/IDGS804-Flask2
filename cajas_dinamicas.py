from  wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FormField, SelectField, RadioField,IntegerField
from wtforms.fields import FieldList

class Cajas(Form):
    numero = IntegerField('txtNumero')
    numeros=FieldList(StringField('numero'),min_entries=1, max_entries=100)
  