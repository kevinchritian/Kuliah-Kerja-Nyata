import streamlit as st

# Menambahkan CSS custom untuk menyembunyikan elemen dengan class tertentu
hide_css = """
<style>
    .st-emotion-cache-giotri, .e1nzilvr2 {
        display: none;
    }
</style>
"""

# Memasukkan CSS custom ke dalam aplikasi
st.markdown(hide_css, unsafe_allow_html=True)

# Konten Streamlit lainnya
st.title("Aplikasi Streamlit dengan Custom CSS")
st.write("Elemen bawaan Streamlit telah disembunyikan.")
