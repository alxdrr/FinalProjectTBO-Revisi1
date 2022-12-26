import streamlit as st
from convert import CYK

valid = 'n'
result = list()

def start():
    st.set_page_config(page_title="Grammar Checker", layout="wide")    
    st.title("Tata :red[Bahasa] Indonesia")
    st.write("Kalimat yang baik adalah kalimat yang :green[memenuhi struktur tata bahasa]")
    st.write("---")

    left_column, right_column = st.columns(2)

    with left_column:
        sentence = st.text_input("Masukan Kalimat :red[Bahasa Indonesia]", placeholder="Ibu Sedang Memasak")
        if st.button('Cek Aturan'):
            CYK(sentence)      
    with right_column:
        if valid == 'n':
            st.write("# Cek Tata :red[Bahasa] Indonesia Sekarang !")
        elif valid == 'x':
            st.write("# Kalimat :red[Tidak Valid]") 
        else:
            st.write("# Kalimat :green[Valid]") 
            # pattern(result)
    st.write("---")