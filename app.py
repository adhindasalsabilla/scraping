import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Baca data dari file PDF
data = pd.read_csv('imdb_primary_uas.csv')

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
st.write("Grafik ini menjelaskan tentang Top 5 Judul Film dengan Durasi Terlama berdasarkan IMDB. Gang of Wayseppur menjadi film dengan durasi terlama (melampaui 300 menit) diikuti Ben-Hur dengan durasi sekitar 225 menit."")
