# Django ZIP Code app
Está aplicación brinda información sobre las colonias y municipios pertenecientes a un código postal específico.

## Assignment
### Setup
1. Iniciar el entorno de Django.
2. Instalar dependencias registradas en el archivo requirement.txt.
3. Crear base de datos llamada "States" en MySQL.
4. Iniciar migraciones en base a los modelos.
5. Migrar a base de datos MySQL.
6. Respaldar datos desde archivo CPdescarga.txt usando el archivo fetch.py.
7. Iniciar servidor.

## Init Django environment
```bash
. .venv/bin/activate
```

## Create databse in MySQL
```bash
create database States;
```

## Setup application
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Backup ZIP Code data to database
```bash
python fetch.py
```

## Running the app
```bash
python manage.py runserver
```


### Requirements
- Mysql
- Python
- Django