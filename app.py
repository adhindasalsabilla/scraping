import pandas as pd
import streamlit as st

# Fungsi untuk membaca data IMDB
def load_imdb_data():
    fn1 = 'imdb_primary_uas.csv'
    df1 = pd.read_csv(fn1, encoding='latin1')
    return df1

# Fungsi untuk membuat visualisasi
def visualize_top_5(df):
    # Ambil 5 baris pertama
    top_5 = df.head(5)

    # Ambil kolom yang relevan
    name = top_5['name']
    rating = top_5['rating']

    # Buat visualisasi
    plt.figure(figsize=(10, 8))
    plt.barh(name, rating, color='skyblue')
    plt.title('Top 5 Rating Film di IMDB')
    plt.xlabel('Rating')
    plt.ylabel('Name')
    st.pyplot(plt)
