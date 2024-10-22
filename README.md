# API de Productos - Proyecto Django

Este es un proyecto sencillo desarrollado en Django que implementa una API RESTful para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un JSON de productos. El proyecto utiliza Docker para facilitar la configuración y el despliegue.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- Docker
- Docker Compose

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local usando Docker.

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local usando git:

``bash
git clone https://github.com/usuario/nombre-del-proyecto.git
cd nombre-del-proyecto
### 2. Crear y configurar el archivo .env
Copia el archivo .env.example a .env para configurar las variables de entorno:

``bash
Copiar código
cp .env.example .env
Luego, edita el archivo .env si es necesario para configurar variables como SECRET_KEY y DEBUG.

### 3. Construir y levantar los contenedores
Usa Docker Compose para construir las imágenes del proyecto y levantar los contenedores:

``bash
Copiar código
docker-compose up --build
Esto descargará las imágenes necesarias, instalará las dependencias y levantará la aplicación junto con los servicios definidos en docker-compose.yml.

### 4. Migrar la base de datos
Ejecuta las migraciones necesarias dentro del contenedor para configurar las tablas iniciales:

``bash
Copiar código
docker-compose exec web python manage.py migrate
### 5. Crear un superusuario (opcional)
Si deseas acceder al panel de administración de Django, puedes crear un superusuario:

``bash
Copiar código
docker-compose exec web python manage.py createsuperuser
### 6. Acceder a la aplicación
Una vez que los contenedores estén en ejecución, puedes acceder a la aplicación en http://localhost:8000/.

## Uso de la API
La API permite realizar operaciones CRUD sobre los productos. A continuación se describen las rutas principales y los métodos HTTP soportados.

## Obtener todos los productos
URL: /api/products/
Método HTTP: GET
Descripción: Devuelve un listado de todos los productos.
## Obtener un producto por ID
URL: /api/products/<id>/
Método HTTP: GET
Descripción: Devuelve los detalles de un producto específico.
## Crear un nuevo producto
URL: /api/products/
Método HTTP: POST
Descripción: Crea un nuevo producto a partir de un JSON enviado en el cuerpo de la solicitud.
## Ejemplo de cuerpo de solicitud:
json
Copiar código
{
  "name": "Producto Ejemplo",
  "description": "Descripción del producto",
  "price": 19.99
}
## Actualizar un producto existente
URL: /api/products/<id>/
Método HTTP: PUT
Descripción: Actualiza los detalles de un producto existente.
Ejemplo de cuerpo de solicitud:
json
Copiar código
{
  "name": "Producto Actualizado",
  "description": "Nueva descripción del producto",
  "price": 29.99
}
## Eliminar un producto
URL: /api/products/<id>/
Método HTTP: DELETE
Descripción: Elimina un producto específico por su ID.
Dependencias
El proyecto utiliza las siguientes dependencias:

txt
Copiar código
asgiref==3.8.1
Django==5.1.2
django-cors-headers==4.5.0
djangorestframework==3.15.2
sqlparse==0.5.1
tzdata==2024.2
Estas dependencias están instaladas automáticamente al usar Docker y están listadas en el archivo requirements.txt.

## Docker
Este proyecto usa Docker para ejecutar los servicios necesarios. A continuación se muestra el contenido básico del archivo docker-compose.yml:

yaml
Copiar código
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
      - SECRET_KEY=supersecretkey
      - ALLOWED_HOSTS=localhost
    depends_on:
      - db

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=nombre_del_proyecto
      - POSTGRES_USER=usuario
      - POSTGRES_PASSWORD=contraseña

volumes:
  postgres_data:
## Comandos útiles de Docker
Levantar los contenedores:

``bash
docker-compose up
Detener los contenedores:

``bash
docker-compose down
Reconstruir la imagen:

``bash
docker-compose up --build
Acceder al contenedor web:

``bash
docker-compose exec web bash
## Pruebas
Para ejecutar las pruebas dentro del contenedor, usa el siguiente comando:

``bash
docker-compose exec web python manage.py test
## Despliegue en Producción
Para desplegar este proyecto en un entorno de producción:

Asegúrate de establecer DEBUG=False en el archivo .env o en la configuración de Docker.
Configura los valores de ALLOWED_HOSTS.
Considera usar un servidor web como Nginx para servir la aplicación en un entorno de producción.
Utiliza un sistema de backend como Gunicorn o uWSGI para ejecutar la aplicación.
## Contribución
Si deseas contribuir a este proyecto, sigue estas pautas:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y commitea (git commit -am 'Agregada nueva funcionalidad').
Empuja tu rama (git push origin feature/nueva-funcionalidad).
Crea un Pull Request.
## Licencia
Este proyecto está bajo la licencia [Nombre de la Licencia]. Consulta el archivo LICENSE para más detalles.

Este archivo `README.md` cubre el uso de Docker para el despliegue, las dependencias del proyecto, y el manejo de la API CRUD con productos. También incluye instrucciones sobre cómo clonar, configurar, y ejecutar el proyecto. Puedes ajustarlo según tus necesidades específicas.
