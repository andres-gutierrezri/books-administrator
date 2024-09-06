from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "secret_key"

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventario'

mysql = MySQL(app)

@app.route('/')
def libros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    cursor.close()
    return render_template('libros.html', libros=libros)

@app.route('/add', methods=['POST'])
def add_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        CodigodeBarras = request.form['CodigodeBarras']
        NoTopografico = request.form['NoTopografico']
        Titulo = request.form['Titulo']
        Autor = request.form['Autor']
        Ciudad = request.form['Ciudad']
        Editorial = request.form['Editorial']
        Fecha = request.form['Fecha']
        Edicion = request.form['Edicion']
        Pagsovols = request.form['Pagsovols']
        Ejemplares = request.form['Ejemplares']
        Genero = request.form['Genero']
        Ubicacion = request.form['Ubicacion']


        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO libros (isbn, CodigodeBarras, NoTopografico, Titulo, Autor, Ciudad, Editorial, Fecha, Edicion, Pagsovols, Ejemplares, Genero, Ubicacion) VALUES (%s, %s, %s, %s)", (isbn, CodigodeBarras, NoTopografico, Titulo, Autor, Ciudad, Editorial, Fecha, Edicion, Pagsovols, Ejemplares, Genero, Ubicacion))
        mysql.connection.commit()
        flash('Libro agregado exitosamente')
        return redirect(url_for('libros '))

@app.route('/edit/<ITEM>', methods=['GET', 'POST'])
def edit_book(ITEM):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros WHERE ITEM = %s", [ITEM])
    libro = cursor.fetchone()
    cursor.close()
    if request.method == 'POST':
        isbn = request.form['isbn']
        CodigodeBarras = request.form['CodigodeBarras']
        NoTopografico = request.form['NoTopografico']
        Titulo = request.form['Titulo']
        Autor = request.form['Autor']
        Ciudad = request.form['Ciudad']
        Editorial = request.form['Editorial']
        Fecha = request.form['Fecha']
        Edicion = request.form['Edicion']
        Pagsovols = request.form['Pagsovols']
        Ejemplares = request.form['Ejemplares']
        Genero = request.form['Genero']
        Ubicacion = request.form['Ubicacion']


        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE libros
            SET isbn = %s, CodigodeBarras = %s, NoTopografico= %s, Titulo= %s, Autor= %s, Ciudad= %s, Editorial= %s, Fecha= %s, Edicion= %s, Pagsovols= %s, Ejemplares= %s, Genero= %s, Ubicacion= %s
            WHERE ITEM = %s
        """, (isbn, CodigodeBarras, NoTopografico, Titulo, Autor, Ciudad, Editorial, Fecha, Edicion, Pagsovols, Ejemplares, Genero, Ubicacion, ITEM))
        mysql.connection.commit()
        flash('Libro actualizado exitosamente')
        return redirect(url_for('libros'))

    return render_template('edit.html', libro=libro)

@app.route('/delete/<ITEM>', methods=['GET'])
def delete_book(ITEM):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM libros WHERE ITEM = %s", [ITEM])
    mysql.connection.commit()
    flash('Libro eliminado exitosamente')
    return redirect(url_for('libros'))

if __name__ == '__main__':
    app.run(debug=True)
