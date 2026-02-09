# Dashboard de Análise de Salários na Área de Dados

Este projeto consiste em uma aplicação interativa desenvolvida para explorar e analisar dados salariais globais na área de tecnologia, com foco em funções de dados. A ferramenta permite que profissionais e recrutadores entendam as tendências de remuneração baseadas em diversos fatores de mercado.

Acesse o dashboard online: [https://degan-imersao-dados-alura.streamlit.app/](https://degan-imersao-dados-alura.streamlit.app/)

## Descrição do Projeto

O dashboard processa dados salariais convertidos para **USD** (Dólar Americano), permitindo uma base de comparação uniforme entre diferentes regiões. O usuário pode filtrar as informações por **Ano**, **Senioridade**, **Tipo de Contrato** e **Tamanho da Empresa**, gerando uma visualização personalizada e dinâmica.

## Funcionalidades Principais

- **Métricas de Desempenho (KPIs)**: Visualização instantânea do salário médio, salário máximo e o cargo com maior volume de dados.
- **Análise por Cargo**: Ranking dos 10 cargos com as maiores médias salariais.
- **Distribuição Salarial**: Histograma detalhado mostrando a concentração de rendimentos anuais.
- **Modelos de Trabalho**: Gráfico de setores indicando a proporção entre regime remoto, presencial ou híbrido.
- **Visão Geográfica**: Mapa global destacando a média salarial para o cargo de Cientista de Dados em diferentes países.

## Tecnologias Utilizadas

- **Python**: Linguagem base para o processamento lógico.
- **Streamlit**: Framework utilizado para a criação da interface web e deploy.
- **Pandas**: Biblioteca essencial para a manipulação e limpeza dos dados.
- **Plotly Express**: Utilizado para a geração de gráficos interativos e mapas.

## Principais Insights

- **Variação por Senioridade**: Existe uma progressão clara nos valores conforme o nível de experiência, com cargos de nível Sênior e Direção apresentando as maiores variações positivas.
- **Predominância do Remoto**: Uma fatia significativa das vagas de alta remuneração está concentrada em regimes de trabalho remoto ou híbrido, refletindo a flexibilidade do setor.
- **Concentração Salarial**: A maior parte dos salários está concentrada em faixas intermediárias, mas há outliers significativos em cargos especializados e em determinadas localizações geográficas.
- **Geografia do Cientista de Dados**: Países com hubs tecnológicos consolidados apresentam as médias salariais mais competitivas para a função de Cientista de Dados.

## Como Executar Localmente

1. Certifique-se de ter o **Python** instalado.
2. Instale as dependências necessárias:
   `pip install -r requirements.txt`
3. Execute a aplicação:
   `streamlit run app.py`
