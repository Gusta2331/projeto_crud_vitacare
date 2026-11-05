# Contexto para Agentes de IA

Bem-vindo ao projeto **Aplicação CRUD com Arquitetura em Camadas e Persistência de Dados**.
Esta pasta (`.ai/`) reúne as diretrizes arquiteturais, regras de negócio e convenções de código para guiar qualquer agente de Inteligência Artificial (como Antigravity, Claude, ChatGPT, Cursor, Copilot, Windsurf, etc.) no desenvolvimento, refatoração e manutenção do código deste repositório.

---

## 📌 Sumário de Documentos

| Arquivo | Descrição |
| :--- | :--- |
| [architecture.md](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/architecture.md) | Arquitetura em camadas, padrão Repository, ciclo de vida das 2 fases e regras de desacoplamento. |
| [conventions.md](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/conventions.md) | Padrões de código (PEP 8), tratamento de exceções, convenções de nomenclatura e robustez da CLI. |
| [domain-guide.md](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/domain-guide.md) | Regras para modelagem das entidades (1:N, N:N associativa), DDL/SQL e relatórios analíticos. |

---

## 🧭 Visão Geral Rápida do Projeto

- **Contexto:** Disciplina de Estruturação, Modelagem e Persistência de Dados (Curso de Engenharia de Software - UNIFAN).
- **Docente:** Prof. Renan Felipe Brito Dantas.
- **Objetivo:** Aplicação CLI interativa em Python implementando operações CRUD com arquitetura desacoplada.
- **Linguagem & Tecnologias:** Python 3.10+, SQLite/SQL nativo, coleções em memória (`list`, `dict`), sem uso de ORMs complexos (SQLAlchemy, Django ORM, etc.).

---

## ⚙️ Regras Fundamentais para Qualquer Agente de IA

1. **Respeitar o Padrão Repository por Convenção:**
   - Métodos obrigatórios: `save(objeto)`, `get_all()`, `find_by_id(id)`, `update(objeto)`, `delete(id)`.
   - A assinatura e os retornos dos métodos devem ser idênticos entre os repositórios em memória e os repositórios SQL.
2. **Proibido o uso de ORMs:**
   - O projeto visa aprendizado didático e avaliação de SQL puro (DDL e DML nativos). Não introduza ORMs como SQLAlchemy, Peewee ou Django ORM.
3. **Respeitar as Fases do Projeto:**
   - **Fase 1:** Persistência em memória (listas/dicionários encapsulados em `repositories/`).
   - **Fase 2:** Persistência em banco relacional via SQL (`database/schema.sql` e repositórios SQL).
   - O `main.py` só deve trocar a instanciação do repositório, mantendo o restante do fluxo inalterado.
4. **Robustez na CLI:**
   - Nenhuma entrada inválida do usuário pode causar encerramento não tratado (`traceback`/crash) da aplicação. Utilize blocos `try/except` defensivos e menus com loops seguros.
5. **Boas Práticas de Código:**
   - Seguir rigorosamente a **PEP 8**: `snake_case` para variáveis/funções/módulos, `PascalCase` para classes.

