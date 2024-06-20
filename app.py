import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Baca data dari file PDF
data = pd.read_csv('imdb_primary_uas.csv')

# Filter 10 film teratas berdasarkan rating IMDb
top_10 = data.sort_values(by='Rating', ascending=False).head(10)

# Buat grafik bar
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_10['Name'], top_10['Rating'])
ax.set_xlabel('Nama Film')
ax.set_ylabel('Rating IMDb')
ax.set_title('10 Film Teratas Berdasarkan Rating di IMDB')
plt.show()

# Tampilkan grafik menggunakan Streamlit
st.title('10 Film Teratas Berdasarkan Rating IMDB')
st.pyplot(fig)
