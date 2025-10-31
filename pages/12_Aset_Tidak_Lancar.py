import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")  # agar tabel tampil lebar penuh
st.title("Aset Tidak Lancar")

# Baca file Excel
df = pd.read_excel("data/Aset Tidak Lancar.xlsx")

# Ganti header "Unnamed" jadi kosong
df.columns = ["" if "Unnamed" in col else col for col in df.columns]

# Ganti None/NaN jadi kolom kosong 
df = df.fillna("")

# Format angka: ubah semua angka menjadi string dengan format ribuan
for col in df.columns[1:]:  # lewati kolom pertama jika itu teks (misal 'ASSET')
    df[col] = df[col].apply(lambda x: f"{int(x):,}" if isinstance(x, (int, float)) and not pd.isna(x) else x)

# Hilangkan index dan tampilkan tabel penuh
st.dataframe(df, hide_index=True, use_container_width=True)