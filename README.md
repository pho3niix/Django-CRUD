# Django ZIP Code app
Está aplicación brinda información sobre las colonias y municipios pertenecientes a un código postal específico.

### Setup
1. Instalar MySQL
2. Instalar Python
3. Instalar dependencias registradas en el archivo requirement.txt.
4. Iniciar el entorno de Django.
5. Crear base de datos llamada "States" en MySQL.
6. Iniciar migraciones en base a los modelos.
7. Migrar a base de datos MySQL.
8. Respaldar datos desde archivo CPdescarga.txt usando el archivo fetch.py.
9. Iniciar servidor.

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

## Access URL
http://ec2-3-82-193-231.compute-1.amazonaws.com/api/v3/?zp=66055

### Requirements
- Mysql
- Python
- Django