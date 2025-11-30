# core/sentiment_model.py
import streamlit as st
from transformers import pipeline
from config.settings import MODEL_NAME, NEUTRAL_DEFAULT

# --- Từ điển cơ bản ---
POSITIVE_WORDS = ["vui", "tốt", "tuyệt", "đẹp", "thích", "yêu", "hay"]
NEGATIVE_WORDS = ["dở", "tệ", "xấu", "buồn", "mệt", "ghét", "không"]

# --- Tải mô hình phân tích cảm xúc ---
@st.cache_resource
def load_pipeline():
    device = 0 if __import__("torch").cuda.is_available() else -1
    return pipeline("sentiment-analysis", model=MODEL_NAME, device=device)

# --- Dự đoán cảm xúc ---
def predict_sentiment(text: str):
    if not text or len(text.strip()) < 3:
        return {"text": text, "sentiment": "NEUTRAL", "score": 0.0}

    try:
        result = load_pipeline()([text])[0]
        label = result.get('label', '').upper()
        score = result.get('score', 0.0)

        # --- Mapping nhãn đúng với model sentiment tiếng Việt ---
        label_map = {
            "LABEL_0": "NEGATIVE",
            "LABEL_1": "NEUTRAL",
            "LABEL_2": "POSITIVE"
        }
        sentiment = label_map.get(label, "NEUTRAL")

        # --- Nếu score thấp hơn ngưỡng, xem là NEUTRAL ---
        if score < NEUTRAL_DEFAULT:
            sentiment = "NEUTRAL"

        # --- Fallback từ điển nếu sentiment vẫn là NEUTRAL ---
        if sentiment == "NEUTRAL":
            text_lower = text.lower()
            if any(word in text_lower for word in POSITIVE_WORDS):
                sentiment = "POSITIVE"
            elif any(word in text_lower for word in NEGATIVE_WORDS):
                sentiment = "NEGATIVE"

        return {
            "text": text,
            "sentiment": sentiment,
            "score": round(score, 4),
        }

    except Exception as e:
        st.error(f"Lỗi model: {e}")
        return {"text": text, "sentiment": "NEUTRAL", "score": 0.0}
