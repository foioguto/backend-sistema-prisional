import pandas as pd
from read_csv import read_csv  
from db.connection import engine 

def load_csv_to_db(csv_path: str, table_name: str, if_exists_policy: str = 'append'):
    """
    Lê um arquivo CSV e o carrega em uma tabela específica do banco de dados.

    Args:
        csv_path (str): O caminho para o arquivo CSV.
        table_name (str): O nome da tabela no banco de dados onde os dados
                          serão inseridos.
        if_exists_policy (str): Como agir se a tabela já existir.
                               'fail': Levanta um erro (Default do pandas).
                               'replace': Dropa a tabela e cria de novo (CUIDADO).
                               'append': Insere os dados na tabela (Mais comum).
    """
    print(f"Iniciando a carga do arquivo: {csv_path}")
    
    df = read_csv(csv_path)
    
    if df.empty:
        print(f"O DataFrame do arquivo {csv_path} está vazio. Carga abortada.")
        return

    print(f"Lendo {len(df)} linhas do arquivo {csv_path}.")
    print(f"Carregando dados para a tabela: {table_name}...")

    try:
        df.to_sql(
            name=table_name,        # Nome da tabela no BD
            con=engine,             # Conexão do SQLAlchemy
            if_exists=if_exists_policy, # O que fazer se a tabela existir
            index=False             # MUITO IMPORTANTE: Não salva o índice do pandas
                                    # como uma coluna no BD.
        )
        
        print(f"Carga do arquivo {csv_path} para a tabela {table_name} concluída com sucesso.")

    except Exception as e:
        print(f"Erro ao carregar dados para a tabela {table_name}: {e}")

if __name__ == "__main__":
    
    print("--- INICIANDO CARGA DE DADOS ---")
    
    # Nível 1 (Não dependem de ninguém)
    load_csv_to_db('Bloco.csv', 'Bloco')
    load_csv_to_db('Funcionario.csv', 'Funcionario')
    load_csv_to_db('Visitante.csv', 'Visitante')
    load_csv_to_db('Atividade.csv', 'Atividade')
    
    # Nível 2 (Dependem do Nível 1)
    load_csv_to_db('Cela.csv', 'Cela') # Depende de Bloco
    
    # Nível 3 (Dependem dos níveis anteriores)
    load_csv_to_db('Preso.csv', 'Preso') # Depende de Cela
    
    # Nível 4 (Dependem de Preso, Funcionario, Visitante, Atividade)
    load_csv_to_db('Ocorrencia.csv', 'Ocorrencia') # Depende de Preso, Funcionario
    load_csv_to_db('Visita.csv', 'Visita')       # Depende de Preso, Visitante
    load_csv_to_db('Participacao.csv', 'Participacao') # Depende de Preso, Atividade
    
    print("--- CARGA DE DADOS FINALIZADA ---")
