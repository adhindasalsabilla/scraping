import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Baca data dari file CSV
data = pd.read_csv('imdb_primary_uas.csv')

# Menampilkan judul di halaman web
st.title("Scraping IMDB")

# Membaca file CSV ke dalam DataFrame dengan encoding 'latin1'
df1 = pd.read_csv(fn1, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
st.dataframe(df1)

# Filter 5 film teratas dengan durasi terlama
top_5 = data.sort_values(by='Durasi(Menit)', ascending=False).head(5)

# Buat grafik bar
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_5['Name'], top_5['Durasi(Menit)'])
ax.set_xlabel('Nama Film')
ax.set_ylabel('Durasi (Menit)')
ax.set_title('5 Film Teratas dengan Durasi Terlama')
plt.show()

# Tampilkan grafik menggunakan Streamlit
st.title('5 Film Teratas dengan Durasi Terlama')
st.pyplot(fig)
