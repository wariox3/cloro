# Backend servicios DIAN

Para instalar el proyecto debes seguir las siguientes instrucciones en la terminar

```sh
git clone
cd cloro
crear archivo al nivel de manage.py llamado .env con estas variables

# Entorno
ENV='dev'
# Credenciales base de datos
DATABASE_USER='user'
DATABASE_PASSWORD='clave'
DATABASE_HOST='localhost'
DATABASE_NAME='bdprueba'
DATABASE_PORT='5432'

# Credenciales mongo
DATABASE_MONGO='123'

# Credenciales Service Bus
SERVICE_BUS_CONNECTION_STR='123'
SERVICE_BUS_QUEUE_NAME='escribirXml'

python3.10 -m venv ~/.venvs/cloro
source ~/.venvs/nombreproyecto/bin/activate
pip install -r requirements.txt

# Ejecutar los fixtures
python manage.py loaddata cliente/fixtures/*.json

# Iniciar el servicio
python manage.py runserver
# Migrar la base de datos -> Debe estar creada
python manage.py migrate
```