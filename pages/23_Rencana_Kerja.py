import streamlit as st
import pandas as pd

st.title("Rencana Kerja")

# Baca file Excel
df = pd.read_excel("data/Rencana Kerja.xlsx", header=None)

# Ganti NaN dengan string kosong agar tidak muncul 'nan'
df = df.fillna("")

# Buat tabel HTML
html = """
<style>
table {
    width: 100%;
    border-collapse: collapse;
    font-family: Arial, sans-serif;
    font-size: 15px;
}
th, td {
    border: 1px solid black;
    padding: 5px 8px;
    vertical-align: top;
}
th {
    text-align: center;
}
tr.section td {
    font-weight: bold;
}
tr.subsection td {
    font-weight: bold;
}
</style>

<table>
<tr>
    <th style='width:5%'>No</th>
    <th>RENCANA KERJA</th>
    <th>KETERANGAN</th>
</tr>
"""

# Loop isi data
for _, row in df.iterrows():
    col1, col2, col3 = row[0], row[1], row[2] if len(row) > 2 else ""

    # Baris utama (I, II, III, IV)
    if str(col1).strip() in ["I", "II", "III", "IV"]:
        html += f"<tr class='section'><td style='text-align:center'>{col1}</td><td colspan='2'>{col2}</td></tr>"
    # Subjudul besar (huruf besar semua)
    elif str(col2).isupper() and col3 == "":
        html += f"<tr class='subsection'><td></td><td colspan='2'>{col2}</td></tr>"
    # Baris isi (a, b, c, ...)
    else:
        html += f"<tr><td style='text-align:center'>{col1}</td><td>{col2}</td><td>{col3}</td></tr>"

html += "</table>"

# Tampilkan di Streamlit
st.markdown(html, unsafe_allow_html=True)