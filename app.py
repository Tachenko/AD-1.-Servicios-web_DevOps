
from flask import Flask

app = Flask(__name__)

HOST = '0.0.0.0'   #Localhost
PORT = 12345       #puerto indicado

#endpoint 1
@app.route('/')
def index():  
    file = open('files/archivo.txt','a+')     #crea el archivo si no existe y abre en modo anexar
    cadena = input ('Introduce una cadena de caracteres: \n')   #recoge la entrada por consola
    file.write(cadena + '\n')  #escribe en el fichero 
    file.close()               #cierra fichero
    return '<h1>received<h1>'  




#endpoint 2
@app.route('/read')
def readFile():
    filename = 'files/archivo.txt'  #almacenamos archivo en variable
    word = input ('Introduce una palabra para buscar: \n')

    with open(filename) as fileObj:   #abrimos archivo y almacenamos en variable
        lines = fileObj.readlines()   #leemos y almacenamos de nuevo en otra variable
        print("El archivo " + filename + " contiene " + str(len(lines)) + " cadenas")         #cuantas cadenas hay en el fichero 
        cont = 0  #iniciamos variable contador
        for line in lines:             #bucle for para recorrer linea a linea del archivo
               cont+=1
               print("Cadena " + str(cont) + ": La palabra " + word + " aparece " + str(line.count(word)) + " veces") #cuantas veces aparece la palabra en el ar4chivo
              





#metodo main para ejecutar programa
if __name__ == '__main__':
    app.run(debug=True,port=PORT)