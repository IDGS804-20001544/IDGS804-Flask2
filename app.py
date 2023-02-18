from flask import Flask,render_template,request
import forms
import cajas_dinamicas
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.config['SECRET_KEY']="ESTA ES UNA LLAVE ENCRIPTADA"
csrf=CSRFProtect()

@app.route("/formprueba")
def prueba():
    
    return render_template("formprueba.html",)
 
@app.route("/Alumnos",methods=['POST', 'GET'])
def Alumnos():
    reg_alum=forms.UserForm(request.form)
    if request.method =='POST':
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template('Alumnos1.html',form=reg_alum)

@app.route("/Cajas",methods=['POST', 'GET'])
def cajas():
    numerocajas = request.form.get("txtNumero")
    numero= int(numerocajas or 0)
    n= int(numerocajas or 0)
    return render_template('cajas_dinamicas.html', numerocajas = numerocajas, numero = numero, n = n)


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
     #csrf.init_app(app)
     app.run(debug=True)   
     