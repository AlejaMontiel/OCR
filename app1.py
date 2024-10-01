import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Estilos CSS para mejorar la apariencia
st.markdown("""
<style>
    body {
        background-color: #f0f4f8;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        color: #1E88E5;
        font-size: 36px;
        margin: 20px 0;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .header {
        text-align: center;
        color: #1565C0;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .text-output {
        background-color: #e3f2fd;
        border: 1px solid #1E88E5;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
        font-family: 'Georgia', serif;
        font-size: 18px;
        color: #333;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='title'>Reconocimiento Óptico de Caracteres (OCR)</h1>", unsafe_allow_html=True)

# Entrada de la cámara
img_file_buffer = st.camera_input("📸 Toma una Foto")

# Barra lateral con opciones de filtro
with st.sidebar:
    st.subheader("Opciones de Filtro")
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    # Leer el archivo de imagen con OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Aplicar filtro según la selección
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    # Convertir la imagen a formato RGB y realizar OCR
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)

    # Mostrar el texto reconocido
    st.markdown("<h2 class='header'>Texto Reconocido:</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='text-output'>{text}</div>", unsafe_allow_html=True)



    


