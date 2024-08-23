import mysql.connector

def obtener_tickets(mysql, estado=None):
    try:
        with mysql.cursor(dictionary=True) as cursor:

            consulta = "SELECT * FROM tickets"
            params = ()

            if estado:
                consulta += " WHERE estado = %s"
                params = (estado,)

            cursor.execute(consulta, params)    
            tickets = cursor.fetchall()
    except mysql.connector.Error as e:
        # Si hay algun error imprime cartel en consola, esto puede ser utilizado en el html
        print(f"Error al obtener datos: {e}")

    return tickets

# Obtengo las tareas para mostrarlas
def obtener_tareas(mysql,estado=None):
    try:
        with mysql.cursor(dictionary=True) as cursor:

            consulta = """SELECT * FROM tareas"""
            params = ()

            cursor.execute(consulta)
            tareas = cursor.fetchall()

    except mysql.connector.Error as e:
        # Si hay algun error imprime cartel en consola, esto puede ser utilizado en el html
        print(f"Error al obtener datos: {e}")
    return tareas

def insertar_datos_ticket(mysql, nombre, empresa, prioridad , descripcion, producto, problema,titulo):
    try:
        #El with hace que se cierre automaticamente al finalizar la consulta
        with mysql.cursor(dictionary=True) as cursor:

            #Asignamos la consulta SQL en la variable consulta
            consulta = """INSERT INTO tickets (usuario, empresa, prioridad, descripcion, producto,tipo_problema,titulo,estado) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, 'Pendiente')"""
            
            #Asignamos los parametros a la variable parametros
            params = (nombre, empresa, prioridad , descripcion, producto, problema,titulo)

            #Ejecutamos la consulta con los parametros correspondientes
            cursor.execute(consulta,params)

            # Commit guarda los cambios hechos en la base de datos
            mysql.commit()

    except mysql.connector.Error as e:
        # Si hay algun error imprime cartel en consola, esto puede ser utilizado en el html
        print(f"Error al insertar datos en tickets: {e}")

        # Revertir cualquier cambio en caso de error
        mysql.rollback()

# Cambio el estado de un ticket
def cambiar_estado_ticket(mysql,id_ticket):
    with mysql.cursor(dictionary=True) as cursor:
        # Paso 1: Obtener el estado actual del ticket
        consulta = "SELECT estado FROM tickets WHERE id_ticket = %s"
        params = (id_ticket,)
        
        cursor.execute(consulta, params)
        resultado = cursor.fetchone()
        
        if not resultado:
            return False  # El ticket no existe
        
        estado_actual = resultado['estado']

    # Paso 2: Determinar el nuevo estado
    nuevo_estado = 'Pendiente' if estado_actual == 'Resuelto' else 'Resuelto'

    with mysql.cursor(dictionary=True) as cursor:
        consulta = """UPDATE tickets SET estado = %s where ticket = %s"""
        params = (nuevo_estado,id_ticket)

        cursor.execute(consulta,params)
        mysql.commit()

        return cursor.rowcount > 0  # Devuelve True si se actualizó al menos una fila

# Cambio estado tareas
def cambiar_estado_tareas(mysql,id_tarea):
    with mysql.cursor(dictionary=True) as cursor:
        # Paso 1: Obtener el estado actual del ticket
        consulta = "SELECT estado FROM tareas WHERE id_tarea = %s"
        params = (id_tarea,)
        
        cursor.execute(consulta, params)
        resultado = cursor.fetchone()
        
        if not resultado:
            return False  # La tarea no existe
        
        estado_actual = resultado['estado']

    # Paso 2: Determinar el nuevo estado
    nuevo_estado = 'Pendiente' if estado_actual == 'Resuelto' else 'Resuelto'

    with mysql.cursor(dictionary=True) as cursor:
        consulta = """UPDATE tareas SET estado = %s where id_tarea = %s"""
        params = (nuevo_estado,id_tarea,)

        cursor.execute(consulta,params)
        mysql.commit()

        return cursor.rowcount > 0  # Devuelve True si se actualizó al menos una fila


# Inserto los datos de la tarea en la base de datos
def insertar_datos_tarea(mysql,titulo,descripcion,responsable,afectado):
    try:
        with mysql.cursor(dictionary=True) as cursor:

            consulta = """INSERT INTO tareas (titulo,descripcion,responsable,afectado,estado) VALUES (%s, %s, %s, %s, 'Pendiente')"""

            params = (titulo,descripcion,responsable,afectado)

            cursor.execute(consulta,params)
            
            mysql.commit()

    except mysql.connector.Error as e:
        # Si hay algun error imprime cartel en consola, esto puede ser utilizado en el html
        print(f"Error al insertar datos en tickets: {e}")

        # Revertir cualquier cambio en caso de error
        mysql.rollback()  