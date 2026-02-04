from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Importa sua função de validação
from src.validators.null_checks import check_nulls


# Argumentos padrão da DAG
default_args = {
    "owner": "ana_paula",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


# Definição da DAG
with DAG(
    dag_id="data_quality_monitoring",
    description="DAG para validação de qualidade de dados",
    default_args=default_args,
    schedule_interval="@daily",  # roda diariamente
    catchup=False,
    tags=["data-quality", "etl", "monitoring"],
) as dag:

    # Task: Validação de dados nulos
    check_null_values = PythonOperator(
        task_id="check_null_values",
        python_callable=check_nulls,
    )

    # Definição do fluxo
    check_null_values
