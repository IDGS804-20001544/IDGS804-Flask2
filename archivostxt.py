f=open('alumnos.txt','r')

"""alumnos=f.read()
print(alumnos)
f.seek(20)
alumnos2=f.read()
print(alumnos2)"""
alumnos=f.readlines()
alumnos1=f.readline()
print(alumnos1)

print(alumnos)
print(alumnos[0])
for item in alumnos:
    print(item,end='')
f.close()

#crea un nuevo archivo y write es para escribir en el texto
f=open('alumnos2.txt','a')
f.write("\n"+"Hola mundo!!")
f.write("\n"+"Nuevo Hola Mundo!!")
f.close()



