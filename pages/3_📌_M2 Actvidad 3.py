import streamlit as st
import pandas as pd
import datetime
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

st.subheader("Actividad 1: Filtrado con pandas en google colab")

st.markdown(
    "<p style='color:blue;'>Haz clic en el siguiente enlace:</p>",
    unsafe_allow_html=True,
)


st.code(
   " https://colab.research.google.com/drive/1fZXJXNcNw9o-FRCIUSYJL4HcUNOPvagS?usp=sharing"
)

st.subheader(
    "Actividad 2: Cree una app de filtros dinámicos en Streamlit"


)

st.header("Solución2")


def cargar_datos():
    hoy = datetime.date.today()
    anios = np.random.randint(1950, 2005, size=10)
    meses = np.random.randint(1, 13, size=10)
    dias = np.random.randint(1, 29, size=10)

    fechas_nacimiento = [datetime.date(year, month, day) for year, month, day in zip(anios, meses, dias)]
    acceso = np.random.choice([True, False], size=10)
    ingresos = [2500000, 6000000, 1800000, np.nan, 3200000, np.nan, 11000000, 2800000, 7500000, 5000000]
    municipios_ejemplo = np.random.choice(['Medellín', 'Bogotá', 'Cali', 'Barranquilla'], size=10)
    ocupaciones_ejemplo = np.random.choice(['Estudiante', 'Docente', 'Comerciante', 'Ingeniero', 'Médico'], size=10)
    tipo_vivienda_ejemplo = np.random.choice(['Arriendo', 'Propia', 'Familiar'], size=10)
    nombres_ejemplo = ['Ana', 'Bryan', 'Carlos', 'Diana', 'Juan', 'Lina',
                        'jorge', 'andrea', 'maria', 'Juanita']
    edades_ejemplo = np.random.randint(18, 65, size=10)

    data = {
        'nombre_completo': nombres_ejemplo,
        'edad': edades_ejemplo,
        'municipio': municipios_ejemplo,
        'ingreso_mensual': ingresos,
        'ocupacion': ocupaciones_ejemplo,
        'tipo_vivienda': tipo_vivienda_ejemplo,
        'fecha_nacimiento': fechas_nacimiento,
        'acceso_internet': acceso
    }
    df = pd.DataFrame(data)
    return df

df_original = cargar_datos()
df_filtrado = df_original.copy()


st.sidebar.header("Filtros Dinámicos")

# 1  rango de edad (between)
filtrar_edad = st.sidebar.checkbox("Filtrar por rango de edad", key="filtrar_edad")
if filtrar_edad:
    min_edad, max_edad = st.sidebar.slider("Rango de edad", 15, 75, (20, 60), key="slider_edad")
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2 municipios isin
filtrar_municipio = st.sidebar.checkbox("Filtrar por municipios", key="filtrar_municipio")
municipios_disponibles = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida']
if filtrar_municipio:
    municipios_seleccionados = st.sidebar.multiselect("Seleccionar municipios", municipios_disponibles, key="multiselect_municipios")
    if municipios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

# 3 ingreso mensual mínimo 
filtrar_ingreso = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo", key="filtrar_ingreso")
if filtrar_ingreso:
    ingreso_minimo = st.sidebar.slider("Ingreso mínimo (COP)", 800000, 12000000, 3000000, key="slider_ingreso")
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

# 4 ocupación isin
filtrar_ocupacion = st.sidebar.checkbox("Filtrar por ocupación", key="filtrar_ocupacion")
ocupaciones_disponibles = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
if filtrar_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect("Seleccionar ocupaciones", ocupaciones_disponibles, key="multiselect_ocupaciones")
    if ocupaciones_seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

# 5  vivienda no propia
filtrar_no_propia = st.sidebar.checkbox("Filtrar personas sin vivienda propia", key="filtrar_no_propia")
if filtrar_no_propia:
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6 nombres str.contains
filtrar_nombre = st.sidebar.checkbox("Filtrar por nombre", key="filtrar_nombre")
if filtrar_nombre:
    texto_nombre = st.sidebar.text_input("Ingresar texto a buscar en el nombre", key="text_nombre")
    if texto_nombre:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto_nombre, case=False, na=False)]

# 7  año de nacimiento especifico (fechas)
filtrar_anio_nacimiento = st.sidebar.checkbox("Filtrar por año de nacimiento", key="filtrar_anio_nacimiento")
if filtrar_anio_nacimiento:
    año_actual = datetime.datetime.now().year
    anios_disponibles = list(range(año_actual - 75, año_actual - 14))
    anio_seleccionado = st.sidebar.selectbox("Seleccionar año de nacimiento", anios_disponibles, key="selectbox_anio")
    df_filtrado['anio_nacimiento'] = pd.to_datetime(df_filtrado['fecha_nacimiento']).dt.year
    df_filtrado = df_filtrado[df_filtrado['anio_nacimiento'] == anio_seleccionado]
    df_filtrado = df_filtrado.drop(columns=['anio_nacimiento'])

# 8 acceso a internet
filtrar_internet = st.sidebar.checkbox("Filtrar por acceso a internet", key="filtrar_internet")
if filtrar_internet:
    tiene_internet = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"], key="radio_internet")
    if tiene_internet == "Sí":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == True]
    elif tiene_internet == "No":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == False]

# 9 ingresos nulos isnull
filtrar_ingresos_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos", key="filtrar_nulos")
if filtrar_ingresos_nulos:
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10
filtrar_rango_fechas_nacimiento = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento", key="filtrar_rango_fechas")
if filtrar_rango_fechas_nacimiento:
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", datetime.date(1949, 1, 1), key="fecha_inicio")
    fecha_fin = st.sidebar.date_input("Fecha de fin", datetime.date(2009, 12, 31), key="fecha_fin")
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]


st.subheader("DataFrame Filtrado")
st.dataframe(df_filtrado)


if st.checkbox("Mostrar DataFrame Original", key="mostrar_original"):
    st.subheader("DataFrame Original")
    st.dataframe(df_original)












