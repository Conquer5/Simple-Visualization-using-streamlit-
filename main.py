import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pengenalan
st.title("Analisis Data: Air Quality Dataset")
st.write("""
Aplikasi ini menganalisis dataset kualitas udara, yang mencakup berbagai parameter polutan seperti PM2.5, PM10, Ozon (O3), dan lainnya.
Tujuan utama adalah untuk memahami pola bulanan polutan dan hubungan antar variabel melalui visualisasi interaktif.
""")

# Load dataset secara langsung
file_path = 'Cleaned_data.csv'
df = pd.read_csv(file_path)

# Konversi kolom waktu menjadi format datetime
df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df.set_index('date', inplace=True)

# Pengenalan dataset
st.subheader("Dataset")
st.write("Dataset yang digunakan:")
st.write(df.head())

# Visualisasi rata-rata bulanan polutan
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
monthly_mean = df[numeric_columns].resample('M').mean()

st.subheader("Visualisasi Rata-rata Bulanan Polutan")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_mean['pm2.5'], label='PM2.5', marker='o')
ax.plot(monthly_mean['pm10'], label='PM10', marker='s')
ax.plot(monthly_mean['o3'], label='O3', marker='^')
ax.set_title("Monthly Average Pollutants")
ax.set_xlabel("Date")
ax.set_ylabel("Pollutant Levels")
ax.legend()
st.pyplot(fig)

# Encoding kategori dan visualisasi korelasi
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].astype('category').cat.codes

correlation_matrix = df.corr()

st.subheader("Matriks Korelasi")
st.write("Hubungan antar variabel dijelaskan dengan matriks korelasi berikut:")
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
ax.set_title("Correlation Matrix Heatmap")
st.pyplot(fig)

# Insight
st.subheader("Insight dari Analisis")
st.write("""
- **Rata-rata Bulanan Polutan**:
    - PM2.5 dan PM10 memiliki pola fluktuasi yang serupa, dengan PM10 cenderung lebih tinggi.
    - Ozon (O3) menunjukkan pola yang berbeda, cenderung meningkat ketika PM2.5 dan PM10 menurun.
- **Matriks Korelasi**:
    - PM2.5 dan PM10 memiliki korelasi positif yang tinggi, mengindikasikan sumber polusi yang serupa.
    - CO, NO2, dan SO2 juga memiliki korelasi positif dengan PM2.5 dan PM10, sementara O3 memiliki korelasi negatif.
- **Polutan PM2.5 dan PM10** menunjukkan pola fluktuasi yang serupa, dengan peningkatan signifikan pada periode tertentu yang mungkin terkait dengan aktivitas musiman atau kejadian luar biasa.
- Sebaliknya, **ozon** menunjukkan pola musiman yang berlawanan, kemungkinan dipengaruhi oleh kondisi atmosfer seperti sinar matahari atau suhu.
- Terdapat korelasi positif antara **SO₂, NO₂, dan CO** dengan tingkat PM2.5 dan PM10, dengan CO dan NO₂ menunjukkan hubungan yang lebih kuat. Sebaliknya, **O₃** memiliki korelasi negatif dengan keduanya, yang mungkin dipengaruhi oleh dinamika atmosfer yang berbeda.
""")