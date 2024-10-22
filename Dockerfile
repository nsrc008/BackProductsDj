# Usar una imagen base de Python
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Exponer el puerto en el que la API se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
