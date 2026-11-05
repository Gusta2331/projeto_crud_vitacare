# AGENTS.md

Instruções e diretrizes de desenvolvimento para Agentes de IA neste repositório.

## 🧭 Documentação do Projeto para Agentes

Todas as informações detalhadas sobre arquitetura, convenções, padrão Repository e modelagem de domínio estão organizadas na pasta [`.ai/`](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/README.md):

- [`.ai/README.md`](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/README.md) - Visão geral e regras essenciais do projeto.
- [`.ai/architecture.md`](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/architecture.md) - Padrão Repository, separação de camadas e fases do projeto.
- [`.ai/conventions.md`](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/conventions.md) - Padrões de código PEP 8 e regras de robustez/tratamento de erros na CLI.
- [`.ai/domain-guide.md`](file:///Users/renan.fb.dantas/Desktop/Projetos/unifan/projeto_crud/.ai/domain-guide.md) - Requisitos das entidades (1:N, N:N associativa), SQL e relatórios analíticos.

## ⚡ Regras Rápidas

1. **Padrão Repository por Convenção:** Nomes de métodos idênticos para repositórios em memória e em banco (`save`, `get_all`, `find_by_id`, `update`, `delete`).
2. **Sem ORM:** Usar SQL nativo com queries parametrizadas (ex.: `sqlite3`).
3. **CLI Resiliente:** Tratamento defensivo com `try/except` para impedir qualquer encerramento inesperado decorrente de entradas incorretas.
4. **PEP 8:** Nomes em `snake_case` para funções/variáveis e `PascalCase` para classes.

