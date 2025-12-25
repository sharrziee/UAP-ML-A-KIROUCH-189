import streamlit as st
import tensorflow as tf
import numpy as np
import json
from pathlib import Path
from PIL import Image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Batik Motif Classification",
    page_icon="🎨",
    layout="wide"
)

# =====================================================
# PATH
# =====================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "mobilenetv2_best.keras"
CLASSES_PATH = BASE_DIR / "classes.json"
CSS_PATH = BASE_DIR / "assets" / "style.css"
CONF_MATRIX_PATH = BASE_DIR / "assets" / "confusion_matrix.png"

# =====================================================
# LOAD CSS
# =====================================================
if CSS_PATH.exists():
    with open(CSS_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL & CLASSES
# =====================================================
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(f"❌ Model tidak ditemukan:\n{MODEL_PATH}")
        st.stop()
    return tf.keras.models.load_model(MODEL_PATH)

@st.cache_resource
def load_classes():
    if not CLASSES_PATH.exists():
        st.error("❌ classes.json tidak ditemukan")
        st.stop()
    with open(CLASSES_PATH) as f:
        return json.load(f)

model = load_model()
CLASS_NAMES = load_classes()

# =====================================================
# HEADER
# =====================================================
st.markdown(
    """
    <div class="header">
        <h1>🎨 Batik Motif Classification</h1>
        <p>CNN & Transfer Learning (MobileNetV2)</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# MAIN GRID
# =====================================================
container = st.container()
with container:
    col_left, col_right = st.columns([1, 1], gap="large")

    # =========================
    # LEFT: INPUT
    # =========================
    with col_left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("## 🖼️ Input Gambar Batik")
        st.caption("Upload gambar JPG / PNG")

        uploaded_file = st.file_uploader(
            "Upload",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

        image = None
        if uploaded_file:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Preview Gambar Batik", use_container_width=True)

        predict_btn = st.button("🚀 Prediksi Motif Batik", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # RIGHT: OUTPUT
    # =========================
    with col_right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("## 🔍 Hasil Prediksi")

        if uploaded_file and predict_btn:
            # Preprocess
            img = image.resize((224, 224))
            arr = np.array(img) / 255.0
            arr = np.expand_dims(arr, axis=0)

            probs = model.predict(arr, verbose=0)[0]
            pred_idx = int(np.argmax(probs))
            confidence = float(probs[pred_idx])
            pred_label = CLASS_NAMES[pred_idx]

            # NON-CLASS HANDLING
            if confidence < 0.65:
                st.warning("⚠️ Gambar tidak dikenali sebagai motif batik dalam dataset.")
            else:
                st.success(f"**Motif: {pred_label}**")
                st.metric("Confidence", f"{confidence*100:.2f}%")

                st.markdown("### 📊 Detail Probabilitas")
                prob_dict = {
                    CLASS_NAMES[i]: float(probs[i])
                    for i in range(len(CLASS_NAMES))
                }
                st.bar_chart(prob_dict)

        else:
            st.info("Upload gambar lalu klik **Prediksi Motif Batik**")

        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# CONFUSION MATRIX
# =====================================================
st.divider()
with st.expander("📉 Evaluasi Model (Confusion Matrix)"):
    if CONF_MATRIX_PATH.exists():
        st.image(str(CONF_MATRIX_PATH), use_container_width=True)
    else:
        st.warning("File confusion_matrix.png belum tersedia.")
