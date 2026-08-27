import math as mt
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Suma
@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma(numero1=0, numero2=0):
    return jsonify({"Resultado": numero1 + numero2, "Operacion": "suma"})

# Resta
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0, numero2=0):
    return jsonify({"Resultado": numero1 - numero2, "Operacion": "resta"})

# Multiplicación
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
def multiplicacion(numero1=0, numero2=0):
    return jsonify({"Resultado": numero1 * numero2, "Operacion": "multiplicación"})

# División
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<float:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
def division(numero1=0, numero2=0):
    return jsonify({"Resultado": numero1 / numero2, "Operacion": "División"})

# Potenciación
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0, numero2=0):
    return jsonify({"Resultado": numero1 ** numero2, "Operacion": "potenciación"})

# Seno
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    return jsonify({"Resultado": mt.sin(numero1), "Operacion": "seno"})

# Coseno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    return jsonify({"Resultado": mt.cos(numero1), "Operacion": "coseno"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
