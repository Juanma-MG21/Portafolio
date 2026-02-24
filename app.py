from flask import Flask, flash, redirect, url_for, render_template, request, session, jsonify
import mysql.connector
import os 

app = Flask (__name__)

app.secret_key = 'clave_secreta'


import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'JuanMG',
    'password': 'Jmy*psd2027',
    'database': 'p0rtafolyo'
}

def conectar_db():
    return mysql.connector.connect(**db_config)


db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()


def get_db_connection():
    return mysql.connector.connect(**db_config)

# ===============================================================================

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
     
        nombre = request.form.get('name')
        email = request.form.get('email')
        mensaje = request.form.get('message')

       
        if not nombre or not email or not mensaje:
            flash('Todos los campos son obligatorios para enviar el mensaje.', 'danger')
            return redirect(url_for('index', _anchor='contact'))

        conexion = conectar_db()
        cursor = conexion.cursor()

        try:
     
            query = """
                INSERT INTO messages (Nombre, Email, Mensaje) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nombre, email, mensaje))
            conexion.commit()
            
            flash('¡Mensaje enviado con éxito!', 'success')
            return redirect(url_for('index', _anchor='contact'))

        except Exception as e:
            conexion.rollback()
            flash('Hubo un error al procesar tu solicitud: ' + str(e), 'danger')
        finally:
            cursor.close()
            conexion.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
