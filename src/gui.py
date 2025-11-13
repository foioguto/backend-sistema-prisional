import PySimpleGUI as sg
import json
from src.db.connection import session 
from sqlalchemy import text
from pandas import DataFrame 

def execute_sql_query(sql_query: str, params_json: str):
    """
    Executa a query no banco de dados usando a sessão SQLAlchemy.
    """
    params_dict = {}
    try:
        # Tenta converter o JSON de argumentos em um dicionário Python
        if params_json:
            params_dict = json.loads(params_json)
            
    except json.JSONDecodeError as e:
        return f"Erro no JSON de Argumentos: {e}"
    except Exception as e:
        return f"Erro inesperado ao processar argumentos: {e}"

    try:
        # Prepara a query
        query = text(sql_query)
        
        # Executa a query com os parâmetros
        result_proxy = session.execute(query, params_dict)
        
        # Se for um INSERT, UPDATE, ou DELETE, precisamos comitar
        # DEPOIS (Corrigido)
        if sql_query.strip().lower().startswith(('insert', 'update', 'delete', 'create', 'truncate', 'set')):
            session.commit()
            return f"Comando executado com sucesso. {result_proxy.rowcount} linhas afetadas."
        
        # Se for um SELECT, busca os resultados
        else:
            # Pega os nomes das colunas
            keys = result_proxy.keys()
            # Pega todas as linhas
            rows = result_proxy.fetchall()
            
            if not rows:
                return "Query executada, mas não retornou resultados."
            
            # Formata a saída usando um DataFrame do Pandas (fica bonito)
            df = DataFrame(rows, columns=keys)
            return df.to_string(index=False)

    except Exception as e:
        # Se der erro (ex: SQL errado), desfaz a transação e mostra o erro
        session.rollback()
        return f"Erro ao executar a query: {e}"

# --- Interface Gráfica ---

sg.theme('DarkBlue3') # Define um tema

# 1. Definir o Layout
layout = [
    [sg.Text('Query SQL:')],
    [sg.Multiline(size=(100, 15), key='-SQL-', font=('Courier New', 10))],
    
    [sg.Text('Argumentos (Ex: {"id": 10001, "regime": "Fechado"} )')],
    [sg.Input(size=(100, 1), key='-PARAMS-')],
    
    [sg.Button('Executar', bind_return_key=True), sg.Button('Sair')],
    
    [sg.Text('Saída:')],
    [sg.Multiline(size=(100, 20), key='-OUTPUT-', font=('Courier New', 10), disabled=True, text_color='black')]
]

# 2. Criar a Janela
window = sg.Window('Cliente SQL do Sistema Prisional', layout, resizable=True)

# 3. Loop de Eventos
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
        
    if event == 'Executar':
        # Pega os valores da interface
        sql = values['-SQL-']
        params = values['-PARAMS-']
        
        if not sql.strip():
            window['-OUTPUT-'].update("Por favor, digite uma query SQL.")
            continue
            
        # Chama a nossa função de lógica
        resultado = execute_sql_query(sql, params)
        
        # Atualiza a caixa de saída
        window['-OUTPUT-'].update(resultado)

# Fecha a sessão e a janela
session.close()
window.close()