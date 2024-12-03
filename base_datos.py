import sqlite3

DB_NAME = "gestor_tareas.db"

def inicializar_db():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    # Crear la tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            descripcion TEXT,
            prioridad TEXT,
            repetir BOOLEAN,
            estado TEXT DEFAULT 'pendiente',
            notificado BOOLEAN DEFAULT 0,
            completada BOOLEAN DEFAULT 0
        )
    """)

    cursor.execute("""
        PRAGMA table_info(tareas);
    """)
    columnas = [col[1] for col in cursor.fetchall()]
    
    if 'notificado' not in columnas:
        cursor.execute("""
            ALTER TABLE tareas ADD COLUMN notificado INTEGER DEFAULT 0
        """)

    if 'completada' not in columnas:
        cursor.execute("""
            ALTER TABLE tareas ADD COLUMN completada INTEGER DEFAULT 0
        """)
    
    conexion.commit()
    conexion.close()



def agregar_tarea(titulo, fecha, hora, descripcion, prioridad, repetir):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO tareas (titulo, fecha, hora, descripcion, prioridad, repetir)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, fecha, hora, descripcion, prioridad, repetir))
    conexion.commit()
    conexion.close()

def agregar_columna_notificado():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()

    
    cursor.execute("PRAGMA table_info(tareas);")
    columnas = [col[1] for col in cursor.fetchall()]

    # Verifica si la columna notificado exste
    if 'notificado' not in columnas:
        cursor.execute("""
            ALTER TABLE tareas ADD COLUMN notificado INTEGER DEFAULT 0
        """)
    
    # Verificar si la columna 'completada' ya existe
    if 'completada' not in columnas:
        cursor.execute("""
            ALTER TABLE tareas ADD COLUMN completada INTEGER DEFAULT 0
        """)

    conexion.commit()
    conexion.close()

def obtener_tareas(estado="pendiente"):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, titulo, fecha, hora, descripcion, prioridad FROM tareas WHERE estado = ?", (estado,))
    tareas = cursor.fetchall()
    conexion.close()
    return tareas

def actualizar_estado_tarea(id_tarea, nuevo_estado):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("UPDATE tareas SET estado = ? WHERE id = ?", (nuevo_estado, id_tarea))
    conexion.commit()
    conexion.close()

def eliminar_tarea(id_tarea):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
    conexion.commit()
    conexion.close()

# Obtener tareas pendientes
def obtener_tareas_pendientes():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT titulo, fecha, hora, notificado
        FROM tareas
        WHERE completada = 0 AND notificado = 0
    """)
    tareas = cursor.fetchall()
    conexion.close()
    return tareas


def marcar_notificada(titulo):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE tareas
        SET notificado = 1
        WHERE titulo = ?
    """, (titulo,))
    conexion.commit()
    conexion.close()



if __name__ == "__main__":
    agregar_columna_notificado()
