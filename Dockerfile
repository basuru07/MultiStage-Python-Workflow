<<<<<<< HEAD
FROM python:3.10-slim
=======
FROM python:3.11-slim
>>>>>>> 308e14e027f0a28401cdea07be459df4a29264c7

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
=======
COPY app/ app/

EXPOSE 5000

CMD ["python", "app/main.py"]
>>>>>>> 308e14e027f0a28401cdea07be459df4a29264c7
