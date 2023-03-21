from flask import Flask,render_template,request
import forms
import Traductorforms
import cajas_dinamicas
import Resistencias
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash
from flask_wtf import FlaskForm
import json
from flask import redirect


app=Flask(__name__)
app.config['SECRET_KEY']="ESTA ES UNA LLAVE ENCRIPTADA"
csrf=CSRFProtect()

@app.route("/formprueba")
def prueba():
    
    return render_template("formprueba.html",)
 
@app.route("/Alumnos",methods=['POST', 'GET'])
def Alumnos():
    reg_alum=forms.UserForm(request.form)
    datos=list()
    if request.method =='POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template('Alumnos1.html',form=reg_alum,datos=datos)

@app.route("/cookie",methods=['POST', 'GET'])
def cookie():
    reg_user=forms.LoginForm(request.form)
    response=make_response(render_template("cookie.html",form=reg_user))
    
    if request.method =='POST' and reg_user.validate():
        user=reg_user.username.data
        password=reg_user.password.data
        datos=user+'@'+password
        success_message='Bienvenido{}'.format(user)
        response.set_cookie('datos_usuario',datos)
        flash(success_message)
    return response



@app.route("/Cajas",methods=['POST', 'GET'])
def cajas():
    numerocajas = request.form.get("txtNumero")
    numero= int(numerocajas or 0)
    n= int(numerocajas or 0)
    return render_template('cajas_dinamicas.html', numerocajas = numerocajas, numero = numero, n = n)


colores = [
    "negro",
    "cafe",
    "rojo",
    "naranja",
    "amarillo",
    "verde",
    "azul",
    "morado",
    "gris",
    "blanco",
]

color = ["oro", "plata"]

def calculate(bands):
    result = float(
        f"{colores.index(bands['ban1'])}{colores.index(bands['ban2'])}"
    ) * float(f"1{colores.index(bands['ban3']) * '0'}")
    min = result - (result * float(bands["tolerancia"]))
    max = result + (result * float(bands["tolerancia"]))
    return (
        bands["ban1"],
        bands["ban2"],
        bands["ban3"],
        bands["tolerancia"],
        result,
        min,
        max,
    )

@app.route("/Resistencia",methods=['POST', 'GET'])
def res():
     form = Resistencias.ResForm(request.form)
     datoss = list()

     filename = "resistencia.json"

     with open(filename, "r") as f:
        dataTemp = json.load(f)

     datos = [calculate(row) for row in dataTemp] if dataTemp != "" else False

     if request.method == "POST" and form.validate():
        banda1 = request.form.get("banda1")
        banda2 = request.form.get("banda2")
        banda3 = request.form.get("banda3")
        tolerancia = request.form.get("tolerancia")
        ban1 = colores[int(banda1)]
        ban2 = colores[int(banda2)]
        ban3 = colores[len(banda3)-1]

        datoss.append(ban1)
        datoss.append(ban2)
        datoss.append(ban3)
        datoss.append(tolerancia)

        f = open('resistencia.txt', 'a')
        f.write(ban1.upper())
        f.write(' ' + ban2.upper())
        f.write(' ' + ban3.upper())
        f.write(' ' + tolerancia.upper() + '\n')
        
        jsonObj = {
            "ban1": colores[int(banda1)],
            "ban2": colores[int(banda2)],
            "ban3": colores[len(banda3) - 1],
            "tolerancia": 
                tolerancia,
        }

        with open(filename, "w") as f:
            json.dump([jsonObj, *dataTemp], f)

        return redirect("/Resistencia")
    
     return render_template('Resistencias.html', form=form,datos=datos)
 
 

@app.route("/Traductor",methods=['POST', 'GET'])
def Traductor():
    reg_traduc=Traductorforms.Traduform(request.form)

    datos=list()
    lenguage=request.form.get('lenguage')
    
    if request.method =='POST' and reg_traduc.validate():
        datos.append(reg_traduc.español.data)
        datos.append(reg_traduc.ingles.data)
        f=open('traductor.txt','a')
        f.write('\n'+ reg_traduc.español.data.upper())
        f.write(' '+ reg_traduc.ingles.data.upper())
        
            
                    
    return render_template('Traductor.html',form=reg_traduc,datos=datos)

@app.route("/TraductorResult",methods=['POST', 'GET'])
def TraductorResult():
        lenguage=request.form.get('lenguage')
        tradu=request.form.get("txtPalabra").upper()
        f=open('traductor.txt', 'r') 
        palabras= f.read().splitlines()
        print(tradu)
        print(palabras)
        
        if lenguage == "2":
            palabra = [palabra.split(' ')[1] for palabra in palabras if palabra.split(' ')[0] == tradu]
            print(palabra)
        else:
           palabra = [palabra.split(' ')[0] for palabra in palabras if palabra.split(' ')[1] == tradu] 
           print(palabra)

        return render_template('TraductorResult.html',traducir=palabra)




@app.route("/CajasResultado",methods=['POST', 'GET'])
def cajas2():
    cajas=cajas_dinamicas.Cajas(request.form)
    arreglo=[int(numero or 0) for numero in cajas.numeros.data]
    print(cajas.numeros)
    suma=0
    total=len(arreglo)
    repeticiones={}
    
    for val in arreglo:
        suma=suma+val
        if val in repeticiones:
            repeticiones[val]+=1
        else:
            repeticiones[val]=1
            
    promedios= suma/total        
    ma=max(arreglo)
    mi=min(arreglo)
    return render_template('cajas_dinamicas_resultado.html',ma=ma,mi=mi,promedios=promedios,repeticiones=repeticiones)



     
if __name__ == "__main__":
     csrf.init_app(app)
     app.run(debug=True)   
     