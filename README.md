# UAP Machine Learning  
## Batik Motif Classification using CNN & Transfer Learning

Repository ini dibuat untuk memenuhi **Ujian Akhir Praktikum (UAP)**  
Mata Kuliah **Pembelajaran Mesin**  
Program Studi Informatika.

---

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk mengklasifikasikan motif batik Indonesia
berdasarkan citra menggunakan **Convolutional Neural Network (CNN)**
dan **Transfer Learning (MobileNetV2)**.  
Model diimplementasikan ke dalam aplikasi web sederhana menggunakan **Streamlit**.

---

## 🧵 Dataset
Dataset berupa citra motif batik dengan **5 kelas**:
1. Jawa_Barat_Megamendung  
2. Kalimantan_Dayak  
3. Papua_Cendrawasih  
4. Solo_Parang  
5. Yogyakarta_Kawung  

Dataset digunakan secara lokal untuk proses training dan evaluasi.

---

## 🔧 Preprocessing
Tahapan preprocessing:
- Resize gambar ke **224 × 224**
- Normalisasi pixel ke **[0–1]**
- Data augmentation (training):
  - Rotation
  - Zoom
  - Horizontal Flip
  - Brightness

---

## 🧠 Model
### 1️⃣ CNN Non-Pretrained
- CNN dari nol
- Digunakan sebagai baseline

### 2️⃣ Transfer Learning (MobileNetV2)
- Pretrained ImageNet
- Fine-tuning layer akhir
- Akurasi lebih tinggi dan stabil

---

## 📊 Evaluasi Model
Evaluasi dilakukan menggunakan:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Confusion Matrix ditampilkan pada dashboard Streamlit.

---

## 🌐 Website Streamlit
Fitur website:
- Upload gambar batik
- Tombol prediksi manual
- Menampilkan:
  - Motif hasil prediksi
  - Confidence score
  - Grafik probabilitas
- Custom UI menggunakan CSS

---

## ▶️ Menjalankan Aplikasi
```bash
pip install -r requirements.txt
streamlit run app.py
