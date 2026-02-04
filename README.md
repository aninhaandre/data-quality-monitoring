# 📊 Data Quality Monitoring

Sistema para monitoramento e validação da qualidade de dados em pipelines ETL.

---

## 🎯 Objetivo

Garantir que os dados carregados estejam:

- Completos  
- Consistentes  
- Sem duplicidades  
- Dentro dos padrões esperados  

---

## 🛠️ Tecnologias Utilizadas

- Python  
- SQL  
- Apache Airflow  
- PostgreSQL  
- Pandas  
- Docker  

---

## ⚙️ Funcionalidades

- Validação de campos obrigatórios  
- Detecção de valores nulos  
- Monitoramento de volumes  
- Alertas de inconsistência  
- Logs de execução  
- Orquestração automática com Airflow  

---

## 📁 Estrutura do Projeto

```bash
data-quality-monitoring/
│
├── dags/          # DAGs do Airflow
├── src/           # Código principal
├── SQL/           # Scripts SQL
├── testes/        # Testes automatizados
├── cadernos/      # Notebooks
├── painel/        # Visualizações/Dashboard
├── Dockerfile     # Containerização
├── requirements.txt
└── README.md
▶️ Como Executar
1️⃣ Clonar o repositório
git clone https://github.com/aninhaandre/data-quality-monitoring.git
cd data-quality-monitoring
2️⃣ Criar ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Executar validação
python src/main.py

⏱️ Orquestração com Airflow

O projeto utiliza Apache Airflow para automatizar as validações.

Exemplo de DAG:
with DAG(
    dag_id="data_quality_monitoring",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    check_null_values = PythonOperator(
        task_id="check_null_values",
        python_callable=check_nulls,
    )
📈 Exemplo de Resultado

Após a execução, o sistema gera relatórios indicando:

Colunas com valores nulos

Inconsistências

Volume fora do padrão

Esses dados podem ser usados para auditoria e melhoria contínua.

👩‍💻 Autora

Ana Paula
Engenheira de Dados

🔗 LinkedIn: (www.linkedin.com/in/anapaulameloandre)
🐙 GitHub: https://github.com/aninhaandre
