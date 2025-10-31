import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("Aset Koperasi")

# Folder tempat file disimpan
folder_path = "data/Aset"

# Urutan file yang ingin ditampilkan
file_order = [
    "Aset Kas.xlsx",
    "Aset Tabungan.xlsx",
    "Aset Deposito.xlsx",
    "Aset Simpanan di Koperasi Lain.xlsx",
    "Aset Pembiayaan.xlsx",
    "Aset Penyisihan Penghapusan Aktiva Produktif (PPAP).xlsx",
    "Aset Perlengkapan Kantor.xlsx",
    "Aset Beban Dibayar Dimuka.xlsx"
]

# Fungsi bantu untuk format angka
def format_number(x):
    if isinstance(x, (int, float)):
        return f"{x:,.0f}"
    return x

# Loop setiap file
for file_name in file_order:
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        # Ambil nama tanpa ekstensi dan "Aset "
        title = file_name.replace("Aset ", "").replace(".xlsx", "")
        st.subheader(title)

        df = pd.read_excel(file_path)
        df = df.fillna("")
        df = df.applymap(format_number)

        # Tampilkan tabel tanpa index
        st.dataframe(df, hide_index=True, use_container_width=True)
    else:
        st.warning(f"⚠️ File tidak ditemukan: {file_name}")