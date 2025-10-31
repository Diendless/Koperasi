import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Relasi Anggaran")

# --- 1. Baca file Excel ---
# Gunakan dtype=str agar tidak mengubah format angka di Excel
df = pd.read_excel("data/Relasi Anggaran.xlsx", dtype=str)

# --- 2. Bersihkan data ---
df = df.fillna("")

# --- 3. Format kolom angka ---
def format_angka(val):
    """Ubah angka ke format ribuan dengan titik (tanpa desimal)."""
    try:
        # Hilangkan koma dan titik yang tidak perlu, ubah ke int
        val = str(val).replace(",", "").replace(".", "")
        val = int(val)
        return f"{val:,}".replace(",", ".")
    except:
        return val

def format_persen(val):
    """Pastikan kolom Capaian tetap tampil dengan % di belakang."""
    try:
        if "%" in str(val):
            return val
        else:
            return f"{float(val) * 100:.1f}%"
    except:
        return val

# Terapkan format hanya untuk kolom yang sesuai
for col in df.columns:
    if "Capaian" in col and col != "Capaian 2024" and col != "Capaian 2023":
        df[col] = df[col].apply(format_persen)
    elif col != "Nama":
        df[col] = df[col].apply(format_angka)

# --- 4. Tampilkan tabel statis tanpa index ---
st.markdown(
    df.to_html(index=False, escape=False),
    unsafe_allow_html=True
)