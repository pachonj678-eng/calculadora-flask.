from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# Configuración de SQLAlchemy para conectar con tu base de datos (ej: MySQL/MariaDB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/gestor_contrasena'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del Modelo (Tabla usando el ORM)
class Registro(db.Model):
    __tablename__ = 'registros_orm'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'valor': self.valor
        }

# Crear las tablas automáticamente al iniciar
with app.app_context():
    db.create_all()

# Rutas con documentación Swagger integrada
@app.route('/registros', methods=['GET'])
def obtener_registros():
    """
    Obtener todos los registros usando SQLAlchemy
    ---
    responses:
      200:
        description: Lista de registros obtenida con éxito
    """
    registros = Registro.query.all()
    return jsonify([r.to_dict() for r in registros]), 200

@app.route('/registros', methods=['POST'])
def crear_registro():
    """
    Crear un nuevo registro
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            valor:
              type: string
    responses:
      201:
        description: Registro creado exitosamente
    """
    data = request.get_json()
    nuevo = Registro(titulo=data.get('titulo'), valor=data.get('valor'))
    
    db.session.add(nuevo)
    db.session.commit()
    
    return jsonify({'mensaje': 'Guardado con éxito', 'id': nuevo.id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)