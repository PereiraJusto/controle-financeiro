# PROJECT_CONTEXT.md

## 1. Visão Geral do Projeto

O projeto “Controle Financeiro” tem como objetivo registrar, organizar e analisar eventos financeiros reais de forma estruturada, clara e auditável, priorizando a fidelidade aos fatos do mundo real.

O sistema é concebido para separar explicitamente dados brutos de dados derivados, evitando o acoplamento entre registro de fatos, regras de negócio e visualizações ou indicadores.

O foco inicial do projeto é o controle financeiro pessoal e familiar, com uma evolução planejada e consciente, evitando antecipações técnicas ou funcionais.


## 2. Princípios e Regras Estruturais

Princípios fundamentais do projeto:

- O domínio do problema precede qualquer decisão técnica.
- Fatos do mundo real são a fonte primária da verdade do sistema.
- Dados brutos nunca são sobrescritos por dados derivados.
- Indicadores, totais e resumos não são entidades persistidas.
- O sistema evolui por fases com escopo fechado e explícito.
- Não há antecipação de funcionalidades, regras ou tecnologias.
- Cada fase registrada torna-se parte imutável da história do projeto.


## 3. Escopo Funcional Atual

O sistema possui atualmente apenas infraestrutura técnica básica validada, sem funcionalidades de domínio implementadas.

Escopo funcional existente:
- Backend exposto exclusivamente como API
- Frontend funcional em ambiente de desenvolvimento
- Comunicação HTTP mínima validada entre frontend e backend
- Endpoint de sanidade para verificação de conectividade

Não existem ainda funcionalidades de domínio, regras de negócio ou operações financeiras implementadas.

## 4. Arquitetura Conceitual

A arquitetura atual do sistema é composta por duas camadas principais, ainda sem acoplamento ao domínio do negócio:

- Backend:
  - Responsável exclusivamente por expor uma API HTTP
  - Não realiza renderização de interface
  - Não contém regras de negócio ou modelos de domínio

- Frontend:
  - Responsável apenas pela interface e consumo da API
  - Comunicação realizada via requisições HTTP diretas

A separação entre backend e frontend é explícita e deliberada, preparando o terreno para a introdução futura do domínio sem impacto estrutural.

## 5. Linha do Tempo das Fases

### Fase 0 – Entendimento do Domínio

**Objetivo**  
Compreender o domínio do projeto “Controle Financeiro” de forma independente de qualquer solução técnica, identificando claramente entidades, eventos financeiros, dados brutos, dados derivados, vocabulário do domínio e os limites explícitos da primeira versão do sistema.

**Escopo Deliberado**  
- Análise conceitual do domínio financeiro familiar  
- Identificação de fatos do mundo real relevantes para o sistema  
- Diferenciação entre dados brutos, dados derivados e regras de negócio  
- Definição de limites claros da V1 do domínio  
- Estabelecimento de convenções conceituais e vocabulário consistente  

**Fora de Escopo**  
- Qualquer decisão técnica ou de implementação  
- Criação de código, modelos físicos ou estruturas de projeto  
- Definição de APIs, interfaces ou backend  
- Projeções financeiras futuras, metas ou simulações  
- Integrações externas (bancos, cartões, etc.)  

**Estado Inicial do Projeto**  
Antes do início desta fase, o projeto apresentava:
- Uma planilha de controle financeiro familiar em uso  
- Conceitos implícitos misturados entre fatos do mundo real, categorias, indicadores e operações da planilha  
- Ausência de uma linguagem de domínio formalizada  
- Ausência de separação clara entre dados brutos, dados derivados e regras de negócio  
- Inexistência de documentação oficial descrevendo o domínio do sistema  

**Decisões Tomadas**  
- O domínio financeiro será modelado a partir de fatos do mundo real, e não a partir da estrutura da planilha existente  
- Indicadores, totais, saldos e resumos não são tratados como entidades nem como dados persistidos  
- Eventos financeiros são definidos como fatos que acontecem no tempo e alteram de forma irreversível o estado financeiro  
- O sistema será orientado a eventos e transações reais, não a previsões ou projeções futuras na V1  

**Convenções Definidas**  
- Separação estrita entre:
  - Entidades do domínio  
  - Eventos financeiros  
  - Dados brutos (fonte da verdade)  
  - Dados derivados (cálculos)  
- Uso de vocabulário de domínio consistente e não ambíguo  
- Proibição explícita de tratar categorias, resumos ou indicadores como entidades  
- A V1 do domínio trabalha exclusivamente com fatos passados e registrados  

**Resultado Final**  
- Domínio financeiro compreendido e delimitado em nível conceitual  
- Regras claras sobre o que constitui dado persistido versus dado derivado  
- Base conceitual estabelecida para evolução segura das próximas fases  

**Status**  
Concluída

### Fase 1 – Setup Inicial de Backend e Frontend

**Objetivo**  
Estabelecer a infraestrutura mínima do sistema “Controle Financeiro”, criando o setup inicial do backend e do frontend, garantindo que ambos subam sem erro e que exista comunicação mínima funcional entre frontend e backend, sem antecipar domínio, regras de negócio ou autenticação.

**Escopo Deliberado**  
- Criação da estrutura inicial de backend e frontend  
- Configuração de um backend exposto exclusivamente como API  
- Configuração de um frontend funcional em ambiente de desenvolvimento  
- Comunicação mínima funcional via HTTP entre frontend e backend  
- Validação do funcionamento da infraestrutura básica do sistema  

**Fora de Escopo**  
- Modelagem de domínio  
- Criação de models, regras de negócio ou CRUDs  
- Autenticação e autorização  
- Persistência de dados estruturada além do banco local inicial  
- Estilização visual avançada  
- Testes automatizados  
- Pipeline de build, deploy ou integrações externas  

**Estado Inicial do Projeto**  
Antes do início desta fase:
- Não existia projeto estruturado  
- Não havia backend, frontend ou repositório Git  
- Não existia comunicação entre camadas do sistema  

**Decisões Tomadas**  
- Separação explícita entre backend e frontend em estruturas distintas  
- Backend desenvolvido utilizando Django com Django REST Framework  
- Utilização de SQLite apenas para viabilizar o setup inicial  
- Frontend desenvolvido com React utilizando Vite, priorizando simplicidade e rapidez no ambiente de desenvolvimento  
- Criação de um endpoint de sanidade no backend para validação da comunicação HTTP  
- Comunicação frontend ↔ backend realizada via requisição HTTP direta a um endpoint REST  

**Convenções Definidas**  
- Backend tratado exclusivamente como API, sem renderização de HTML  
- Endpoints versionados sob o prefixo `/api`  
- Uso de ambiente virtual isolado para dependências Python  
- Uso de `.gitignore` para exclusão de ambientes virtuais, dependências e artefatos locais  
- Commit inicial representando uma infraestrutura funcional mínima  

**Resultado Final**  
- Infraestrutura básica de backend e frontend criada  
- Backend e frontend executando sem erros em ambiente de desenvolvimento  
- Comunicação mínima funcional entre frontend e backend validada  
- Base técnica estabelecida para início da modelagem de domínio  

**Status**  
Concluída


## 6. Registro de Decisões Importantes

Nenhuma decisão arquitetural transversal foi registrada fora do escopo das fases concluídas até o momento.

As decisões tomadas encontram-se documentadas dentro das respectivas fases.


## 7. Glossário do Domínio

O glossário do domínio será construído a partir da Fase 2, após a definição explícita das entidades, eventos financeiros e conceitos centrais do sistema.

Até o momento, não há termos formalmente consolidados.


## 8. Estado Atual do Projeto

Status geral do projeto:
- Fase 0 – Entendimento do Domínio: Concluída
- Fase 1 – Setup Inicial de Backend e Frontend: Concluída

Situação atual:
- Domínio conceitual compreendido e delimitado
- Infraestrutura mínima de backend e frontend funcional
- Comunicação entre camadas validada
- Nenhuma funcionalidade de domínio implementada

Próximo passo previsto:
- Início da Fase 2, com foco exclusivo na modelagem do domínio, eventos e regras de negócio, sem decisões de implementação antecipadas.
