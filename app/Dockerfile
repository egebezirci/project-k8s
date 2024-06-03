FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV DATABASE_URL=postgresql://kind:password@db:5432/postgres

EXPOSE 80

COPY . .

CMD ["python", "app.py"]
