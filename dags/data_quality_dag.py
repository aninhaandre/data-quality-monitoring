from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.validators.null_checks import check_nulls

# DAG setup...