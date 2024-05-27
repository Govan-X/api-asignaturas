from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)

#conexion = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_asignaturas'
mysql = MySQL(app)

#SETTINGS
app.secret_key= 'sadas15456s4d56asdasdsadsa'

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM asignaturas")
    data = cursor.fetchall()
    print(data)
    return render_template('index.html', asignaturas = data)

#METODO POST
@app.route('/add_asignatura', methods=['POST'])
def add_asignatura():
    if request.method == 'POST':
        claveAsignatura = request.form['claveAsignatura']
        nombreAsignatura = request.form['nombreAsignatura']
        grupo = request.form['grupo']
        profesor = request.form['profesor']
        salon = request.form['salon']
        dia = request.form['dia']
        hora = request.form['hora']
        lugaresDisponibles = request.form['lugaresDisponibles']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO asignaturas (claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles))
        mysql.connection.commit()
        print(claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles)
        flash('Asignatura agregada correctamente')    
        return redirect(url_for('index'))

#METODO GET
@app.route('/edit/<id>')
def get_asignatura(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM asignaturas WHERE id = %s",(id))
    data = cursor.fetchall()
    return render_template('edit_asignatura.html', asignatura = data[0])

#METODO POST
@app.route('/update/<id>', methods=['POST'])
def update_asignatura(id):
    if request.method == 'POST':
        claveAsignatura = request.form['claveAsignatura']
        nombreAsignatura = request.form['nombreAsignatura']
        grupo = request.form['grupo']
        profesor = request.form['profesor']
        salon = request.form['salon']
        dia = request.form['dia']
        hora = request.form['hora']
        lugaresDisponibles = request.form['lugaresDisponibles']
        cursor = mysql.connection.cursor()
        cursor.execute(""" 
                UPDATE asignaturas
                SET claveAsignatura = %s, nombreAsignatura = %s, grupo = %s, profesor = %s, salon = %s, dia = %s, hora = %s, lugaresDisponibles = %s WHERE id = %s
                    """, (claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles, id))
        flash('Asignatura actualizada correctamente')
        return redirect(url_for('index'))

#METODO DELETE
@app.route('/delete/<string:id>')
def delete_asignatura(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM asignaturas WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash('Asignatura eliminada correctamente')
    return redirect(url_for('index'))

#Pagina no encontrada
def pagina_no_encontrada(error):
    return "<h1>Lo sentimos, esta página no existe... :(</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()