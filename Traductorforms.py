from  wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField, SelectField, RadioField

from wtforms.fields import EmailField, TextAreaField, PasswordField,RadioField
from wtforms import validators


    
class Traduform(Form):
    español= StringField('Español',[validators.DataRequired(message="El campo es requerido"), 
                                      validators.length(min=1)])
    
    ingles=StringField('Ingles',[validators.DataRequired(message="El campo es requerido"), 
                                 validators.length(min=1)])



    
    


    
    
    
