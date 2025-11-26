# Imagen base
FROM python:3.11-slim

# Evitar buffer en logs
ENV PYTHONUNBUFFERED=1

# Crear directorio de la app
WORKDIR /app

# Copiar requirements antes para aprovechar cache
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto para Flask
EXPOSE 8816

# Comando de ejecución
CMD ["python", "app.py"]