# Guia de Domínio e Requisitos de Dados

Este documento orienta os agentes de IA sobre as regras acadêmicas exigidas para o modelo de dados e relatórios do projeto.

---

## 📊 Regras do Modelo de Domínio

1. **Quantidade Mínima de Entidades:**
   - O projeto deve contemplar **pelo menos 3 entidades** correlacionadas.
2. **Classificação das Entidades:**
   - Devem coexistir entidades fortes e fracas.
3. **Relacionamentos Obrigatórios:**
   - Relacionamento de cardinalidade $1:N$.
   - Pelo menos um relacionamento de cardinalidade $N:N$, obrigatoriamente resolvido por uma **Entidade Associativa** que possua atributos próprios (ex.: data da operação, quantidade, valor unitário ou status).
4. **Chaves Identificadoras:**
   - Chaves Primárias (PK) e Chaves Estrangeiras (FK) expressas e consistentes em código e no `schema.sql`.

---

## 🗄️ Requisitos de SQL (Fase 2)

### DDL (`database/schema.sql`):
- Deve conter instruções `CREATE TABLE` completas para todas as tabelas.
- Deve incluir constraints explícitas:
  - `PRIMARY KEY`
  - `FOREIGN KEY` com `REFERENCES` e integridade referencial ativa
  - `NOT NULL` para campos mandatórios
  - `UNIQUE` para identificadores únicos (ex.: CPF, e-mail, placa)
  - `CHECK` para validações de domínio (ex.: valores monetários $> 0$, status permitidos)

### DML e Relatórios Analíticos:
- Os repositórios SQL devem implementar comandos parametrizados (`?` para SQLite) para evitar SQL Injection.
- O sistema deve implementar **no mínimo 2 relatórios analíticos** utilizando:
  - `JOIN` entre as entidades relacionadas;
  - Funções agregadoras: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`;
  - Agrupamentos via `GROUP BY` e opcionalmente `HAVING` ou ordenação `ORDER BY`.

