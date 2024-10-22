# API de Productos - Proyecto Django

Este es un proyecto desarrollado en Django que implementa una API RESTful para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un conjunto de productos. El proyecto está configurado para ejecutarse utilizando Docker Compose para facilitar la configuración y el despliegue.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- Docker
- Docker Compose

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local usando git:

```
git clone https://github.com/nsrc008/BackProductsDj.git
cd nombre-del-proyecto
```

### 2. Crear y configurar el archivo .env

Copia el archivo .env.example a .env para configurar las variables de entorno:

```
cp .env.example .env
```

Luego, edita el archivo .env si es necesario para configurar variables como `SECRET_KEY`, `DEBUG`, y `ALLOWED_HOSTS`.

### 3. Construir y levantar los contenedores

Usa Docker Compose para construir las imágenes del proyecto y levantar los contenedores:

```
docker-compose up --build
```

Esto descargará las imágenes necesarias, instalará las dependencias, y levantará la aplicación junto con la base de datos PostgreSQL definida en `docker-compose.yml`.

### 4. Migrar la base de datos

Ejecuta las migraciones necesarias dentro del contenedor para configurar las tablas iniciales:

```
docker-compose exec web python manage.py migrate
```

### 5. Crear un superusuario (opcional)

Si deseas acceder al panel de administración de Django, puedes crear un superusuario:

```
docker-compose exec web python manage.py createsuperuser
```

### 6. Acceder a la aplicación

Una vez que los contenedores estén en ejecución, puedes acceder a la aplicación en `http://localhost:8000/`.

## Uso de la API

La API permite realizar operaciones CRUD sobre los productos. A continuación se describen las rutas principales y los métodos HTTP soportados.

## Obtener todos los productos

- URL: /api/products/
- Método HTTP: GET
- Descripción: Devuelve un listado de todos los productos.

## Obtener un producto por ID

- URL: /api/products/<id>/
- Método HTTP: GET
- Descripción: Devuelve los detalles de un producto específico.

## Crear un nuevo producto

- URL: /api/products/
- Método HTTP: POST
- Descripción: Crea un nuevo producto a partir de un JSON enviado en el cuerpo de la solicitud.

### Ejemplo de cuerpo de solicitud:

```
{
  "name": "Producto Ejemplo"
}
```

## Actualizar un producto existente

- URL: /api/products/<id>/
- Método HTTP: PUT
- Descripción: Actualiza los detalles de un producto existente.

### Ejemplo de cuerpo de solicitud:

```
{
  "name": "Producto Actualizado",
  "is_active": "false"
}
```

## Eliminar un producto

- URL: /api/products/<id>/
- Método HTTP: DELETE
- Descripción: Elimina un producto específico por su ID.

## Dependencias

El proyecto utiliza las siguientes dependencias, que están listadas en el archivo `requirements.txt`:

```
asgiref==3.8.1
Django==5.1.2
django-cors-headers==4.5.0
djangorestframework==3.15.2
sqlparse==0.5.1
tzdata==2024.2
python-dotenv==1.0.1
```

Estas dependencias están instaladas automáticamente al usar Docker y están listadas en el archivo requirements.txt.

## Docker

Este proyecto utiliza Docker para ejecutar los servicios necesarios. A continuación, se describe brevemente cómo está configurado el entorno Docker.

- Levantar los contenedores:

```
docker-compose up
```

- Detener los contenedores:

```
docker-compose down
```

- Reconstruir la imagen:

```
docker-compose up --build
```

- Acceder al contenedor web:

```
docker-compose exec web bash
```

## Pruebas

Para ejecutar las pruebas dentro del contenedor, usa el siguiente comando:

```
docker-compose exec web python manage.py test
```

## Despliegue en Producción

Para desplegar este proyecto en un entorno de producción:

1. Asegúrate de establecer `DEBUG=False` en el archivo `.env` o en la configuración de Docker.
2. Configura los valores de `ALLOWED_HOSTS` correctamente.
3. Considera usar un servidor web como Nginx para servir la aplicación en producción.
4. Utiliza un sistema de backend como Gunicorn o uWSGI para ejecutar la aplicación.
