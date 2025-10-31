import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("Beban Pokok")

# Folder tempat file disimpan
folder_path = "data/Beban Pokok"

# Urutan file yang ingin ditampilkan
file_order = [
    "Beban Bagi Hasil Simpanan.xlsx",
    "Beban Bagi Hasil Dana Pihak Ketiga.xlsx",
    "Jumlah Beban Pokok.xlsx"
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

        # Baca file Excel
        df = pd.read_excel(file_path)

        # Ganti nilai kosong jadi string kosong
        df = df.fillna("")

        # 🔹 Ganti header "Unnamed" jadi kosong
        df.columns = ["" if "Unnamed" in str(col) else col for col in df.columns]

        # Format angka ribuan
        df = df.applymap(format_number)

        # Tampilkan tabel tanpa index
        st.dataframe(df, hide_index=True, use_container_width=True)
    else:
        st.warning(f"⚠️ File tidak ditemukan: {file_name}")