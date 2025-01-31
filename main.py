import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat dataset
@st.cache_data
def load_data():
    # Load dataset
    df = pd.read_csv("Cleaned_data.csv")

    # Pastikan kolom 'date' bertipe datetime dan dijadikan indeks
    df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df.set_index('date', inplace=True)

    # Ubah nama kolom agar lebih seragam
    df.rename(columns={'PM2.5': 'pm2.5', 'PM10': 'pm10'}, inplace=True)

    # Menambahkan kolom 'season' berdasarkan musim
    df['season'] = df['month'].apply(lambda x: 'Spring' if x in [3, 4, 5] else 
                                     ('Summer' if x in [6, 7, 8] else 
                                     ('Fall' if x in [9, 10, 11] else 'Winter')))
    
    return df

# Load data
df = load_data()

# ---- SIDEBAR FILTER ----
st.sidebar.header("📌 Filter Data")

# Pilih Rentang Tahun
years = sorted(df.index.year.unique())
start_year, end_year = st.sidebar.select_slider(
    "Pilih Rentang Tahun",
    options=years,
    value=(years[0], years[-1])
)

# Pilih Polutan untuk Ditampilkan
pollutants = ['pm2.5', 'pm10']
selected_pollutants = st.sidebar.multiselect("Pilih Polutan", pollutants, default=['pm2.5', 'pm10'])

# ---- FILTER DATA ----
df_filtered = df[(df.index.year >= start_year) & (df.index.year <= end_year)]

# ---- PLOTTING VISUALISASI 1: Tren Konsentrasi PM2.5 dan PM10 per Tahun ----
st.title("📊 Visualisasi Tren Konsentrasi Polutan Udara")
st.subheader(f"Tren Konsentrasi PM2.5 dan PM10 per Tahun ({start_year} hingga {end_year})")

# Visualisasi Tren Konsentrasi PM2.5 dan PM10 per Tahun
plt.figure(figsize=(14, 8))

# Plot PM2.5
sns.lineplot(x='year', y='pm2.5', data=df_filtered, marker='o', label='PM2.5', color='blue', markersize=8, linewidth=2)

# Plot PM10
sns.lineplot(x='year', y='pm10', data=df_filtered, marker='o', label='PM10', color='orange', markersize=8, linewidth=2)

# Menambahkan Title dan Label dengan ukuran yang lebih besar
plt.title('Tren Konsentrasi PM2.5 dan PM10 per Tahun', fontsize=18)
plt.xlabel('Tahun', fontsize=16)
plt.ylabel('Konsentrasi (µg/m³)', fontsize=16)

# Mengatur ukuran font pada ticks
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Mengatur ukuran font pada legenda
plt.legend(fontsize=14)

# Mengatur agar grid lebih jelas
plt.grid(True)

# Menampilkan plot
st.pyplot(plt)

# ---- PLOTTING VISUALISASI 2: Konsentrasi PM2.5 dan PM10 per Musim ----
st.subheader("Distribusi Konsentrasi PM2.5 dan PM10 per Musim")

# Visualisasi Tren Konsentrasi PM2.5 dan PM10 per Musim (Boxplot)
plt.figure(figsize=(14, 8))

# Plot PM2.5 per Musim
sns.boxplot(x='season', y='pm2.5', data=df_filtered, palette="Set2", boxprops=dict(alpha=0.7))

# Plot PM10 per Musim
sns.boxplot(x='season', y='pm10', data=df_filtered, palette="Set2", boxprops=dict(alpha=0.7))

# Menambahkan Title dan Label dengan ukuran yang lebih besar
plt.title('Distribusi Konsentrasi PM2.5 dan PM10 per Musim', fontsize=18)
plt.xlabel('Musim', fontsize=16)
plt.ylabel('Konsentrasi (µg/m³)', fontsize=16)

# Mengatur ukuran font pada ticks
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Menampilkan plot
st.pyplot(plt)

# ---- MENAMPILKAN DATAFRAME ----
st.subheader("📋 Data yang Digunakan")
st.dataframe(df_filtered[selected_pollutants])
