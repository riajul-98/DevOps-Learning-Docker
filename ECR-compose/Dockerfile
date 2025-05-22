FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install flask mysqlclient

EXPOSE 5000

CMD ["python", "app.py"]