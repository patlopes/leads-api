FROM python:3.10-slim

WORKDIR /app

COPY infrastructure/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["fastapi", "run", "main.py"]
EXPOSE 8000