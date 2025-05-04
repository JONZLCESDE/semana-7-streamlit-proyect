import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

biblioteca = {
    "Titulo": [
        "orgullo y valor",
        "orgullo y valor",
        "orgullo y valor",
        "orgullo y valor",
    ],
    "Autor": ["Andrew vahkelinho", "Andrew vahkelinho", "Andrew vahkelinho", "Andrew vahkelinho"],
    "Año de publicación": ["1858", "1858", "1858", "1858"],
    "Genero": ["Filosofia", "Filosofia", "Filosofia", "filosofia"],
}

df_bibioteca = pd.DataFrame(biblioteca)



st.write(
    """1. Crea un diccionario en tu script con al menos cuatro claves: "título", "autor", año de publicación" y "género". Para cada clave asigna una lista con datos de ejemplo sobre libros (por ejemplo, 3 o 4 libros distintos)."""
)

st.dataframe(df_bibioteca)

lista_biblioteca = [
    {
        "Titulo": "orgullo y valor",
        "Autor": "Andrew vahkelinho",
        "Año de publicación": "1858",
        "Genero": "Filosofia",
        
    },
    {
        "Titulo": "orgullo y perspicacia",
        "Autor": "Andrew vahkelinho",
        "Año de publicación": "1865",
        "Genero": "Filosofia",
        
    },
    {
        "Titulo": "orgullo y herencia",
        "Autor": "Andrew vahkelinho",
        "Año de publicación": "1870",
        "Genero": "Filosofia",
        
    },
    
   {
        "Titulo": "orgullo y descendencia",
        "Autor": "Andrew vahkelinho 2do",
        "Año de publicación": "1885",
        "Genero": "Filosofia",
        
    },
    
]

df_lista_biblioteca = pd.DataFrame(lista_biblioteca)


st.write("DataFrame de libros")

st.dataframe(df_lista_biblioteca)




productos = [
    ["Shorts", 100.000, 15],
    ["Camisa de Tirantes", 55.000, 50],
    ["Chanclas", 80.000, 100],
    ["Abrigo", 120.000, 30],
]

columnas = ["Producto", "Precio", "Cantidad en Stock"]
df_productos = pd.DataFrame(productos, columns=columnas)

st.dataframe(df_productos)



