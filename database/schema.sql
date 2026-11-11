PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS paciente (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL CHECK(length(trim(nome)) > 0),
    cpf TEXT UNIQUE NOT NULL CHECK(length(trim(cpf)) = 11),
    data_nascimento TEXT NOT NULL,
    telefone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS medico (
    id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL CHECK(length(trim(nome)) > 0 ),
    crm TEXT UNIQUE NOT NULL CHECK(length(trim(crm)) > 0),
    especialidade TEXT NOT NULL CHECK(length(trim(especialidade)) > 0),
    telefone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS consulta (
    id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER NOT NULL,
    id_medico INTEGER NOT NULL,
    data_hora TEXT NOT NULL,
    diagnostico TEXT NOT NULL,
    valor_consulta REAL NOT NULL CHECK(valor_consulta >= 0),
    FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente) ON DELETE CASCADE,
    FOREIGN KEY (id_medico) REFERENCES medico(id_medico) ON DELETE RESTRICT
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_consulta_medico_data_hora
ON consulta (id_medico, data_hora);