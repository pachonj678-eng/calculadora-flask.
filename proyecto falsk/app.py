from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='gestor_contrasena',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/', methods=['GET'])
def inicio():
    return "¡Bienvenido al backend de tu gestor de contraseñas ADSO!"

@app.route('/api/baul', methods=['GET'])
def obtener_registros():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM baul")
            resultado = cursor.fetchall()
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/api/baul', methods=['POST'])
def agregar_registro():
    data = request.get_json()
    plataforma = data.get('Plataforma')
    usuario = data.get('usuario')
    clave = data.get('clave')

    if not plataforma or not usuario or not clave:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO baul (Plataforma, usuario, clave) VALUES (%s, %s, %s)"
            cursor.execute(sql, (plataforma, usuario, clave))
        connection.commit()
        return jsonify({"mensaje": "¡Credencial guardada con éxito!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)