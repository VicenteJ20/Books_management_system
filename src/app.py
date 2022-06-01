from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect

#models
from Models.ModelUser import ModelUser

#entities
from Models.Entities.User import User
import crud_admin

app = Flask(__name__)
database = MySQL(app)
login_manager_app = LoginManager(app)
csrf = CSRFProtect()

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_rut(database, id)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(request.form['rut'], request.form['password'])
        logged_user = ModelUser.login(database, user)
        
        if logged_user != None:
            login_user(logged_user)
            if logged_user.password:
                if logged_user.id == '20509776-7':
                    return redirect(url_for('admin_panel'))
                else:
                    return redirect(url_for('home'))
            else:
                flash('Contraseña inválida')
                return render_template('auth/login.html')
        else:
            flash('Usuario no encontrado')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin_panel')
@login_required
def admin_panel():
    return render_template('admin/admin_panel.html')

@app.route('/add_librarian')
@login_required
def add_librarian():
    return render_template('admin/add_librarian.html')

@app.route('/insert_librarian', methods=['POST'])
@login_required
def insert_librarian():
    rut = request.form['rut']
    password = request.form['password']
    username = request.form['username']
    fullname = request.form['fullname']
    email = request.form['email']
    creator_id = request.form['creator_id']

    crud_admin.add_librarian(rut, password, username, fullname, email, creator_id)

    return redirect('/admin_panel')


@app.route('/view_librarian')
@login_required
def view_librarian():
    librarians = crud_admin.view_librarians()
    return render_template('admin/view_librarian.html', librarians=librarians)

@app.route('/view_edit_librarians')
@login_required
def view_edit_librarian():
    librarians = crud_admin.view_librarians()
    return render_template('admin/view_edit_librarian.html', librarians=librarians)

@app.route('/edit_librarian/<id>')
def edit_librarian(id):
    librarian = crud_admin.get_librarian(id)
    return render_template('admin/edit_librarian.html', librarian=librarian)


@app.route('/update_librarian', methods=['POST'])
def update_librarian():
    rut = request.form['rut']
    password = request.form['password']
    username = request.form['username']
    fullname = request.form['fullname']
    email = request.form['email']
    creator_id = request.form['creator_id']

    crud_admin.update_librarian(rut, password, username, fullname, email, creator_id)
    return redirect('/admin_panel')

@app.route('/view_delete_librarians')
@login_required
def view_delete_librarian():
    librarians = crud_admin.view_librarians()
    return render_template('admin/view_delete_librarians.html', librarians=librarians)

@app.route('/delete_librarian', methods=['POST'])
@login_required
def delete_librarian():
    crud_admin.delete_librarian(request.form['id'])
    return redirect('/admin_panel')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')


#common errors
def status_401(err):
    return redirect(url_for('login'))

def status_404(err):
    return '<h1> Página no encontrada </h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()