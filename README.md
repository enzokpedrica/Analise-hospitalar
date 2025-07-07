# 🏥 Inovamed - Healthcare Analytics
---

## 📊 Tecnologias Utilizadas

- Python (ETL e pré-processamento)
- Pandas
- SQL Server (modelagem relacional + criação de views)
- Power BI (dashboards interativos)
- Git/GitHub (versionamento e portfólio)

---

## 🧩 Estrutura dos Dados

O projeto trabalha com 5 datasets principais que foram baixados do KAGLE, são estes:

- **patients.csv** – Dados demográficos e de cadastro de pacientes
- **doctors.csv** – Especialidades e experiência médica
- **appointments.csv** – Agendamentos, status e motivos das visitas
- **treatments.csv** – Tipos de tratamento, custos e datas
- **billing.csv** – Faturamento, métodos de pagamento e status

Esses arquivos foram tratados, relacionados e inseridos no SQL Server. Views otimizadas foram criadas para facilitar a análise via Power BI.

---

## 🌱 Passo a Passo do Projeto

- Após o dowload dos nossos datasets, precisamos entender nossas estruturas de dados, onde vamos criar relacionamentos, realizar Joins e seguir para a análise

### Modelagem de Dados
- Esse passo da modelagem é primordial para você entender os meus dados e criar suas tabelas de relacionamento. Site utilizado: **dbdigram.io**
![Modelagem Banco](Imagens/modelagem_banco.PNG)

### Processo de ETL
- Após eu ter o mapeamento dos meus dados chegou a hora de executar o processo de ETL
- Eu optei por usar a **Arquitetura Medallion**
- O ponto inicial foi deixar os datasets na camada BRONZE
- Logo em seguida foi executado uma pipeline de dados onde aplicava o processo de **TRANSFORMAÇÃO** dos dados
  - O arquivo da transformação .ipynb se encontra no repositório, mas em resumo foram alterados: Tipo de dados, criação de novas colunas com extração de valores
  - Após a transformação os datasets já foram salvos na camada PRATA
- Com os dados na camada PRATA, chegou o momento de fazer o **LOAD** para nosso banco de dados

### Load para o Banco de Dados (SQL Server)
- No SQL Server foi executado Queries para a criação do database que ficariam armazenados as tabelas
- Com os nossos dados mapeados e modelados foi executado Queries para a criação das tabelas
- Após a criação das tabelas precisamos realizar a conexão Python -> SQL Server
  - Com conexão bem sucessida foi hora de executar nossa função e realizar o LOAD para nosso banco de dados
![Queries](Imagens/Querydecriacaotabelas.PNG)

### Dados no SQL Server
- Com os dados inseridos no nosso banco de dados, chegou a hora de criarmos views para facilitar nossa análise no PowerBI
- Views criadas, agora partiu PowerBI

### Conexão PowerBI
- Realizado a conexão entre PowerBI -> SQL Server
- Carregamento das views, o carregamento foi direto porque os dados já se encontravam "LIMPOS e FORMATADOS"

 ### Criação de Dashboard para Visualização com PowerBI
- O Dashboard foi divido em 3 páginas onde abordamos: Visão Geral, Financeiro e Atendimentos
- 📄 Veja o dashboard completo em PDF:
![Dashboard Geral](Imagens/dash_hospital.pdf)

---

## 💼 Perguntas de Negócio Respondidas

O painel do Power BI foi desenvolvido para responder a perguntas estratégicas para a gestão da Inovamed, como:

✅ **Qual mês que mais faturou?**  
↳ O mês com o maior faturamento foi Abril com R$ 64.271,54.

✅ **Qual o tipo de tratamento que mais gera receita?**  
↳ O tipo de tratamento que mais gera receita é do tipo: Chemoterapy (Quimioterapia), representando 23,38%.

✅ **Quais médicos geram mais receitas?**  
↳ Os 3 médicos mais "valiosos" são: Dra Sarah Taylor, Dr Alex Davies, Dr David Taylor.

✅ **Quem são os pacientes que mais geram receitas?**  
↳ Os 3 pacientes que mais geram receitas são: Michael Taylor, Michael Wilson e Laura Davis.

✅ **Qual plano de saúde gera maior receita?**  
↳ O plano que representa a maior porcentagem de receita gerada é o HealIndia com 33,34%.

✅ **Qual a faixa etária dos meus pacientes?**  
↳ A média da faixa etária esta em 45 anos.
 
✅ **Com os pacientes que não aparecem, quais os motivos?**  
💬 Apesar da ausência de uma coluna direta com o motivo, a estratégia adotado poderia ser envolver o setor de SAC, com isso criar uma nova tabela de dados onde estariam esses dados.
📌 *Sugestão futura*: apoiar o setor de SAC com pesquisas de satisfação para investigar possíveis objeções — como dúvidas sobre o tratamento, percepção de preço ou insegurança.

---

> 🔎 *Este projeto utiliza dados fictícios, gerados para fins educacionais. Nenhuma informação real de pacientes foi utilizada.*

