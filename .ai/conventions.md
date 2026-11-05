# Convenções de Código e Boas Práticas

Este documento orienta os agentes de IA sobre as normas de codificação, tratamento de erros e integridade do projeto.

---

## 🐍 Padrões de Código Python (PEP 8)

- **Nomenclatura:**
  - Classes: `PascalCase` (ex.: `Cliente`, `VeiculoRepositoryMemory`).
  - Funções e métodos: `snake_case` (ex.: `find_by_id`, `calcular_total`).
  - Variáveis e instâncias: `snake_case` (ex.: `cliente_repo`, `lista_veiculos`).
  - Constantes: `UPPER_SNAKE_CASE` (ex.: `DATABASE_PATH`, `MAX_ATTEMPTS`).
  - Arquivos e módulos: `snake_case` (ex.: `cliente_database_repository.py`).
- **Imports:** Organizados no início do arquivo (biblioteca padrão primeiro, bibliotecas de terceiros depois, e módulos locais por fim).
- **Type Hints:** Recomenda-se o uso de anotações de tipo quando possível (ex.: `def find_by_id(self, id_registro: int) -> Optional[Cliente]:`).

---

## 🛡️ Robustez e Tratamento de Exceções (Crítico para Avaliação)

A aplicação CLI **nunca pode crashar** ou exibir tracebacks não tratados para o usuário final.

### Diretrizes:
1. **Entradas Numéricas e Menus:**
   - Sempre encapsular conversões `int(input(...))` ou `float(input(...))` em blocos `try/except ValueError` com laços de repetição até que uma entrada válida seja fornecida.
2. **Entradas de Texto:**
   - Validar strings vazias ou apenas espaços com `.strip()`.
3. **Erros de Banco de Dados:**
   - No SQL, tratar exceções como `sqlite3.IntegrityError` (ex.: violação de chave única ou estrangeira) emitindo mensagem clara e acionando `rollback` da transação.
4. **Mensagens ao Usuário:**
   - Mensagens de erro devem ser amigáveis e claras, indicando o que deve ser corrigido sem expor detalhes internos do sistema.

---

## 📦 Gestão de Dependências

- Priorizar sempre que possível a **biblioteca padrão do Python** (`sqlite3`, `datetime`, `re`, `sys`, `os`, `pathlib`).
- Manter o `requirements.txt` enxuto, registrando apenas bibliotecas estritamente necessárias caso sejam solicitadas.

