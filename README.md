# MINIBLOG DE BULFON, Y QUEVEDO
![Kirby is here](https://i.pinimg.com/564x/3f/78/fd/3f78fd0cd0e8b2ee0b10eeaca003af96.jpg)

Un miniblog que permite a los usuarios crear y compartir sus propios posteos.

## Requisitos

- Python (versión 3.11)
- Flask (versión 2.3)
- Flask-Migrate (versión 4.0)
- Tailwind CSS (instalado con Node.js)

## Configuración

1. Clona este repositorio: `git clone git@github.com:quevedoagostina/AGOS_MiniBlog.git`
2. Ve al directorio del proyecto: `cd AGOS_MiniBlog`
3. Luego de crear tu propio entorno virtual, actívalo: `source tu_entorno/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Crea las migraciones iniciales: `flask db init`
6. Después de realizar tus cambios ejecuta: `flask db migrate -m "..."`
7. Si es necesario, cambia la ruta de la base de datos en tu app.py
8. Ejecuta las migraciones de la base de datos: `flask db upgrade`
9. Vas a tener que cambiar la ruta del "tailwind.config.js" así ubicas la carpeta de tus templates correctamente.
10. Inicia la aplicación: `flask run`

## Uso

Clona el repositorio de GitHub en tu máquina local, crea un entorno virtual para el proyecto e instala las dependencias, también se deben ejecutar las migraciones para la base de datos. Asegúrate de tener Node.js instalado en tu sistema. Si aún no lo tienes, descárgalo e instálalo desde https://nodejs.org/. Instala las dependencias de Node.js para Tailwind CSS e inicia la aplicación.

## Aclaración importante

Hay un init_db.py para meter las categorías en la base de datos, para agregarlas ejecuta el script init_db.py. Desde el cmd, con el siguiente comando: "python init_db.py".

Este readme.md cambialo, al final las migraciones ya estan subidas a github entonces no es necesario que se suba el init_db.py pero bueno que sea como una aclaracion por si borran la carpeta migrations y ya no es solo blog de AGos, ahora es el blog de Bulfon, Quevedo, y Agos.

