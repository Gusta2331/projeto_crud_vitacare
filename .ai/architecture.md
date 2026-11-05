# Arquitetura e Padrões de Software

Este documento define a organização de pastas, camadas e contratos de software que devem ser estritamente seguidos por qualquer agente de IA ao gerar ou modificar código.

---

## 🏗️ Estrutura de Diretórios Obrigatória

```text
projeto_crud/
│
├── .ai/                               # Informações e contexto para agentes de IA
│   ├── README.md
│   ├── architecture.md
│   ├── conventions.md
│   └── domain-guide.md
│
├── database/
│   ├── connection.py                  # Gerenciamento da conexão com o banco de dados (SQLite/PostgreSQL)
│   └── schema.sql                     # Script DDL com CREATE TABLE, constraints e chaves
│
├── models/                            # Entidades de domínio (POO com __init__ e propriedades)
│   ├── cliente.py
│   └── ...
│
├── repositories/                      # Camada de abstração e acesso a dados (Padrão Repository)
│   ├── cliente_memory_repository.py   # Fase 1: CRUD manipulando coleções em memória
│   └── cliente_database_repository.py # Fase 2: CRUD executando comandos SQL nativos
│
├── services/                          # Regras de negócio, validações complexas e relatórios analíticos
│   └── ...
│
├── requirements.txt                   # Dependências mínimas do projeto
├── main.py                            # Interface interativa de linha de comando (CLI)
├── AGENTS.md                          # Ponto de entrada padrão para agentes de IA
└── README.md                          # Documentação acadêmica do projeto
```

---

## 🧩 Responsabilidades de Cada Camada

### 1. `models/` (Domínio)
- Contém classes puras em Python representando as entidades de negócio.
- Devem possuir método construtor `__init__`, atributos tipados ou documentados, e métodos utilitários próprios do domínio quando aplicável.
- **Não** devem conter lógica de acesso a banco de dados nem comandos SQL.

### 2. `repositories/` (Persistência)
- Implementa o **Repository Pattern por convenção**.
- Não utilizar bibliotecas de ORM externas.
- As implementações em memória e em banco de dados devem compartilhar a exata mesma assinatura de métodos:
  - `save(objeto)`: Insere uma nova entidade e retorna a entidade com ID gerado (ou `objeto`).
  - `get_all()`: Retorna uma lista de todas as instâncias da entidade.
  - `find_by_id(id)`: Retorna a instância correspondente ou `None`.
  - `update(objeto)`: Atualiza os dados da entidade existente (retorna `bool` ou a entidade atualizada).
  - `delete(id)`: Remove o registro por identificador e retorna `True` (se removido) ou `False` (se não encontrado).

### 3. `services/` (Regras de Negócio)
- Orquestra chamadas aos repositórios.
- Aplica validações de negócio (ex.: impedir duplicação de dados únicos, validação de regras temporais, cálculos de totais ou status).
- Executa consultas analíticas e agregações da Fase 2.

### 4. `database/` (Infraestrutura SQL)
- `connection.py`: Função `criar_conexao()` que fornece a conexão ativa (ex.: via `sqlite3` nativo da biblioteca padrão).
- `schema.sql`: Definição formal das tabelas com constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `CHECK`).

### 5. `main.py` (Apresentação / CLI)
- Interface de terminal interativa com menus numéricos.
- Coleta entradas com validação robusta.
- Não deve conter queries SQL ou manipulação direta de arquivos/listas globais; apenas interage com a camada de serviços ou repositórios.
- Na transição da Fase 1 para a Fase 2, **apenas** a inicialização da instância do repositório deve ser alterada.

