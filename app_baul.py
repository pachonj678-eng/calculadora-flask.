from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
import bcrypt
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='',  # Pon aquí tu contraseña de MySQL si tienes una
        db='gestor_contrasena',
        charset='utf8mb4'
    )

@app.route("/", methods=['GET'])
def consulta_general():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id_baul, plataforma, usuario, clave FROM baul")
        datos = cur.fetchall()
        cur.close()
        conn.close()

        data = [{'id_baul': row[0], 'plataforma': row[1], 'usuario': row[2], 'clave': row[3]} for row in datos]
        return jsonify({'baul': data, 'mensaje': 'Baúl de contraseñas'})
    except Exception as ex:
        return jsonify({'mensaje': f'Error: {str(ex)}'}), 500

@app.route("/registro/", methods=['POST'])
def registro():
    try:
        data = request.get_json()
        plataforma = data['plataforma']
        usuario = data['usuario']
        # Encriptamos la contraseña con bcrypt antes de guardarla
        clave = bcrypt.hashpw(data['clave'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO baul (plataforma, usuario, clave) VALUES (%s, %s, %s)", (plataforma, usuario, clave))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'mensaje': 'Registro agregado con éxito'}), 201
    except Exception as ex:
        return jsonify({'mensaje': f'Error: {str(ex)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Usamos el puerto 5001 para que no choque con el anterior