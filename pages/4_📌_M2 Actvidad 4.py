import streamlit as st
import pandas as pd
import numpy as np


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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


st.title("Las Películas mas valoradas de la Historia")




def cargar_datos():
    data = {
        'Título': ['El Padrino', 'Rambo', 'Rocky', 'El Caballero Oscuro', 'Forrest Gump', 'Terminator', 'Interestelar', 'Misión Imposible', 'Scarface', 'Casablanca'],
        'Año': [1972, 1982, 1976, 2008, 1994, 1984, 2014, 1996, 1983, 1942],
        'Género': ['Crimen', 'Acción', 'Drama', 'Acción', 'Drama', 'Ciencia Ficción', 'Ciencia Ficción', 'Acción', 'Crimen', 'Romance'],
        'Director': ['Francis Ford Coppola', 'Ted Kotcheff', 'John G. Avildsen', 'Christopher Nolan', 'Robert Zemeckis', 'James Cameron', 'Christopher Nolan', 'Brian De Palma', 'Brian De Palma', 'Michael Curtiz'],
        'Puntuación IMDb': [9.2, 7.2, 8.1, 9.0, 8.8, 8.1, 8.6, 7.1, 8.3, 8.5],
        'Recaudación (Millones USD)': [246.1, 47.2, 117.2, 1004.9, 677.9, 78.4, 701.7, 457.7, 65.9, 3.7]
    }
    df = pd.DataFrame(data)
    return df

df_original = cargar_datos()
df = df_original.copy() 


st.sidebar.header("Controles")


if st.sidebar.checkbox("Mostrar DataFrame Completo"):
    st.subheader("DataFrame Completo")
    st.dataframe(df)

# --- Sección para Selección con .loc ---
st.subheader("Selección con `.loc`")
st.markdown("Selecciona filas y columnas por etiquetas.")

# Selección de columnas con .loc
columnas_loc = st.sidebar.multiselect("Seleccionar columnas (.loc)", df.columns, default=['Título', 'Año', 'Género'])
if columnas_loc:
    
    st.dataframe(df.loc[:, columnas_loc])


st.sidebar.subheader("Filtrado de Filas (.loc)")
columna_filtro_loc = st.sidebar.selectbox("Filtrar por columna (.loc)", df.columns)
valores_filtro_loc = st.sidebar.multiselect(f"Valores a incluir en {columna_filtro_loc} (.loc)", df[columna_filtro_loc].unique())
if valores_filtro_loc:
    df_filtrado_loc = df.loc[df[columna_filtro_loc].isin(valores_filtro_loc)]
    st.write("DataFrame filtrado (.loc):")
    st.dataframe(df_filtrado_loc)


st.sidebar.subheader("Selección de Celda Específica (.loc)")
fila_loc = st.sidebar.selectbox("Índice de fila (.loc)", df.index.tolist())
columna_celda_loc = st.sidebar.selectbox("Columna (.loc)", df.columns)
st.write(f"Valor en la fila {fila_loc} y columna '{columna_celda_loc}' (.loc):")
if fila_loc in df.index and columna_celda_loc in df.columns:
    st.write(df.loc[fila_loc, columna_celda_loc])
else:
    st.warning("Índice de fila o columna no válido.")

st.subheader("Selección con `.iloc`")
st.markdown("Selecciona filas y columnas por posición (índice entero).")


indices_columnas_iloc = st.sidebar.multiselect("Seleccionar columnas (índices)", list(range(len(df.columns))), format_func=lambda i: f"{df.columns[i]} ({i})", default=[0, 1, 2])
if indices_columnas_iloc:
    st.write("DataFrame con columnas seleccionadas:")
    st.dataframe(df.iloc[:, indices_columnas_iloc])


st.sidebar.subheader("Filtrado de Filas (por índice")
indices_filas_iloc = st.sidebar.multiselect("Seleccionar filas por índice (.iloc)", df.index.tolist())
if indices_filas_iloc:
    df_filtrado_iloc_indices = df.iloc[indices_filas_iloc]
    st.write("DataFrame filtrado por índice (.iloc):")
    st.dataframe(df_filtrado_iloc_indices)


st.sidebar.subheader("Selección de Celda Específica (.iloc)")
indice_fila_iloc = st.sidebar.selectbox("Índice de fila (.iloc)", df.index.tolist())
indice_columna_iloc = st.sidebar.selectbox("Índice de columna (.iloc)", list(range(len(df.columns))), format_func=lambda i: f"{df.columns[i]} ({i})")
st.write(f"Valor en la fila {indice_fila_iloc} y columna '{df.columns[indice_columna_iloc]}' (índice .iloc):")
if indice_fila_iloc in df.index and 0 <= indice_columna_iloc < len(df.columns):
    st.write(df.iloc[indice_fila_iloc, indice_columna_iloc])
else:
    st.warning("Índice de fila o columna no válido.")


st.subheader("Modificación con `.loc`")
st.markdown("Modifica valores en el DataFrame utilizando etiquetas.")

st.sidebar.subheader("Modificar Valor con `.loc`")
fila_modificar_loc = st.sidebar.selectbox("Fila a modificar (.loc)", df.index.tolist())
columna_modificar_loc = st.sidebar.selectbox("Columna a modificar (.loc)", df.columns)
nuevo_valor_loc = st.sidebar.text_input(f"Nuevo valor para '{columna_modificar_loc}' en la fila {fila_modificar_loc} (.loc)")
if st.sidebar.button("Modificar con .loc"):
    if fila_modificar_loc in df.index and columna_modificar_loc in df.columns and nuevo_valor_loc:
        try:
            
            dtype_original = df_original.loc[fila_modificar_loc, columna_modificar_loc].dtype
            df.loc[fila_modificar_loc, columna_modificar_loc] = pd.Series([nuevo_valor_loc], dtype=dtype_original)[0]
            st.success(f"Valor en '{columna_modificar_loc}' para la fila {fila_modificar_loc} modificado a '{df.loc[fila_modificar_loc, columna_modificar_loc]}'.")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error al modificar el valor: {e}")
    elif not nuevo_valor_loc:
        st.warning("Por favor, introduce un nuevo valor.")
    else:
        st.warning("Índice de fila o columna no válido para la modificación.")


st.subheader("Modificación con `.iloc`")
st.markdown("Modifica valores en el DataFrame utilizando índices enteros.")

st.sidebar.subheader("Modificar Valor con `.iloc`")
fila_modificar_iloc = st.sidebar.selectbox("Fila a modificar (índice .iloc)", df.index.tolist())
indice_columna_modificar_iloc = st.sidebar.selectbox("Índice de columna a modificar (.iloc)", list(range(len(df.columns))), format_func=lambda i: f"{df.columns[i]} ({i})")
nuevo_valor_iloc = st.sidebar.text_input(f"Nuevo valor para '{df.columns[indice_columna_modificar_iloc]}' en la fila {fila_modificar_iloc} (índice .iloc)")
if st.sidebar.button("Modificar con .iloc"):
    if fila_modificar_iloc in df.index and 0 <= indice_columna_modificar_iloc < len(df.columns) and nuevo_valor_iloc:
        try:
            dtype_original_iloc = df_original.iloc[fila_modificar_iloc, indice_columna_modificar_iloc].dtype
            df.iloc[fila_modificar_iloc, indice_columna_modificar_iloc] = pd.Series([nuevo_valor_iloc], dtype=dtype_original_iloc)[0]
            st.success(f"Valor en '{df.columns[indice_columna_modificar_iloc]}' para la fila {fila_modificar_iloc} modificado a '{df.iloc[fila_modificar_iloc, indice_columna_modificar_iloc]}'.")
            st.dataframe(df) 
        except Exception as e:
            st.error(f"Error al modificar el valor: {e}")
    elif not nuevo_valor_iloc:
        st.warning("Por favor, introduce un nuevo valor.")
    else:
        st.warning("Índice de fila o columna no válido para la modificación.")

if st.sidebar.button("Resetear DataFrame"):
    df = df_original.copy()
    st.info("DataFrame reseteado a su estado original.")

