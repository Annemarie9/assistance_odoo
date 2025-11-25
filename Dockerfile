FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirement.txt (SANS 's')
COPY requirement.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirement.txt && \
    rm -rf /tmp/* /root/.cache

# Définir le PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Copier tout le code source
COPY . /app/

# Exposer les ports pour Streamlit (8501) et Flask (5000)
EXPOSE 8501 5000

# Commande par défaut (sera overridée par docker-compose)
CMD ["python", "src/api.py"]