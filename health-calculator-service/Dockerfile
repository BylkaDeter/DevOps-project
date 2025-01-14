FROM python:3.9-slim

# repertoire de travial dans le container 
WORKDIR /app

# on copie tout dans le /app du container
COPY . /app

# installation des dependances dans le container 
RUN pip install --no-cache-dir -r requirements.txt

# exposition du port 5000 car flask tourne sur ce port
EXPOSE 5000

# demarrage de l'app
CMD ["python", "app.py"]
