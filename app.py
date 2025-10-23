import streamlit as st
from PIL import Image
from qr import generar_qr

st.set_page_config(page_title = "QrEZ", page_icon = "📨")

col1, col2, col3 = st.columns((2, 1, 2))
with col2:
    st.header("QrEZ")

col1, col2, col3 = st.columns((2, 20, 2))
with col2:
    st.title("Crea QR de forma rapida y gratuita")
    link = st.text_input("Ingrese el link", key="link")
    estatus = st.empty()

col1, col2, col3 = st.columns((2, 1, 2))
with col2:

    red = st.checkbox("Rojo", key="red")
    azul = st.checkbox("Azul",key = "blue")
    morado = st.checkbox("Morado", key="purple")
    verde = st.checkbox("Verde", key = "green")

if red:
    azul = False
    morado = False
    verde = False 
    color_file = "red"


elif azul:
    red = False
    morado = False
    verde = False
    color_file = "blue"

elif morado:
    red = False
    azul = False
    verde = False
    color_file = "purple"

elif verde:
    red = False
    azul = False
    morado = False
    color_file = "green"
else:
    color_file = "Black"

col1, col2, col3 = st.columns((2, 10, 2))
with col2:
    if link:
        estatus.success("QR generado correctamente")
        imagen = generar_qr(link, color_file)

        col1, col2, col3 = st.columns((1, 10, 1))
        with col2:
            st.image(imagen, caption="QR generado", width=400)
        
        if imagen:
            col1, col2, col3, col4 = st.columns((1,2 , 2, 1))
            with col2:
                st.download_button("Descargar QR", data=imagen, file_name="QR.png")
            
            with col3:
                if st.button("Refrescar"):
                    imagen = None
                    red = None
                    azul = None
                    verde = None
                    morado = None
                    link = None
                    st.session_state.clear()
                    st.rerun()


        else:
            st.download_button("Descargar QR")


    else:  
        estatus.info("Ingrese el qr")

