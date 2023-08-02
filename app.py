from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/miniblog'
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Usuario, Entrada, Comentario, Categoria

@app.context_processor
def categorias_disponibles():
    categorias = Categoria.query.all()
    return dict(categorias=categorias)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posteos')
def posteos():
    posts = Entrada.query.all()
    return render_template('posteos.html', posts=posts)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica si el nombre de usuario ya existe en la base de datos
        usuario_existente = Usuario.query.filter_by(username=username).first()
        if usuario_existente:
            flash('El nombre de usuario ya está en uso. Por favor, elige otro.', 'error')
        else:
            # Crea un nuevo usuario con las credenciales ingresadas
            nuevo_usuario = Usuario(username=username, password=password)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Registro exitoso. Inicia sesión con tus nuevas credenciales.', 'success')
            return redirect(url_for('login'))

    return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar si el usuario existe y la contraseña es válida
        usuario = Usuario.query.filter_by(username=username, password=password).first()
        if usuario is not None:
            session['user_id'] = usuario.id
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('crear_posteo'))  # Redirigir a la página de creación de posteos
        else:
            flash('Credenciales inválidas. Inténtalo de nuevo.', 'error')  # Mensaje de error en caso de credenciales inválidas

    return render_template('login.html')


@app.route('/crear_posteo', methods=['GET', 'POST'])
def crear_posteo():
    if 'user_id' not in session:
        # Si el usuario no ha iniciado sesión, redirigir a inicio de sesión
        flash('Inicia sesión para crear un posteo.', 'info')
        return redirect(url_for('login'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        categoria_id = int(request.form['categoria'])

        nueva_entrada = Entrada(
            titulo=titulo,
            contenido=contenido,
            fecha_creacion=datetime.now(),
            autor_id=session['user_id'],
            categoria_id=categoria_id
        )

        db.session.add(nueva_entrada)

        db.session.commit()

        flash('Posteo creado exitosamente.', 'success')
        return redirect(url_for('posteos'))

    categorias = Categoria.query.all()
    return render_template('crear_posteo.html', categorias=categorias)


@app.route('/post/<int:post_id>')
def ver_post(post_id):
    post = Entrada.query.get(post_id)
    print(post)  
    return render_template('ver_post.html', post=post)

@app.route('/post/<int:post_id>/comentar', methods=['POST'])
def comentar(post_id):
    if 'user_id' not in session:
        flash('Inicia sesión para comentar.', 'info')
        return redirect(url_for('login'))

    texto_comentario = request.form['comentario']
    autor_id = session['user_id'] 

    nuevo_comentario = Comentario(texto=texto_comentario, fecha_creacion=datetime.now(),
                                  autor_id=autor_id, entrada_id=post_id)
    db.session.add(nuevo_comentario)
    db.session.commit()
    return redirect(url_for('ver_post', post_id=post_id))

@app.route('/logout')
def logout_view():
    if 'user_id' in session:
        del session['user_id']
        flash('Has cerrado sesión', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

