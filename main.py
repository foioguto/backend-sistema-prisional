import sys
from src.gui import execute_sql_query
from src.db.connection import session

def main_cli():
    """
    Função principal para rodar a aplicação via linha de comando (CLI).
    """
    print("--- Cliente SQL (Modo Terminal) ---")
    print("Digite 'sair' a qualquer momento para fechar.")
    print("-" * 30)

    try:
        while True:
            sql_input = input("SQL> ")
            if sql_input.lower() == 'sair':
                break
        
            params_input = input("Parâmetros (JSON)> ")
            if params_input.lower() == 'sair':
                break

            resultado = execute_sql_query(sql_input, params_input)
            
            print("\n--- Resultado ---")
            print(resultado)
            print("-" * 30)

    except KeyboardInterrupt:
        # Permite sair com Ctrl+C
        print("\nSaindo...")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
    finally:
        print("\nFechando conexão com o banco de dados.")
        session.close()

if __name__ == "__main__":
    main_cli()