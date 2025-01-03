# Analisador de Notícias Financeiras

Este projeto é um aplicativo interativo desenvolvido com **Streamlit**, que busca notícias financeiras do site [InfoMoney](https://www.infomoney.com.br/), analisa o sentimento das postagens utilizando técnicas de NLP e apresenta análises visuais.

## **Funcionalidades**

- **Rastreamento de notícias:**
- Automação para coletar noticías de sites financeiros utilizando Selenium e BeautifulSoup.
- **Análise de Sentimento:**
  - Classificação das noticías em positivas, negativas ou neutras com modelos baseados em `transformers` ou `nltk`.
- **Filtros Personalizados:**
  - Filtragem de dados por setor, palavra-chave ou período.
- **Visualização Interativa:**
  - Gráficos de sentimento ao longo do tempo.
  - Word clouds para destacar termos mais frequentes.
- **Geração de Relatórios:**
  - Exportação de análises em PDF ou Excel.

