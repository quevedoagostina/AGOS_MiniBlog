# Nombre del Proyecto

Un miniblog que permite a los usuarios crear y compartir sus propios posteos. 

## Requisitos

- Python (versión 3.11)
- Flask (versión 2.3)
- Flask-Migrate (versión 4.0)
- Tailwind CSS (instalado con Node.js)

## Configuración

1. Clona este repositorio: `git clone git@github.com:quevedoagostina/AGOS_MiniBlog.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Configura las variables de entorno en el archivo `.env`
4. Ejecuta las migraciones de la base de datos: `flask db upgrade`
5. Inicia la aplicación: `flask run`

## Uso

Clona el repositorio de GitHub en tu máquina local, crea un entorno virtual para el proyecto e instala las dependencias, también se deben ejecutar las migraciones para la base de datos. Asegúrate de tener Node.js instalado en tu sistema. Si aún no lo tienes, descárgalo e instálalo desde https://nodejs.org/. Instala las dependencias de Node.js para Tailwind CSS e inicia la aplicación.

## Aclaración importante

Hay un init_db.py para meter las categorías en la base de datos, para agregarlas ejecuta el script init_db.py. Desde el cmd, con el siguiente comando: "python init_db.py".
