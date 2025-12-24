import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Klasifikasi Rempah Indonesia", layout="centered")

st.title("🌿 Sistem Klasifikasi Rempah Indonesia")
st.write("Unggah gambar rempah untuk mengetahui jenisnya menggunakan Model AI.")

# 2. Fungsi Load Model (Agar lebih ringan)
@st.cache_resource
def load_all_models():
    # Pastikan path ini sesuai dengan tempat Anda menyimpan model di Sel 16
    base = tf.keras.models.load_model('/content/drive/MyDrive/UAP Machine Learning/Models/model_base_rempah.h5')
    mnet = tf.keras.models.load_model('/content/drive/MyDrive/UAP Machine Learning/Models/model_mobilenet_rempah.h5')
    vgg = tf.keras.models.load_model('/content/drive/MyDrive/UAP Machine Learning/Models/model_vgg16_rempah.h5')
    return base, mnet, vgg

# 3. Daftar Kelas (Sesuaikan dengan urutan folder Anda)
class_names = ['adas', 'andaliman', 'asam jawa', 'bawang bombai', 'bawang merah', 'bawang putih',
               'biji ketumbar', 'bukan rempah', 'bunga lawang', 'cengkeh', 'daun jeruk',
               'daun kemangi', 'daun ketumbar', 'daun salam', 'jahe', 'jinten', 'kapulaga',
               'kayu manis', 'kayu secang', 'kemiri', 'kemukus', 'kencur', 'kluwek', 'kunyit',
               'lada', 'lengkuas', 'pala', 'saffron', 'serai', 'vanili', 'wijen']

# Load model
try:
    model_base, model_mnet, model_vgg = load_all_models()
    st.sidebar.success("Semua Model Berhasil Dimuat!")
except:
    st.sidebar.error("Model tidak ditemukan. Pastikan sudah menjalankan Sel 16.")

# 4. Sidebar untuk Pemilihan Model
st.sidebar.title("Pengaturan Model")
selected_model_name = st.sidebar.selectbox(
    "Pilih Model untuk Prediksi:",
    ("Neural Network Base", "MobileNetV2 (Terbaik)", "VGG16")
)

# 5. Input Data (Upload Gambar)
uploaded_file = st.file_uploader("Pilih Gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan Gambar
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_container_width=True)

    # Preprocessing
    img = image.resize((128, 128))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Pilih model yang digunakan
    if selected_model_name == "Neural Network Base":
        model = model_base
    elif selected_model_name == "MobileNetV2 (Terbaik)":
        model = model_mnet
    else:
        model = model_vgg

    # Prediksi
    if st.button("Klasifikasikan Sekarang"):
        with st.spinner('Sedang menganalisis...'):
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])

            result = class_names[np.argmax(predictions)]
            conf = np.max(predictions) * 100

            st.success(f"### Hasil Prediksi: **{result}**")
            st.info(f"Tingkat Keyakinan: {conf:.2f}%")
            st.write(f"Menggunakan Model: {selected_model_name}")
