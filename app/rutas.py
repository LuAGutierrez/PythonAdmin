from flask import render_template, redirect, url_for, request, flash, current_app
from app.modelo import *

@current_app.route('/')
def index():
    return redirect(url_for('tickets'))


@current_app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        titulo = request.form['titulo']
        empresa = request.form['nombre_empresa']
        nombre = request.form['usuario']
        producto = request.form['producto']        
        problema = request.form['problema']
        prioridad = request.form['prioridad']
        descripcion = request.form['descripcion']

        insertar_datos_ticket(current_app.mysql,nombre, empresa, prioridad , descripcion, producto, problema,titulo)
        
        flash('Ticket creado con exito')
        return redirect(url_for('tickets'))
    
    estado = request.args.get('estado')
    tickets = obtener_tickets(current_app.mysql,estado)

    return render_template('/tickets.html', tickets=tickets)


@current_app.route('/tareas', methods=['GET', 'POST'])
def tareas():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        responsable = request.form['responsable']
        afectado = request.form['afectado']

        insertar_datos_tarea(current_app.mysql,titulo,descripcion,responsable,afectado)

        return redirect(url_for('tareas'))
    
    estado = request.args.get('estado')
    tareas = obtener_tareas(current_app.mysql,estado)


    return render_template('/tareas.html',tareas = tareas)

@current_app.route('/ticket/<int:id_ticket>', methods=['POST'])
def cambiar_estado(id_ticket):

    cambiar_estado_ticket(current_app.mysql,id_ticket) 

    return redirect(url_for('tickets'))

@current_app.route('/tareas/<int:id_tarea>', methods=['POST'])
def cambiar_estado_tarea(id_tarea):
    
    cambiar_estado_tareas(current_app.mysql,id_tarea)

    return redirect(url_for('tareas'))