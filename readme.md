# Running Apache Airflow with Docker and Python

## Docker Installation

### Steps to run Airflow using Docker

1. **Install Docker**  
   Ensure Docker is installed on your system. Follow instructions at [Docker's official website](https://docs.docker.com/get-docker/).

2. **Download `docker-compose.yaml`**
   ```bash
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.3/docker-compose.yaml'
   ```
   - In `docker-compose.yaml`, change the executor from 'CeleryExecutor' to 'LocalExecutor'.
   - Remove `AIRFLOW__CELERY__RESULT_BACKEND` and `AIRFLOW__CELERY__BROKER_URL` in the `docker-compose.yaml` file.
   - Delete Redis dependency and configuration from the file.
   - Remove Celery worker and Flower as well.
   - Change `AIRFLOW__CORE__LOAD_EXAMPLES` from 'true' to 'false'.

3. **Create Folders**
   ```bash
   mkdir dags
   mkdir logs
   mkdir plugins
   mkdir config
   ```

4. **Initialize Database**
   ```bash
   docker compose up airflow-init
   ```

5. **Environment Setup**
   - In the `.env` file add: `AIRFLOW_UID=50000` (Just to avoid a warning message that AIRFLOW_UID is not set)


6. **Run Airflow**
   - Use `-d` to run containers in the background:
     ```bash
     docker compose up -d
     ```

7. **Check Containers**
   ```bash
   docker ps
   ```

   - Airflow will now be running on http://localhost:8080/  by docker
   - Default username and password are "airflow".

8. **Stop and Remove Containers**
   ```bash
   docker-compose down -v
   ```

9. **Expose Postgres**
   - Add this under services in the `docker-compose.yaml` under the PostgreSQL service:
     ```yaml
     ports:
       - 5432:5432
     ```
   - Then recreate the PostgreSQL container using the following command:
     ```bash
     docker-compose up -d --no-deps --build postgres
     ```

10. **Connect to PostgreSQL**
    - Use DBeaver Community Edition to create a new PostgreSQL connection (username and password are "airflow").
    - In the Airflow UI, go to Admin -> Connections -> Create a new connection (for PostgreSQL). 
        - In host: host.docker.internal (for Windows or Mac, when using PostgreSQL from Docker).


### Instructions to Run Airflow on Windows Using Python

(Currently, there are compatibility issues with Airflow on Windows, so this might not work properly.)

1. **Create Virtual Environment**
   ```bash
   python -m venv py_env
   ```

2. **Activate Virtual Environment**
   ```bash
   py_env\Scripts\activate
   ```

3. **Deactivate Virtual Environment**
   ```bash
   py_env\Scripts\deactivate
   ```

4. **Install Airflow**
    source: https://github.com/apache/airflow
   ```bash
   pip install 'apache-airflow==2.9.3' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.8.txt"
   ```

5. **Set AIRFLOW_HOME Environment Variable**
   ```bash
   set AIRFLOW_HOME=.  # Recommended - for current directory
   set AIRFLOW_HOME=%USERPROFILE%\airflow  # If installing for the full system
   ```
