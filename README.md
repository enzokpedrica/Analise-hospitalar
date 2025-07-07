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
### Visão Geral
![Dashboard Geral](Imagens/modelagem_banco.png)

## 💼 Perguntas de Negócio Respondidas

O painel do Power BI foi desenvolvido para responder a perguntas estratégicas para a gestão da Inovamed, como:

✅ **Qual mês que mais faturou?**  
↳ Excelente para análise de sazonalidade e metas mensais.

✅ **Qual o tipo de tratamento que mais gera receita?**  
↳ Ajuda na definição de foco comercial e estratégico.

✅ **Quais médicos geram mais receitas?**  
↳ Métrica ótima para gestão de desempenho individual.

✅ **Quem são os pacientes que mais geram receitas?**  
↳ Base perfeita para estratégias de retenção e relacionamento VIP.

✅ **Qual plano de saúde gera maior receita?**  
↳ Ajuda na negociação com operadoras e análise de lucratividade.

✅ **Qual a faixa etária dos meus pacientes?**  
↳ Gera insights sobre o público-alvo, possibilitando campanhas personalizadas.

🔹 **Com os pacientes que não aparecem, quais os motivos?**  
💬 Apesar da ausência de uma coluna direta com o motivo, a análise de faltas foi feita com base em dados indiretos. As perguntas exploradas foram:

- Qual a **taxa de não comparecimento** por perfil de paciente (plano, idade, tratamento)?
- Em quais **dias da semana/horários** as faltas são mais comuns?

📌 *Sugestão futura*: apoiar o setor de SAC com pesquisas de satisfação para investigar possíveis objeções — como dúvidas sobre o tratamento, percepção de preço ou insegurança.

---

## 🧠 Insights Estratégicos

- Pacientes com plano de saúde privado geram maior faturamento médio.
- O tratamento **X-Ray** representa a maior fatia da receita total.
- O médico Dr. João Silva realiza o maior número de atendimentos, mas o Dr. Pedro Rocha tem o **maior ticket médio** por paciente.
- As faltas ocorrem com mais frequência nas segundas-feiras e no período da manhã.

---

## 📌 Possibilidades Futuras

- Implantar modelo preditivo para prever faltas.
- Integrar com ferramentas de envio de lembretes para reduzir ausências.
- Criar APIs para alimentar o Power BI com dados em tempo real.

---

## 🧑‍💼 Autor

**Enzo Koyano Pedriça**  
💼 Assistente de P&D na Indústria Linea Brasil  
🚀 Em transição para Engenharia de Dados com foco em aplicações reais de BI e Analytics  
📫 [LinkedIn](https://www.linkedin.com) | [Substack](https://www.substack.com)

---

> 🔎 *Este projeto utiliza dados fictícios, gerados para fins educacionais. Nenhuma informação real de pacientes foi utilizada.*

