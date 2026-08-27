from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>Servidor Flask Activo</h1><hr>"

# 1. Promedio de Notas (30%, 30%, 40%)
@app.route("/notas/<float:n1>/<float:n2>/<float:n3>")
def notas(n1, n2, n3):
    definitiva = (n1 * 0.30) + (n2 * 0.30) + (n3 * 0.40)
    return f"<h1>Nota final: {definitiva:.2f}</h1><hr>"

# 2. Clasificación por Edad
@app.route("/edades/<int:edad>")
def edades(edad):
    if edad < 18:
        categoria = "Menor de edad"
    elif edad < 60:
        categoria = "Adulto"
    else:
        categoria = "Adulto mayor"
    return f"<h1>Categoría: {categoria}</h1><hr>"

# 3. Matriz Aleatoria con NumPy
@app.route("/matriz/<int:filas>/<int:columnas>")
def matriz(filas, columnas):
    datos = np.random.randint(1, 100, size=(filas, columnas))
    return jsonify({"filas": filas, "columnas": columnas, "matriz": datos.tolist()})

if __name__ == "__main__":
    app.run(debug=True, port=5000)