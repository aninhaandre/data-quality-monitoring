def check_nulls():
    import pandas as pd
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://user:password@localhost:5432/seu_banco')
    df = pd.read_sql("SELECT * FROM sua_tabela", engine)...