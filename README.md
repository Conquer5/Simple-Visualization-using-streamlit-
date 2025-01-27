# Analisis Data: Air Quality Dataset

Aplikasi ini dirancang menggunakan **Streamlit** untuk menganalisis dataset kualitas udara. Aplikasi ini menyediakan visualisasi interaktif dan analisis data yang membantu memahami pola polutan dan hubungan antar variabel.

## Fitur Utama

1. **Tampilan Dataset**
   - Menampilkan data awal untuk memberikan gambaran umum tentang dataset yang digunakan.

2. **Visualisasi Rata-rata Bulanan Polutan**
   - Grafik interaktif untuk mengamati pola rata-rata bulanan parameter seperti PM2.5, PM10, dan Ozon (O₃).

3. **Matriks Korelasi**
   - Heatmap interaktif untuk mengidentifikasi hubungan antar variabel polutan.

4. **Insight Data**
   - Analisis mendalam tentang pola polusi udara, hubungan antar polutan, dan kemungkinan penyebabnya.

## Cara Menggunakan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/air-quality-analysis.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd air-quality-analysis
   ```
3. Pastikan Anda memiliki Python 3.7 atau lebih baru.
4. Install semua dependensi:
   ```bash
   pip install -r requirements.txt
   ```
5. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run main.py
   ```

## Struktur Dataset

Dataset yang digunakan memiliki kolom berikut:
- **Tanggal dan Waktu**: Kombinasi tahun, bulan, hari, dan jam.
- **Polutan**: PM2.5, PM10, O₃, CO, NO₂, SO₂, dan parameter lainnya.

## Output Aplikasi

- **Tabel Data**: Menampilkan preview data awal.
- **Grafik Bulanan**: Visualisasi rata-rata bulanan untuk parameter PM2.5, PM10, dan O₃.
- **Heatmap Korelasi**: Matriks korelasi untuk melihat hubungan antar variabel.

## Teknologi yang Digunakan

- **Streamlit**: Framework untuk membuat aplikasi web berbasis Python.
- **Pandas**: Untuk pengolahan data.
- **Matplotlib** dan **Seaborn**: Untuk visualisasi data.

## Catatan Penting

- File dataset bernama `Cleaned_data.csv` harus berada di direktori yang sama dengan file `main.py`.
- Dataset harus mencakup kolom `year`, `month`, `day`, dan `hour` untuk pengolahan waktu.

## Kontribusi

Kontribusi sangat dihargai! Silakan buat pull request atau ajukan issue jika Anda memiliki ide atau menemukan bug.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
