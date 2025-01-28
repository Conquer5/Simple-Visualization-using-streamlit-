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
pollutants = ['pm2.5', 'pm10', 'o3', 'so2', 'co', 'no2']
selected_pollutants = st.sidebar.multiselect("Pilih Polutan", pollutants, default=['pm2.5', 'pm10'])

# Pilih Frekuensi Resampling
resample_options = {"Harian": "D", "Bulanan": "M", "Tahunan": "Y"}
resample_freq = st.sidebar.radio("Pilih Skala Waktu", list(resample_options.keys()), index=1)

# ---- FILTER DATA ----
df_filtered = df[(df.index.year >= start_year) & (df.index.year <= end_year)]
df_resampled = df_filtered[selected_pollutants].resample(resample_options[resample_freq]).mean()

# ---- PLOTTING ----
st.title("📊 Visualisasi Tren Konsentrasi Polutan Udara")
st.subheader(f"Tren Polutan dari {start_year} hingga {end_year} ({resample_freq})")

fig, ax = plt.subplots(figsize=(12, 6))

for pollutant in selected_pollutants:
    ax.plot(df_resampled.index, df_resampled[pollutant], marker='o', label=pollutant)

ax.set_title(f"Tren Rata-rata {', '.join(selected_pollutants)} ({resample_freq})", fontsize=14)
ax.set_xlabel("Tanggal", fontsize=12)
ax.set_ylabel("Konsentrasi (µg/m³)", fontsize=12)
ax.legend()
ax.grid(True)

# Menampilkan Plot di Streamlit
st.pyplot(fig)

# ---- MENAMPILKAN DATAFRAME ----
st.subheader("📋 Data yang Digunakan")
st.dataframe(df_resampled)
