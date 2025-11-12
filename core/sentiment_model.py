# core/sentiment_model.py
import streamlit as st
from transformers import pipeline
from config.settings import MODEL_NAME, NEUTRAL_DEFAULT

# --- Từ điển cơ bản ---
POSITIVE_WORDS = ["vui", "tốt", "tuyệt", "đẹp", "thích", "yêu", "hay"]
NEGATIVE_WORDS = ["dở", "tệ", "xấu", "buồn", "mệt", "ghét", "không"]

@st.cache_resource
def load_pipeline():
    device = 0 if __import__("torch").cuda.is_available() else -1
    return pipeline("sentiment-analysis", model=MODEL_NAME, device=device)

def predict_sentiment(text: str):
    if not text or len(text.strip()) < 3:
        return {"text": text, "sentiment": "NEUTRAL", "score": 0.0}

    try:
        result = load_pipeline()([text])[0]
        label = result.get('label', '').upper()
        score = result.get('score', 0.0)
        used_rule = "model"

        # --- Dựa vào điểm trước, nhãn sau ---
        if score <= NEUTRAL_DEFAULT:  
            sentiment = "NEUTRAL"
        else:
            if 'POS' in label or label.endswith('2'):
                sentiment = "POSITIVE"
            elif 'NEG' in label or label.endswith('0'):
                sentiment = "NEGATIVE"
            else:
                sentiment = "NEUTRAL"

        # --- Nếu model không tự tin, dùng từ điển ---
        if sentiment == "NEUTRAL":
            text_lower = text.lower()
            if any(word in text_lower for word in POSITIVE_WORDS):
                sentiment = "POSITIVE"
                used_rule = "dictionary"
            elif any(word in text_lower for word in NEGATIVE_WORDS):
                sentiment = "NEGATIVE"
                used_rule = "dictionary"

        return {
            "text": text,
            "sentiment": sentiment,
            "score": round(score, 4),
            "used_rule": used_rule
        }

    except Exception as e:
        st.error(f"Lỗi model: {e}")
        return {"text": text, "sentiment": "NEUTRAL", "score": 0.0}
