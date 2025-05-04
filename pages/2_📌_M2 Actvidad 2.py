import os
import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Estudiantes en Colombia")
st.markdown(
    """
En esta actividad, se trabajará con un archivo CSV que contiene información de 50 estudiantes en Colombia,
 incluyendo datos como su nombre, edad, ciudad, promedio académico y asistencia. 
"""
)

st.header("Objetivo de aprendizaje")

st.markdown(
    """
    El objetivo principal es desarrollar una aplicación interactiva con Streamlit que permita explorar  información del archivo CSV.

"""
)

st.header("Solución")

st.title(" Bienvenido al explorador de Estudiantes")

st.subheader("¿Qué deseas hacer hoy con los registros?")

opcion = st.selectbox(
    "Elige una opción:",
    (
        "Ver primeras y últimas 5 filas",
        "Ver el resumen con .info() y .describe().)",
        "Seleccionar columnas específicas",
        "Filtrar por promedio",
    ),
)


try:
    archivo = pd.read_csv("assets/estudiantes_colombia.csv")
except FileNotFoundError:
    st.error(
        "No se encontró el archivo 'estudiantes.csv' en la carpeta 'assets'.  Asegúrate de que el archivo exista y la ruta sea correcta."
    )
    st.stop()  
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()



if opcion == "Ver primeras y últimas 5 filas":
    

    st.subheader("▪️ Primeras 5 filas")
    st.dataframe(archivo.head())

    
    st.subheader("▪️ Últimas 5 filas")
    st.dataframe(archivo.tail())



elif opcion == "Resumen del dataset (.info y .describe)":
    st.subheader("Resumen general del dataset")
    
    st.write(archivo.info())

    st.text("Resumen estadístico con .describe():")
    
    st.write(archivo.describe())



elif opcion == "Seleccionar columnas específicas":
    st.subheader("Qué columnas quieres ver")
    columnas = st.multiselect(
        "Selecciona una o más columnas:",
        archivo.columns.tolist(),
        default=["nombre", "edad", "ciudad", "promedio", "asistencia"],
    )
    st.dataframe(archivo[columnas])



elif opcion == "Filtrar por promedio":
    st.subheader("Filtra estudiantes según su promedio")
    promedio_minimo = st.slider(
        "Promedio mínimo", min_value=0.0, max_value=5.0, value=3.0, step=0.1
    )  
    st.write(
        archivo[archivo["promedio"] > promedio_minimo]
    )  