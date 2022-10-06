FROM python:3.10.6-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY montessori .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

