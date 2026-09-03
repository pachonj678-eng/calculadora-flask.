from flask import Flask
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

# Ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask! - SENA ADSO</h1><hr>"

# 1.) Promedio de notas (30%, 30% y 40%)
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1 * 30) / 100 + (nota2 * 30) / 100 + (nota3 * 40) / 100
    return f"<h1>El resultado es: {resultado}</h1><hr>"

# 2.) Clasificación de edades
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad < 18:
        R = "menor de edad"
    elif edad < 60:
        R = "Adulto"
    else:
        R = "Adulto mayor"
    return f"<h1>La persona es: {R}</h1><hr>"

# 3.) Arreglos y matrices aleatorias con Numpy
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=10, columnas=5, filas=0):
    if filas == 0:
        arreglo = np.random.randint(valores, size=columnas)
    else:
        arreglo = np.random.randint(valores, size=(filas, columnas))
    return f"<h1>El arreglo aleatorio es: {arreglo.tolist()}</h1><hr>"

# --- EJERCICIOS PROPUESTOS ---

# Ejercicio 1: Ecuación Y = X * Z + Z + X
@app.route("/ecuacion/<float:x>/<float:z>")
def ecuacion(x=0, z=0):
    y = (x * z) + z + x
    return f"<h1>El resultado de la ecuación Y = X*Z + Z + X es: {y}</h1><hr>"

# Ejercicio 2: Tabla de multiplicar hasta el 10
@app.route("/tabla/<int:num>")
def tabla(num=1):
    resultado = f"<h3>Tabla de multiplicar del {num}</h3><ul>"
    for i in range(1, 11):
        resultado += f"<li>{num} x {i} = {num * i}</li>"
    resultado += "</ul><hr>"
    return resultado

# Ejercicio 3: Áreas de círculo, cuadrado y triángulo
@app.route("/area/<figura>/<float:p1>")
@app.route("/area/<figura>/<float:p1>/<float:p2>")
def area(figura, p1=0, p2=0):
    figura = figura.lower()
    if figura == "circulo":
        res = 3.1416 * (p1 ** 2)
        msg = f"Área del círculo con radio {p1}: {res:.2f}"
    elif figura == "cuadrado":
        res = p1 ** 2
        msg = f"Área del cuadrado con lado {p1}: {res:.2f}"
    elif figura == "triangulo":
        res = (p1 * p2) / 2
        msg = f"Área del triángulo con base {p1} y altura {p2}: {res:.2f}"
    else:
        msg = "Figura no válida (use: circulo, cuadrado, triangulo)"
    return f"<h1>{msg}</h1><hr>"

if __name__ == '__main__':
    app.run(debug=True)