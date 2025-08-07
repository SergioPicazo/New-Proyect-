import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos US", layout="wide")

# Título principal
st.title("Análisis de Vehículos en Estados Unidos")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

# Cargar el dataset
df = load_data()

# Mostrar información básica del dataset
st.header("Información del Dataset")
st.write(f"Total de vehículos: {len(df)}")
st.write(f"Número de columnas: {len(df.columns)}")

# Mostrar las primeras filas
st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())

# Visualizaciones
st.header("Visualizaciones Interactivas")

# Casilla de verificación para generar histograma
hist_checkbox = st.checkbox("Mostrar histograma de precios")
if hist_checkbox:
    st.write("Generando histograma de distribución de precios...")
    if 'price' in df.columns:
        fig_hist = px.histogram(df, x='price', title='Distribución de Precios de Vehículos')
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.error("La columna 'price' no se encuentra en el dataset")

# Casilla de verificación para generar gráfico de dispersión
scatter_checkbox = st.checkbox("Mostrar gráfico de dispersión")
if scatter_checkbox:
    st.write("Generando gráfico de dispersión año vs precio...")
    if 'year' in df.columns and 'price' in df.columns:
        fig_scatter = px.scatter(df, x='year', y='price', title='Relación entre Año y Precio')
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.error("Las columnas 'year' y/o 'price' no se encuentran en el dataset")
