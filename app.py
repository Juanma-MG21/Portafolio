from flask import Flask, flash, redirect, url_for, render_template, request, session, jsonify
import sqlite3
import os 

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configuración de la ruta de la base de datos
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

def inicializar_db():
    """Crea la tabla automáticamente si no existe al iniciar la app"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            ID_messages INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Email TEXT NOT NULL,
            Mensaje TEXT NOT NULL,
            Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexion.commit()
    conexion.close()

def conectar_db():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row 
    return conexion

# Llamamos a la creación de la tabla antes de cualquier ruta
inicializar_db()

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
            flash('Todos los campos son obligatorios.', 'danger')
            return redirect(url_for('index', _anchor='contact'))

        conexion = conectar_db()
        cursor = conexion.cursor()

        try:
            query = "INSERT INTO messages (Nombre, Email, Mensaje) VALUES (?, ?, ?)"
            cursor.execute(query, (nombre, email, mensaje))
            conexion.commit()
            flash('¡Mensaje enviado con éxito!', 'success')
        except Exception as e:
            flash('Hubo un error al procesar tu solicitud: ' + str(e), 'danger')
        finally:
            cursor.close()
            conexion.close()

    return redirect(url_for('index', _anchor='contact'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
