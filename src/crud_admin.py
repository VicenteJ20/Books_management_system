from flask import flash
import pymysql

def get_connection():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        db = 'loan_books_management'
    )

def add_librarian(rut, password, username, fullname, email, creator_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Bibliotecario (rut, password, username, full_name, email, creator_id) VALUES (%s, %s, %s, %s, %s, %s)", (rut, password, username, fullname, email, creator_id))
            connection.commit()
        except connection.Error as err:
            if '1062' in str(err):
                flash(f'ERROR, el RUT: {rut} ya se encuentra en REGISTRADO')
            else:
                flash(f'Lo sentimos, ha ocurrido un error inesperado, contacte con el administrador por favor. {str(err)}')
        connection.close()

def view_librarians():
    connection = get_connection()
    librarians = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Bibliotecario")
        librarians = cursor.fetchall()
        connection.close()
        return librarians

def delete_librarian(id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Bibliotecario WHERE rut = %s", (id))
        connection.commit()
        connection.close()

def get_librarian(id):
    connection = get_connection()
    librarian = None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Bibliotecario WHERE rut = %s", (id))
        librarian = cursor.fetchone()
        connection.commit()
        connection.close()
        return librarian

def update_librarian(rut, password, username, fullname, email, creator_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Bibliotecario SET password = %s, username = %s, full_name = %s, email = %s, creator_id = %s WHERE rut = %s", (password, username, fullname, email, creator_id, rut))
        connection.commit()
        connection.close()