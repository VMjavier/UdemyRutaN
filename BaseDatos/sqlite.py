import sqlite3

#conexion
conexion = sqlite3.connect('clientes.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS datos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "nombres varchar(255), "+
    "apellidos varchar(255), "+
    "telefono int(255), " +
    "correo_electronico varchar(255)"+
    ")")

#Guardar cambios
conexion.commit()

#Cerrar conexión
conexion.close()