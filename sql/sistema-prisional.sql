
-- Tabela BLOCO
CREATE TABLE BLOCO (
    CodBloco INT PRIMARY KEY,
    NomeBloco VARCHAR(50) UNIQUE NOT NULL,
    CapacidadeTotal INT NOT NULL
);

-- Tabela CELA
CREATE TABLE CELA (
    CodCela INT PRIMARY KEY,
    Numero VARCHAR(10) UNIQUE NOT NULL,
    Capacidade INT NOT NULL,
    CodBloco INT NOT NULL,
    FOREIGN KEY (CodBloco) REFERENCES BLOCO(CodBloco)
);

-- Tabela FUNCIONARIO
CREATE TABLE FUNCIONARIO (
    MatriculaFunc INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Cargo VARCHAR(30) NOT NULL,
    Setor VARCHAR(40) NOT NULL,
    DataAdmissao DATE NOT NULL
);

-- Tabela DETENTO (Preso)
CREATE TABLE DETENTO (
    Matricula INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF CHAR(11) UNIQUE NOT NULL,
    DataNascimento DATE NOT NULL,
    DataPrisao DATE NOT NULL,
    Regime VARCHAR(20) NOT NULL,
    CodCela INT NOT NULL,
    FOREIGN KEY (CodCela) REFERENCES CELA(CodCela)
);

-- Tabela ATIVIDADE
CREATE TABLE ATIVIDADE (
    CodAtividade INT PRIMARY KEY,
    Nome VARCHAR(100) UNIQUE NOT NULL,
    Tipo VARCHAR(30) NOT NULL,
    CargaHoraria INT NOT NULL
);

-- Tabela VISITANTE
CREATE TABLE VISITANTE (
    CodVisitante INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(200) NOT NULL,
    Telefone VARCHAR(15),
    CPF CHAR(11) UNIQUE NOT NULL
);

-- Tabela OCORRENCIA
CREATE TABLE OCORRENCIA (
    CodOcorrencia INT PRIMARY KEY,
    Descricao VARCHAR(255) NOT NULL,
    DataHora DATETIME NOT NULL,
    Tipo VARCHAR(20) NOT NULL,
    MatriculaPreso INT NOT NULL,
    MatriculaFunc INT NOT NULL,
    FOREIGN KEY (MatriculaPreso) REFERENCES DETENTO(Matricula),
    FOREIGN KEY (MatriculaFunc) REFERENCES FUNCIONARIO(MatriculaFunc)
);

-- Tabela PARTICIPACAO
CREATE TABLE PARTICIPACAO (
    DataInicio DATE NOT NULL,
    Status VARCHAR(30) NOT NULL,
    MatriculaPreso INT NOT NULL,
    CodAtividade INT NOT NULL,
    PRIMARY KEY (DataInicio, MatriculaPreso, CodAtividade),
    FOREIGN KEY (MatriculaPreso) REFERENCES DETENTO(Matricula),
    FOREIGN KEY (CodAtividade) REFERENCES ATIVIDADE(CodAtividade)
);

-- Tabela VISITA
CREATE TABLE VISITA (
    CodVisita INT PRIMARY KEY,
    DataVisita DATE NOT NULL,
    HoraInicio TIME NOT NULL,
    HoraFim TIME,
    Status VARCHAR(20) NOT NULL,
    CodVisitante INT NOT NULL,
    MatriculaPreso INT NOT NULL,
    FOREIGN KEY (CodVisitante) REFERENCES VISITANTE(CodVisitante),
    FOREIGN KEY (MatriculaPreso) REFERENCES DETENTO(Matricula)
);