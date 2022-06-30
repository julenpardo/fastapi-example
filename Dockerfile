FROM python:3.8-slim

WORKDIR /srv
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]
