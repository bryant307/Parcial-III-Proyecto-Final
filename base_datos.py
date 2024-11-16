import sqlite3

def conectar():
    conexion = sqlite3.connect('tareas.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT NOT NULL,
                        descripcion TEXT,
                        fecha_limite TEXT,
                        completada INTEGER DEFAULT 0
                    )''')
    conexion.commit()
    return conexion, cursor