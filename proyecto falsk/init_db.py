import pymysql

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS gestor_contrasena;")
        cursor.execute("USE gestor_contrasena;")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `baul` (
              `id_baul` INT NOT NULL AUTO_INCREMENT,
              `Plataforma` VARCHAR(80) NOT NULL,
              `usuario` VARCHAR(80) NOT NULL,
              `clave` VARCHAR(80) NOT NULL,
              PRIMARY KEY (`id_baul`),
              UNIQUE KEY `Plataforma` (`Plataforma`, `usuario`)
            );
        """)
    connection.commit()
    print("¡Base de datos y tabla creadas con éxito!")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()