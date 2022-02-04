FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/
RUN apt update && apt install libpq-dev python3-dev xmlsec1 libxml2-dev libxmlsec1-dev libxmlsec1-openssl -y
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# TODO: productionalize
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]