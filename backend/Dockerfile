FROM python:3.9-bullseye

WORKDIR /app

# Copier requirements.txt et installer les dépendances
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier chaque fichier explicitement
COPY app/main.py .
COPY app/database.py .
COPY app/models.py .
COPY app/.env .
COPY app/test_db.py .

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]