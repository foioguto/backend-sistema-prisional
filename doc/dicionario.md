### Tabela: Preso (Detento)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **Matricula** | Código único de identificação do detento. | INT | Chave Primária (PK), Não Nulo |
| Nome | Nome completo do detento. | VARCHAR (100) | Não Nulo |
| CPF | Cadastro de Pessoa Física do detento. | CHAR (11) | Único, Não Nulo |
| DataNascimento | Data de nascimento do detento. | DATE | Não Nulo |
| DataPrisao | Data em que o detento deu entrada na unidade prisional. | DATE | Não Nulo |
| Regime | Regime de cumprimento da pena (Fechado, Semiaberto, etc.). | VARCHAR (20) | Não Nulo |
| **CodCela** | Chave estrangeira que liga o preso à Cela onde está alocado. | INT | Chave Estrangeira (FK), Não Nulo |

### Tabela: Cela

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **CodCela** | Código único para identificar a cela. | INT | Chave Primária (PK), Não Nulo |
| Numero | Número ou identificação da cela. | VARCHAR (10) | Único, Não Nulo |
| Capacidade | Capacidade máxima de detentos na cela. | INT | Não Nulo |
| **CodBloco** | Chave estrangeira que liga a cela ao Bloco onde está localizada. | INT | Chave Estrangeira (FK), Não Nulo |

### Tabela: Funcionário (Agente Penitenciário)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **MatriculaFunc** | Matrícula única do funcionário na instituição. | INT | Chave Primária (PK), Não Nulo |
| Nome | Nome completo do funcionário. | VARCHAR (100) | Não Nulo |
| Cargo | Cargo ou função exercida (Agente, Supervisor, etc.). | VARCHAR (30) | Não Nulo |
| Setor | Setor de trabalho do funcionário. | VARCHAR (40) | Não Nulo |
| DataAdmissao | Data de início das atividades do funcionário. | DATE | Não Nulo |

### Tabela: Ocorrência (Exemplo de Entidade de Relacionamento)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **CodOcorrencia** | Código único para identificação da ocorrência. | INT | Chave Primária (PK), Não Nulo |
| Descricao | Detalhes sobre o incidente ou infração. | VARCHAR (255) | Não Nulo |
| DataHora | Momento exato em que a ocorrência foi registrada. | DATETIME | Não Nulo |
| Tipo | Classificação da ocorrência (Leve, Grave, Segurança, etc.). | VARCHAR (20) | Não Nulo |
| **MatriculaPreso** | FK que liga a ocorrência ao detento envolvido. | INT | Chave Estrangeira (FK), Não Nulo |
| **MatriculaFunc** | FK que liga a ocorrência ao funcionário que a registrou. | INT | Chave Estrangeira (FK) |

### Tabela: Bloco (Estrutura Física)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **CodBloco** | Código único para identificar o bloco na penitenciária. | INT | Chave Primária (PK), Não Nulo |
| NomeBloco | Nome ou identificação da seção/ala (Ex: Bloco A, Ala de Segurança Máxima). | VARCHAR (50) | Único, Não Nulo |
| CapacidadeTotal | Soma da capacidade de todas as celas do bloco. | INT | Não Nulo |

### Tabela: Visitante

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **CodVisitante** | Código de identificação único para o visitante. | INT | Chave Primária (PK), Não Nulo |
| Nome | Nome completo do visitante. | VARCHAR (100) | Não Nulo |
| CPF | CPF do visitante. | CHAR (11) | Único, Não Nulo |
| Telefone | Telefone de contato do visitante. | VARCHAR (15) | Opcional |
| Endereco | Endereço completo do visitante. | VARCHAR (200) | Não Nulo |

### Tabela: Visita (Agendamento e Registro)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **CodVisita** | Código único da visita. | INT | Chave Primária (PK), Não Nulo |
| DataVisita | Data programada ou realizada da visita. | DATE | Não Nulo |
| HoraInicio | Horário de início da visita. | TIME | Não Nulo |
| HoraFim | Horário de término da visita. | TIME | Opcional |
| Status | Status da visita (Agendada, Realizada, Cancelada). | VARCHAR (20) | Não Nulo |
| **MatriculaPreso** | FK para o detento que receberá a visita. | INT | Chave Estrangeira (FK), Não Nulo |
| **CodVisitante** | FK para o visitante que está realizando a visita. | INT | Chave Estrangeira (FK), Não Nulo |

### Tabela: Atividade (Ressocialização)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **CodAtividade** | Código de identificação único da atividade (Ex: Curso de Eletricista). | INT | Chave Primária (PK), Não Nulo |
| Nome | Nome da atividade. | VARCHAR (100) | Único, Não Nulo |
| Tipo | Tipo de programa (Trabalho, Estudo, Religioso, Esporte). | VARCHAR (30) | Não Nulo |
| CargaHoraria | Duração total da atividade (em horas). | INT | Não Nulo |

### Tabela: Participação (Relacionamento N:M entre Preso e Atividade)

| Atributo | Descrição | Domínio | Restrição do Atributo |
| :--- | :--- | :--- | :--- |
| **MatriculaPreso** | FK para o detento que participa da atividade. | INT | Chave Estrangeira (FK), Chave Composta |
| **CodAtividade** | FK para a atividade da qual o detento participa. | INT | Chave Estrangeira (FK), Chave Composta |
| **DataInicio** | Data de início da participação do detento. | DATE | Chave Composta, Não Nulo |
| Status | Situação da participação (Em andamento, Concluída, Desligado). | VARCHAR (30) | Não Nulo |