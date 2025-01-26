# Analisador de Notícias Financeiras

Este projeto é um aplicativo interativo desenvolvido com **Streamlit**, que busca notícias financeiras do site [CoinTeleGraph](https://br.cointelegraph.com/), analisa o sentimento das postagens utilizando técnicas de NLP e apresenta análises visuais.

## **Funcionalidades**

- **Rastreamento de notícias:**
- Automação para coletar noticías de sites financeiros utilizando BeautifulSoup.
- **Análise de Sentimento:**
  - Classificação das noticías com modelos baseados em `nltk`.
- **Sumarização:**
  - Resumir as notíticas com o modelo de sumariização `facebook/bart-large-cnn`.
- **Visualização Interativa:**
  - Gráficos de sentimento ao longo do tempo.
  - Word clouds para destacar termos mais frequentes.
- **Geração de Relatórios:**
  - Exportação de análises em PDF ou Excel.

