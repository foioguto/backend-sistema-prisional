# 1. Modelo Conceitual

## 1.1 Definição do Minimundo: Sistema de Gestão Prisional (SGP)

O Sistema de Gestão Prisional (SGP) será desenvolvido para informatizar e otimizar as operações de uma unidade prisional de médio porte, focando no acompanhamento dos **presos**, no gerenciamento das **visitas** e na alocação da **estrutura física** da penitenciária.

### 📝 Requisitos Funcionais e de Negócio

1.  **Cadastro e Acompanhamento do Preso:** O sistema deve registrar todos os dados pessoais do preso, informações sobre a pena (início, fim, regime), e o histórico de transferências dentro da unidade.
2.  **Gerenciamento da Estrutura:** O sistema deve manter o cadastro da estrutura da prisão, incluindo **Blocos** e **Celas**, e a alocação atual de cada preso.
3.  **Controle de Ocorrências:** Deve ser possível registrar **Ocorrências** disciplinares ou de segurança relacionadas aos presos e aos funcionários.
4.  **Gestão de Visitas:** O sistema deve controlar o cadastro de **Visitantes** autorizados, agendamentos e o registro da efetivação das visitas.
5.  **Acompanhamento de Atividades:** É fundamental registrar a participação dos presos em programas de **Trabalho** ou **Estudo** como parte do processo de ressocialização.
6.  **Gerenciamento de Funcionários:** O cadastro de **Funcionários** (Agentes e Administrativos) é necessário para a segurança e para vincular responsabilidades a ocorrências e escalas de trabalho.

### 👥 Entidades Principais Identificadas 

| Entidade | Descrição |
| :--- | :--- |
| **Preso** | Guarda as informações pessoais e de pena do detento. |
| **Funcionário** | Armazena dados dos agentes penitenciários e demais servidores. |
| **Ocorrência** | Registra qualquer incidente ou falta disciplinar. |
| **Bloco** | Representa a estrutura física de uma seção da prisão. |
| **Cela** | Detalha as celas contidas nos blocos, incluindo capacidade. |
| **Visitante** | Informações das pessoas autorizadas a fazer visitas. |
| **Visita** | Registra o agendamento e a efetivação das visitas. |
| **Atividade** | Programas de trabalho, estudo ou ressocialização disponíveis. |
| **Participação** | Tabela de relacionamento para registrar o envolvimento do preso nas Atividades. |

### 🔗 Mapeamento Preliminar dos Relacionamentos

* Um **Preso** está alocado em exatamente uma **Cela**, mas uma **Cela** pode conter um ou mais **Presos** (1:N).
* Uma **Cela** pertence a um único **Bloco**, e um **Bloco** possui várias **Celas** (1:N).
* Uma **Ocorrência** é registrada por um **Funcionário**, e um **Funcionário** pode registrar várias **Ocorrências** (1:N).
* Um **Preso** pode ter um ou mais **Visitantes** autorizados, e um **Visitante** pode estar autorizado a visitar um ou mais **Presos** (N:N - resolvida por uma tabela de relacionamento *Autorização*).
* Uma **Visita** é agendada para um **Preso** e envolve um **Visitante** (N:M).

---