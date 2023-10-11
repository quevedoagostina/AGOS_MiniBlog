# import datetime
# from flask import redirect, request, session, flash, url_for
# from flask_marshmallow import Marshmallow
# from app import app, db
# from models import Entrada

# ma = Marshmallow()

# class EntradasSchema(ma.ModelSchema):
#     class Meta:
#         model = Entrada
#         fields = ('titulo', 'contenido', 'categoria_id')

# post_schema = EntradasSchema()

# @app.post('/crear_posteo', content_type='application/json')
# def crear_posteo():
#     if 'user_id' not in session:
#         # Si el usuario no ha iniciado sesión, redirigir a inicio de sesión
#         flash('Inicia sesión para crear un posteo.', 'info')
#         return redirect(url_for('login'))

#     data = request.json

#     nueva_entrada = Entrada(
#         titulo=data['titulo'],
#         contenido=data['contenido'],
#         fecha_creacion=datetime.now(),
#         autor_id=session['user_id'],
#         categoria_id=data['categoria_id']
#     )

#     db.session.add(nueva_entrada)

#     db.session.commit()

#     flash('Posteo creado exitosamente.', 'success')
#     return redirect(url_for('posteos'))

