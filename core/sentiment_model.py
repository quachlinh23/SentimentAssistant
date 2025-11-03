# core/sentiment_model.py
import streamlit as st
from transformers import pipeline
from config.settings import MODEL_NAME
import re

# Từ điển PHỤ TRỢ – CHỈ CAN THIỆP KHI MODEL SAI RÕ RÀNG
POSITIVE_BOOST = {"rất", "tuyệt vời", "siêu hay", "ngon tuyệt", "thích", "nhiều lắm"}
NEGATIVE_BOOST = {"rất tệ", "dở", "ghét", "buồn", "mệt"}

@st.cache_resource
def load_pipeline():
    return pipeline("sentiment-analysis", model=MODEL_NAME, tokenizer=MODEL_NAME, device=-1)

def predict_sentiment(text: str):
    if not text.strip():
        return "NEUTRAL", 0.0

    try:
        with st.spinner("Đang phân tích bằng PhoBERT..."):
            result = load_pipeline()(text)[0]
            label = result['label']
            score = result['score']

            # BƯỚC 1: ĐỌC LABEL
            if '1' in label or 'POS' in label.upper():
                model_pred = "POSITIVE"
            elif '0' in label or 'NEG' in label.upper():
                model_pred = "NEGATIVE"
            else:
                model_pred = "NEUTRAL"

            # BƯỚC 2: NGƯỠNG NGHIÊM NGẶT – CHỈ TIN NẾU score ≥ 0.6
            if score < 0.6:
                # DÙNG TỪ ĐIỂN ĐỂ CHỐNG SAI
                text_lower = text.lower()
                if any(re.search(r'\b' + re.escape(phrase) + r'\b', text_lower) for phrase in POSITIVE_BOOST):
                    return "POSITIVE", 0.85
                if any(re.search(r'\b' + re.escape(phrase) + r'\b', text_lower) for phrase in NEGATIVE_BOOST):
                    return "NEGATIVE", 0.85
                # NẾU KHÔNG CÓ TỪ ĐIỂN → NEUTRAL
                return "NEUTRAL", score

            # BƯỚC 3: MODEL TỰ TIN → TRẢ KẾT QUẢ
            return model_pred, score

    except Exception as e:
        st.error("Lỗi model: " + str(e))
        return "NEUTRAL", 0.0