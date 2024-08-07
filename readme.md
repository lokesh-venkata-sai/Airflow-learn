# Instructions to run airflow using docker
# Install Docker

# Download docker-compose.yaml
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.3/docker-compose.yaml'

# In docker-compose.yaml change executor from 'CeleryExecutor' to 'LocalExecutor'

# Remove AIRFLOW__CELERY__RESULT_BACKEND, AIRFLOW__CELERY__BROKER_URL in docker-compose.yaml file

# Delete Redis dependency and config from the file

# Remove Celery worker and flower also

# change AIRFLOW__CORE__LOAD_EXAMPLES from 'true' to 'false'

# create folders
mkdir dags
mkdir logs
mkdir plugins
mkdir config

# Initialize database
docker compose up airflow-init

# in .env file add --> AIRFLOW_UID=50000 (Just to avoid a warning msg AIRFLOW_UID is not set)

# Run Airflow (use -d to run containers in background)
docker compose up -d

# Check which containers are running
docker ps

# Now docker will run on http://localhost:8080/

default username and pwd is "airflow"


# To stop and remove the containers
docker-compose down -v


# To expose Postgres
    Add this under services under prostgres service
    ```sh
    ports:
      - 5432:5432

# Then recreate postgres container using following command
    docker-compose up -d --no-deps --build postgres

# If we want to connect to postgres database use dbeaver community edition
# create a new postgres connection (username and password is "airflow')

# In the Airflow UI, go to admin -> connections -> create a new connection (for postgres)
# In host: host.docker.local (for windows or mac, when using postgres from docker)

# Instructions to run airflow in windows using python (currently there are issues with airflow compatibility in windows - so not working)

# To create virtual environment
python -m venv py_env

# activate virtual environment
py_env\Scripts\activate

# To decativate Virtual environment
py_env\Scripts\deactivate

# Install Airflow
# source: https://github.com/apache/airflow
pip install 'apache-airflow==2.9.3' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.8.txt"


# Set the AIRFLOW_HOME environment variable to define where Airflow should store its configuration and logs. You can set this in your terminal session.
set AIRFLOW_HOME=. # recommended - for current director
set AIRFLOW_HOME=%USERPROFILE%\airflow # If we install for full system

# Initialize the Airflow database by running:
airflow db init

