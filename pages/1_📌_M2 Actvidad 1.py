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

lista_ciudades = [
    {
        "nombre": "Medellín",
        "Población": "2,800,000",
        "País": "Colombia",
    },
    {
        "nombre": "Bogotá",
        "Población": "7,000,000 ",
        "País": "Colombia",
    },
    {
        "nombre": "Nueva York",
        "Población": "9,500,000",
        "País": "Estados Unidos",
    },
    {
        "nombre": "Los Ángeles ",
        "Población": "5,000,000",
        "País": "Estados Unidos",
    },
]

df_lista_ciudades = pd.DataFrame(lista_ciudades)
st.subheader("**2. Lista de diccionarios:**")

st.write(
    """**Una lista de diccionarios es como una colección de filas, donde cada diccionario representa una fila con sus columnas etiquetadas.**
    Crea una lista que contenga varios diccionarios (por ejemplo, 3 o 4). Cada diccionario debe tener las claves "nombre", "población" y "país", 
    con valores correspondientes a ciudades diferentes."""
)

st.subheader("Información de Ciudades")
st.dataframe(df_lista_ciudades)



with st.expander("Ver información de las ciudades"):
    st.dataframe(df_lista_ciudades)


    nombres = pd.Series(
    [
        "Lucas",
        "Mario",
        "Sara",
        "Carolina",
        "John",
    ]
)
edades = pd.Series([18, 20, 23, 30, 40])
ciudades = pd.Series(["Medellín", "Bogotá", "Cali", "Armenia", "Manizales"])


series_combinadas = {
    "Nombres": nombres,
    "edades": edades,
    "ciudades": ciudades,
}
df_datos_personas = pd.DataFrame(series_combinadas)
st.subheader("Datos de Personas")
st.dataframe(df_datos_personas)


with st.expander("Información sobre la creación de Series y DataFrame de personas", expanded=True):
    st.info(
        "Se crearon tres Series de pandas para nombres, edades y ciudades. "
        " estas Series se combinaron en un diccionario  para mostrar los datos de varias personas."
    )




