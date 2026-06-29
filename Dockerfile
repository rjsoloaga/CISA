# 1. Imagen base liviana de Python
FROM python:3.12-slim

# 2. Variables de entorno recomendadas para Python en Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. INSTALAR DEPENDENCIAS DEL SISTEMA (Esto es lo que te falta)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 4. Directorio de trabajo
WORKDIR /app

# 5. Copiar e instalar requerimientos de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar el resto del código
COPY . /app/