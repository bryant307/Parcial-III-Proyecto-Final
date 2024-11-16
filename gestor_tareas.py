from base_datos import conectar

def agregar_tareas(titulo, descripcion, fecha_limite):
    conexion, cursor = conectar()
    cursor.execute("INSERT INTO tareas (titulo, descripcion, fecha_limite) VALUES (?, ?, ?)",
                   (titulo, descripcion, fecha_limite))
    conexion.commit()
    conexion.close()