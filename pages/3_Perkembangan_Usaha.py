import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")  # agar tabel tampil lebar penuh
st.title("Perkembangan Usaha")

# Baca file Excel
df = pd.read_excel("data/Perkembangan Usaha.xlsx")

# Ganti None/NaN jadi kolom kosong 
df = df.fillna("")

# Hilangkan index dan tampilkan tabel penuh
st.dataframe(df, hide_index=True, use_container_width=True)