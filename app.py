import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Inteligência Salarial",
    layout="wide",
)

# --- Estilização Customizada ---
st.markdown("""
<style>
    /* Glow Atmosférico no Fundo */
    .stApp {
        background: radial-gradient(circle at 20% 30%, rgba(57, 255, 20, 0.08) 0%, rgba(14, 17, 23, 0) 50%),
                    radial-gradient(circle at 80% 70%, rgba(0, 255, 255, 0.08) 0%, rgba(14, 17, 23, 0) 50%);
        background-color: #0e1117;
    }
    
    /* Estilo dos cards de métricas */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #39FF14; /* Verde Neon */
    }
    [data-testid="stMetricLabel"] {
        font-size: 1rem;
        color: #00FFFF; /* Ciano Neon */
    }
    div[data-testid="stMetric"] {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 18px;
        border-left: 4px solid #39FF14;
        box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.3);
    }
    /* Títulos em Neon */
    h1, h2, h3 {
        color: #00FFFF !important;
        text-shadow: 1px 1px 5px rgba(0, 255, 255, 0.5);
    }
    /* Ajuste da Sidebar (Glassmorphism) */
    [data-testid="stSidebar"] {
        background-color: rgba(14, 17, 23, 0.7);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(0, 255, 255, 0.1);
    }
    
    /* Esconder menu de troca de tema e header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Configuração de Cores Plotly ---
NEON_GREEN = "#39FF14"
NEON_CYAN = "#00FFFF"
COLOR_PALETTE = [NEON_GREEN, NEON_CYAN, "#7DF9FF", "#50C878", "#AFE1AF"]

# --- Carregamento dos dados ---
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

df = load_data()

# --- Barra Lateral (Filtros) ---
# Centralizando a imagem usando colunas
col_side1, col_side2, col_side3 = st.sidebar.columns([1, 1, 1])
with col_side2:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)

# Centralizando o título
st.sidebar.markdown("<h1 style='text-align: center;'>Filtros</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Selecione os Anos", anos_disponiveis, default=anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Nível de Experiência", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Modelo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Porte da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

st.sidebar.markdown("---")
st.sidebar.info("Dashboard atualizado com tendências de mercado e remuneração em USD.")

# --- Filtragem do DataFrame ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal ---
st.title("Dashboard de Inteligência Salarial")
st.markdown("Análise avançada dos rendimentos na área de dados com foco em tendências globais.")

# --- Métricas Principais (KPIs) ---
if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Média Salarial", f"${salario_medio:,.0f}")
col2.metric("Salário Topo", f"${salario_maximo:,.0f}")
col3.metric("Amostragem", f"{total_registros:,}")
col4.metric("Cargo Dominante", cargo_mais_frequente)

st.markdown("<br>", unsafe_allow_html=True)

# --- Organização em Abas ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Visão Geral", "📈 Distribuição & Senioridade", "🌍 Análise Geográfica", "📄 Dados Brutos"])

with tab1:
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        if not df_filtrado.empty:
            top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
            fig = px.bar(
                top_cargos,
                x='usd',
                y='cargo',
                orientation='h',
                title="Top 10 Cargos (Média USD)",
                template="plotly_dark",
                color_discrete_sequence=[NEON_GREEN]
            )
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
    
    with col_graf2:
        if not df_filtrado.empty:
            remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
            remoto_contagem.columns = ['tipo', 'qtd']
            fig = px.pie(
                remoto_contagem,
                names='tipo',
                values='qtd',
                title='Distribuição de Remoto/Híbrido',
                hole=0.6,
                template="plotly_dark",
                color_discrete_sequence=[NEON_CYAN, NEON_GREEN, "#FF6D2D"]
            )
            fig.update_traces(
                textposition='inside', 
                textinfo='percent+label',
                insidetextfont=dict(size=12, color="white", family="Arial", weight="bold", shadow="auto")
            )
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    col_graf3, col_graf4 = st.columns(2)
    
    with col_graf3:
        if not df_filtrado.empty:
            fig = px.histogram(
                df_filtrado,
                x='usd',
                nbins=40,
                title="Curva de Distribuição Salarial",
                template="plotly_dark",
                color_discrete_sequence=[NEON_CYAN]
            )
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

    with col_graf4:
        if not df_filtrado.empty:
            fig = px.box(
                df_filtrado,
                x='senioridade',
                y='usd',
                title="Variação Salarial por Senioridade",
                template="plotly_dark",
                color_discrete_sequence=[NEON_GREEN]
            )
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

with tab3:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
            fig = px.choropleth(
                media_ds_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale=[[0, '#003333'], [0.5, NEON_CYAN], [1, NEON_GREEN]],
                title='Mapa de Calor: Média de Cientistas de Dados',
                template="plotly_dark"
            )
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Filtre pelo cargo 'Data Scientist' para ver a análise geográfica.")

with tab4:
    st.subheader("Exploração de Dados")
    st.dataframe(df_filtrado, use_container_width=True)
