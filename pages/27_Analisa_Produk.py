import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Analisa Produk")

# Baca file Excel
df = pd.read_excel("data/Analisa Produk.xlsx")

# Bersihkan data kosong
df = df.fillna("")

# Pastikan kolom 'No' ditampilkan tanpa desimal
if "No" in df.columns:
    df["No"] = df["No"].apply(lambda x: int(x) if isinstance(x, (int, float)) and not pd.isna(x) else x)

# Perbaiki teks "Pola\nSyariah" jadi "Pola Syariah"
if "Opini" in df.columns:
    df["Opini"] = df["Opini"].apply(lambda x: str(x).replace("\n", " ").strip())

# Ganti newline di kolom 'Uraian' jadi <br> agar tampil baris baru di HTML
if "Uraian" in df.columns:
    df["Uraian"] = df["Uraian"].apply(lambda x: str(x).replace("\n", "<br>").strip())

# Hilangkan kolom "Unnamed" di header
df.columns = ["" if "Unnamed" in str(c) else c for c in df.columns]

# Styling tabel
st.markdown("""
<style>
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 16px;
}
th, td {
    border: 1px solid #666;
    padding: 8px;
    vertical-align: top;
}
th {
    text-align: center;
    font-weight: bold;
}
td {
    text-align: left;
}
td:first-child {
    text-align: center; /* Kolom No di tengah */
    width: 50px;
}
td:last-child {
    text-align: center; /* Kolom Opini di tengah */
    width: 120px;
}
</style>
""", unsafe_allow_html=True)

# Tampilkan tabel ke halaman Streamlit
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)