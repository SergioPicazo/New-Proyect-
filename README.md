# Análisis de Vehículos en Estados Unidos

## Descripción del Proyecto

Esta aplicación web interactiva permite realizar un análisis exploratorio de datos sobre vehículos en Estados Unidos. La aplicación está desarrollada utilizando Streamlit y Plotly Express para proporcionar visualizaciones dinámicas e interactivas.

## Funcionalidades

La aplicación web proporciona las siguientes características:

### 📊 Visualización de Datos
- **Información del Dataset**: Muestra estadísticas básicas como el número total de vehículos y columnas
- **Vista Previa**: Displays las primeras 5 filas del conjunto de datos para una vista rápida

### 📈 Visualizaciones Interactivas
- **Histograma de Precios**: Casilla de verificación para mostrar/ocultar la distribución de precios de vehículos
- **Gráfico de Dispersión**: Casilla de verificación para mostrar/ocultar la relación entre año del vehículo y precio

### 🎛️ Controles Interactivos
- Casillas de verificación que permiten al usuario seleccionar qué visualizaciones desea ver
- Interfaz intuitiva y fácil de usar
- Gráficos responsivos que se adaptan al tamaño de la pantalla

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Streamlit**: Framework para crear aplicaciones web interactivas
- **Pandas**: Manipulación y análisis de datos
- **Plotly Express**: Creación de gráficos interactivos

## Estructura del Proyecto

```
proyecto/
├── app.py                      # Aplicación principal de Streamlit
├── vehicles_us.csv            # Conjunto de datos de vehículos
├── requirements.txt           # Dependencias del proyecto
├── notebooks/
│   └── EDA.ipynb             # Análisis exploratorio de datos
└── README.md                 # Este archivo
```

## Instalación y Uso

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

3. **Abrir en el navegador**: La aplicación se abrirá automáticamente en `http://localhost:8501`

## Uso de la Aplicación

1. Al abrir la aplicación, verás información básica sobre el conjunto de datos
2. Utiliza las casillas de verificación para seleccionar qué visualizaciones mostrar:
   - Marca "Mostrar histograma de precios" para ver la distribución de precios
   - Marca "Mostrar gráfico de dispersión" para ver la relación año vs precio
3. Los gráficos aparecerán dinámicamente basados en tu selección

## Conjunto de Datos

El proyecto utiliza el archivo `vehicles_us.csv` que contiene información sobre vehículos en Estados Unidos, incluyendo variables como precio, año del modelo, odómetro, y más características relevantes para el análisis.
