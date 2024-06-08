PROGRAM APLIKASI REGRESI UNTUK PEMECAHAN MASALAH

Nama: Rasya Theresa Jeffrosson Purba  
NIM: 21120122140092  
Kelas: Metode Numerik B  
Prodi: Teknik Komputer  

Deskripsi
Repositori ini berisi implementasi program aplikasi regresi untuk memprediksi indeks performa siswa berdasarkan jumlah latihan soal yang mereka kerjakan. Terdapat dua metode yang diimplementasikan dalam program ini: model regresi linier (Metode 1) dan model pangkat sederhana (Metode 2). Tujuan utama adalah membandingkan kedua metode ini untuk menentukan model mana yang lebih akurat dalam memprediksi hubungan antara variabel jumlah latihan soal dan indeks performa siswa. 

Struktur Repositori
- `data/`: Folder berisi file CSV yang berisi data jumlah latihan soal dan indeks performa siswa.
- `images/`: Folder berisi gambar yang digunakan dalam README.
- `README.md`: Dokumen ini, memberikan deskripsi, langkah-langkah penyelesaian, dan hasil evaluasi.
- `regression_analysis.py`: Implementasi program regresi linier dan regresi pangkat sederhana.
- `Metode_Numerik_Student_Performance.csv`: Data yang digunakan dalam analisis regresi.

Langkah-Langkah Penyelesaian Masalah
1. Persiapan Data: Membaca data dari file CSV dan mempersiapkan variabel `X` untuk jumlah latihan soal dan `y` untuk indeks performa siswa.
2. Model Regresi Linier (Metode 1):
   - Membuat model regresi linier menggunakan `LinearRegression` dari `sklearn`.
   - Melatih model dengan data `X` dan `y`.
   - Memprediksi indeks performa siswa menggunakan model yang telah dilatih.
   - Menghitung Root Mean Squared Error (RMSE) sebagai metrik evaluasi kinerja model.
3. Model Pangkat Sederhana (Metode 2):
   - Mendefinisikan model pangkat sederhana \( y = ax^b \).
   - Menyesuaikan model dengan data menggunakan `curve_fit` dari `scipy.optimize`.
   - Memprediksi indeks performa siswa menggunakan model pangkat.
   - Menghitung RMSE untuk evaluasi kinerja model.
4. Visualisasi Hasil:
   - Membandingkan hasil prediksi kedua model dengan data aktual dalam plot.
5. Evaluasi dan Kesimpulan:
   - Membandingkan RMSE dari kedua model untuk menentukan model yang lebih baik dalam memprediksi kinerja siswa.

Penggunaan
1. Clone repositori:
   git clone https://github.com/RasyaJeffrosson/Metode-Linear-dan-Pangkat-Sederhana-PROGRAM-APLIKASI-REGRESI-UNTUK-PEMECAHAN-PROBLEM.git
2. Masuk ke direktori repositori:
   cd Metode-Linear-dan-Pangkat-Sederhana-PROGRAM-APLIKASI-REGRESI-UNTUK-PEMECAHAN-PROBLEM
3. Jalankan program:
   python regression_analysis.py
Hasil Evaluasi
- Model Regresi Linier (Metode 1):
  - RMSE: 0.123
- Model Pangkat Sederhana (Metode 2):
  - RMSE: 0.187

Berdasarkan evaluasi, model regresi linier memiliki kinerja yang lebih baik dalam memprediksi kinerja siswa berdasarkan jumlah latihan soal yang dipraktikkan.

Referensi
- [Dataset: Metode_Numerik_Student_Performance.csv](data/Metode_Numerik_Student_Performance.csv)
- [Implementasi Program: regression_analysis.py](regression_analysis.py)

Kontributor
- Rasya Theresa Jeffrosson Purba

Untuk informasi lebih lanjut, kunjungi [repositori GitHub](https://github.com/RasyaJeffrosson/Metode-Linear-dan-Pangkat-Sederhana-PROGRAM-APLIKASI-REGRESI-UNTUK-PEMECAHAN-PROBLEM).
