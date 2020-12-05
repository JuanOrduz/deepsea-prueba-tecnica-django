# DeepSea prueba tecnica Django backend
El presente repositorio contiene la solución a la prueba técnica de Deepsea development para desarrollador backend django. Los requerimientos son los siguientes:

### Descripción
Se quiere realizar una herramienta para organizar los equipos de trabajo de una empresa. Para esto se quiere crear un modelo de ‘Equipo’ el cual agrupa múltiples Usuarios y tiene un nombre y una imagen. Un usuario puede ser parte de múltiples equipos. La herramienta tendrá un frontend aparte,
por lo tanto se quiere realizar un API que ofrezca un CRUD sobre el modelo de Equipo. También se quiere poder administrar los equipos y los usuarios por medio del administrador de Django. Los administradores de la herramienta quieren recibir un correo electrónico cada vez que se crea un nuevo Equipo. Se debe también almacenar la fecha en la que un usuario se unió a un equipo.

### Requerimientos
1. Usar Django Rest Framework para ofrecer los endpoints de un CRUD sobre el modelo de Equipo.
2. Reemplazar el modelo de Usuario que usa Django por defecto por uno propio.
3. Poder asignar todos los miembros del equipo en los endpoints de Create y Update enviando un arreglo con los IDs de los usuarios en el request.
4. Administrar los modelos de Usuario y Equipo por medio del administrador de Django.
5. Utilizar Inlines en el administrador del modelo de Usuario.
6. Recibir un correo electrónico cuando se crea un Equipo. Poder ver, crear y actualizar la
imagen del Equipo usando base64.
7. Almacenar la fecha en la que un usuario se unió a un equipo.

### Bonus
* Crear dockerfile para generar una imagen de Docker con el proyecto.
* Realizar el envío de correo de manera asíncrona.
* Cada 5 minutos validar que el número de equipos no exceda de 10 usuarios. Si es así enviar correo de alerta.

## Solucion
El backend se diseño con las siguientes caracteristicas:
* Modelo de usuarios personalizados basado en modelo por defecto de Django, utiliza el email como usuario y tiene un campo adicional para el numero de identificacion.
* Enpoints configurados con DRF para listar Usuarios y CRUD de equipos ([postman](https://documenter.getpostman.com/view/13751212/TVmQcavg))
* Para enviar emails se utilizo la libreria "django.core.mail"
* Las tareas asincronas y periodicas se manejaron con celery y redis

El codigo del backend se encuentra en la carpeta src, para desplegarlo se siguen los siguientes pasos:
* Clonar el repositorio, crear virtualenv e instalar paquetes:

```
git clone git@github.com:JuanOrduz/deepsea-prueba-tecnica-django.git
cd deepsea-prueba-tecnica-django/
python -m virtualenv env
source env/bin/activate
cd src/
pip install -r requirements.txt
```
* A continuacion se realiza la migracion de las bases de datos y se crea un superusuario
```
python manage.py migrate
python manage.py createsuperuser
```
* Para el envio de emails se tiene configurado utilizar un correo de gmail, cuyo usuario y contraseña se lee de variables de entorno por seguridad
```
export EMAIL_HOST_USER=[correo electronico de gmail]
export EMAIL_HOST_PASSWORD=[contraseña del correo electronico]
```
* Se inicia el servidor
```
python manage.py runserver
```
Para activar la funcionalidad de tareas asincronas se requiere **redis** instalado y desplegado en el equipo, para comprobar que esta configurado correctamente se tiene como respuesta *PONG* al utilizar el siguiente comando:
```
redis-cli ping
PONG
```
Para configurar las tareas asincronas se necesita desplegar un *celery worker* y *celery beat*, para esto se abren dos terminales adicionales que se denominaran terminal 2 y terminal 3
#### Terminal 2 (celery worker)
Se activa el *virtualenv*, configuran variables de entorno y despliega *celery worker*
```
source ../env/bin/activate
export EMAIL_HOST_USER=[correo electronico de gmail]
export EMAIL_HOST_PASSWORD=[contraseña del correo electronico]
celery -A deepsea worker -l info
```
#### Terminal 3 (celery beat)
Se activa el *virtualenv*, configuran variables de entorno y despliega *celery beat*
```
source ../env/bin/activate
export EMAIL_HOST_USER=[correo electronico de gmail]
export EMAIL_HOST_PASSWORD=[contraseña del correo electronico]
celery -A deepsea beat -l debug
```

## Creacion imagen docker
Pare crear una imagen docker de este repositorio se utiliza el respectivo docker file, para desplegar el servidor, *celery worker* y *celery beat* se utiliza la misma imagen y solo se modifica el comando utilizado para desplegarlo. Partiendo de la ruta base de este repositorio se genera la imagen docker de la siguiente manera:
```
cd src/
docker build -t [Usuario]/[Nombre imagen]:[Tag] .
```
