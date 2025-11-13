from sqlalchemy import text
from connection import session, engine
import sys

# IMPORTANTE: Lista das tabelas erradas (minúsculas/mistas)
# que foram criadas pelo pandas.
# A tabela 'Preso' também será apagada.
TABLES_TO_DROP = [
    'Atividade',
    'Bloco',
    'Cela',
    'Funcionario',
    'Ocorrencia',
    'Participacao',
    'Preso', 
    'Visita',
    'Visitante'
]

def drop_tables():
    """
    Conecta ao banco e remove as tabelas da lista TABLES_TO_DROP.
    """
    print("--- INICIANDO LIMPEZA DE TABELAS DUPLICADAS ---")
    
    try:
        # Usar 'with session.begin()' garante que tudo seja
        # executado em uma transação.
        with session.begin():
            for table_name in TABLES_TO_DROP:
                try:
                    # Usamos 'text()' para executar SQL puro de forma segura
                    # O 'IF EXISTS' garante que o script não falhe
                    # se a tabela já foi apagada.
                    sql_command = text(f"DROP TABLE IF EXISTS `{table_name}`")
                    
                    print(f"Executando: {sql_command}")
                    session.execute(sql_command)
                    print(f"Tabela `{table_name}` removida com sucesso.")
                    
                except Exception as e:
                    print(f"Erro ao tentar remover a tabela `{table_name}`: {e}")
                    # Mesmo com erro, continua para a próxima tabela
        
        print("--- LIMPEZA FINALIZADA ---")

    except Exception as e:
        print(f"\nErro fatal de conexão ou transação: {e}")
        print("Script abortado.")
        session.rollback() # Desfaz tudo se houver um erro maior
    finally:
        session.close() # Fecha a sessão

if __name__ == "__main__":
    # Confirmação de segurança
    print("ATENÇÃO: Este script irá remover as seguintes tabelas do seu banco de dados:")
    for t in TABLES_TO_DROP:
        print(f"- {t}")
    
    confirm = input("Você tem certeza que deseja continuar? (s/n): ")
    
    if confirm.lower() == 's' or confirm.lower() == 'sim':
        drop_tables()
    else:
        print("Operação cancelada.")
        sys.exit()