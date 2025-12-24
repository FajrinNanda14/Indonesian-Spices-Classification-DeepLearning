# 🌿Identifikasi Jenis Rempah-Rempah Dapur Indonesia🌿

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.x-red.svg)](https://streamlit.io/)

Repositori ini dibuat untuk memenuhi Tugas Ujian Akhir Praktikum Mata Kuliah Pembelajaran Mesin. Proyek ini mengimplementasikan teknologi **Computer Vision** untuk mengklasifikasikan 31 jenis rempah-rempah khas Indonesia menggunakan perbandingan arsitektur CNN Custom dan *Transfer Learning*.

---

# 📑 TABLE OF CONTENT
1. [Deskripsi Project](#-deskripsi-project-)
2. [Eksplorasi Dataset](#-eksplorasi-dataset-)
3. [Arsitektur Model](#-arsitektur-model-)
4. [Eksperimen & Pelatihan](#-eksperimen--pelatihan-)
5. [Evaluasi & Performa](#-evaluasi--performa-)
6. [Implementasi Streamlit](#-implementasi-streamlit-)
7. [Struktur Repositori](#-struktur-repositori-)
8. [Biodata](#-biodata-)

---

# 📝 DESKRIPSI PROJECT 📝

### Latar Belakang
Indonesia dikenal sebagai pusat rempah dunia. Namun, identifikasi manual terhadap jenis rempah seringkali sulit dilakukan karena kemiripan visual antar varietas (misalnya antara jahe, lengkuas, dan kencur). Proyek ini hadir sebagai solusi berbasis AI untuk melakukan identifikasi cepat dan akurat melalui media gambar agar mempermudah edukasi dan pengenalan komoditas rempah.

### Tujuan Utama
* Mengembangkan model klasifikasi yang mampu mengenali **31 kelas rempah** secara otomatis.
* Menerapkan teknik **Transfer Learning** untuk meningkatkan akurasi meskipun dengan dataset yang terbatas.
* Membangun aplikasi web interaktif melalui **Streamlit** yang dideploy menggunakan **Ngrok** untuk pengujian real-time.

---

# 📊 EKSPLORASI DATASET 📊

Dataset mencakup variasi gambar dari 31 jenis rempah Indonesia yang diambil dalam berbagai kondisi pencahayaan dan sudut pandang.

* **Total Kelas**: 31 Kategori (Adas, Kunyit, Kayu Manis, Daun Salam, Ketumbar, dsb).
* **Preprocessing**:
    * **Resizing**: Semua citra diubah ukurannya menjadi **128 x 128** piksel.
    * **Normalization**: Nilai piksel diskalakan ulang ke rentang [0, 1] melalui *scaling* 1/255.

---

# 🏗️ ARSITEKTUR MODEL 🏗️

Proyek ini membandingkan tiga arsitektur Convolutional Neural Network (CNN) berbeda:

1.  **Custom CNN (Model Base)**:
    * Terdiri dari 3 lapisan Konvolusi (`Conv2D`) yang diikuti oleh `MaxPooling2D` dan `Dense Layer`.
    * Berperan sebagai baseline untuk mengukur performa model sederhana tanpa pre-trained weights.
2.  **VGG16 (Transfer Learning)**:
    * Arsitektur CNN yang dalam dengan 16 lapisan berbobot.
    * Memanfaatkan fitur yang sudah dipelajari dari dataset ImageNet untuk mengenali tekstur rempah yang kompleks.
3.  **MobileNetV2 (Transfer Learning)**:
    * Arsitektur yang dioptimalkan untuk performa tinggi dengan beban komputasi rendah.
    * Menggunakan *depthwise separable convolutions* yang sangat efisien untuk klasifikasi citra.

---

# 📈 EVALUASI & PERFORMA 📈

Berdasarkan hasil pengujian pada *Validation Set*, MobileNetV2 menunjukkan keunggulan signifikan dibandingkan arsitektur lainnya:

| Arsitektur Model | Accuracy | Loss | Keterangan |
| :--- | :---: | :---: | :--- |
| **Custom CNN (Base)** | ~57% | Tinggi | Mengalami overfitting yang signifikan. |
| **VGG16** | ~70% | Sedang | Performa cukup baik namun model sangat berat. |
| **MobileNetV2** | **~83%** | **Rendah** | **Model Terbaik.** Paling stabil, akurat, dan efisien. |

### Visualisasi Performa
Berikut adalah grafik pelatihan dan matriks kebingungan (*Confusion Matrix*) untuk model terbaik:

<p align="center">
  <img src="Assets/Akurasi_Grafik.png" width="45%" title="Grafik Akurasi">
  <img src="Assets/CM_MobileNet.png" width="45%" title="Confusion Matrix MobileNetV2">
</p>

---

# 💻 IMPLEMENTASI STREAMLIT 💻

Aplikasi web dikembangkan agar pengguna dapat melakukan prediksi secara instan dengan tiga langkah mudah:
1.  **Langkah 1**: Unggah gambar rempah (JPG/PNG/JPEG).
2.  **Langkah 2**: Pilih arsitektur model di Sidebar (MobileNetV2 direkomendasikan).
3.  **Langkah 3**: Sistem akan memproses citra dan menampilkan nama rempah beserta skor tingkat keyakinannya.

<p align="center">
  <img src="Assets/Preview_Web.png" width="80%" alt="Preview Aplikasi">
</p>

---

# 📂 STRUKTUR REPOSITORI 📂

```text
├── Assets/             # Screenshot aplikasi, grafik akurasi, dan Confusion Matrix
├── Docs/               # Laporan tugas akhir (PDF)
├── Model/              # Folder penyimpanan file model (.h5)
├── Notebook/           # File .ipynb (Proses EDA, Training, dan Evaluasi)
├── App.py              # File script utama aplikasi Streamlit
├── requirements.txt    # Daftar library Python (TensorFlow, Streamlit, dll)
└── README.md           # Dokumentasi utama proyek
