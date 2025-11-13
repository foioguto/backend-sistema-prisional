# backend-sistema-prisional

Backend para gestão de sistema prisional — desenvolvido em **Python** com arquitetura modular, endpoints REST e suporte a banco de dados relacional.

---

## 📘 Visão geral

O **backend-sistema-prisional** oferece a infraestrutura de software necessária para gerenciar informações do sistema prisional, incluindo:
- cadastro e controle de presos;
- movimentações e registros históricos;
- autenticação e autorização de usuários;
- gerenciamento de unidades prisionais e visitantes.

---

## ⚙️ Funcionalidades

- CRUD completo para entidades principais (presos, unidades, visitantes, movimentações);
- Sistema de login/autenticação via token (JWT ou similar);
- Integração com banco de dados relacional (PostgreSQL, MySQL, etc);
- Configuração via arquivo `.env`;
- Estrutura organizada por módulos no diretório `src/`.

---

## 🧰 Tecnologias

- **Python** (>=3.10)
- **Framework Web:** (FastAPI, Flask ou Django – conforme implementação)
- **Banco de Dados:** PostgreSQL / MySQL / SQLite
- **ORM:** SQLAlchemy / Django ORM
- **Gerenciamento de dependências:** `requirements.txt`
- **Controle de versão:** Git + GitHub

---

## 📦 Estrutura de diretórios

backend-sistema-prisional/
│
├── src/ # Código-fonte principal
├── data/ # Seeds, dumps ou dados auxiliares
├── doc/ # Documentação técnica
├── .env.example # Exemplo de variáveis de ambiente
├── requirements.txt # Dependências do projeto
├── main.py # Ponto de entrada da aplicação
└── README.md