from  wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField, SelectField, RadioField

from wtforms.fields import EmailField, TextAreaField, PasswordField,RadioField
from wtforms import validators

#def mi_validacion(form,field):
 #   if len(field.data)==0:
  #      raise validators.ValidationError('El campo no tiene datos')
    
class Traduform(Form):
    español= StringField('Español',[validators.DataRequired(message="El campo es requerido"), 
                                      validators.length(min=1)])
    
    ingles=StringField('Ingles',[validators.DataRequired(message="El campo es requerido"), 
                                 validators.length(min=1)])

class Traducidoform(Form):
    traducir=StringField('Traducir')

    
    


    
    
    
