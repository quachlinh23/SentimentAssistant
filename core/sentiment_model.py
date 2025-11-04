# core/sentiment_model.py
import streamlit as st
from transformers import pipeline
from config.settings import (
    MODEL_NAME, 
    NEUTRAL_DEFAULT_THRESHOLD
)
import re
import torch

@st.cache_resource
def load_pipeline():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline(
        "sentiment-analysis", 
        model=MODEL_NAME, 
        tokenizer=MODEL_NAME, 
        device=device
    )

def predict_sentiment(text: str):
    if not text.strip():
        return {"text": text, "sentiment": "NEUTRAL", "score": 0.0}

    try:
        with st.spinner("Đang phân tích bằng PhoBERT..."):
            result = load_pipeline()(text)[0]
            label = result['label'].upper()
            score = result['score']

            # --- BƯỚC 1: Dựa vào nhãn model
            if 'POS' in label or '1' in label:
                sentiment = "POSITIVE"
            elif 'NEG' in label or '0' in label:
                sentiment = "NEGATIVE"
            else:
                sentiment = "NEUTRAL"

            # --- BƯỚC 2: Nếu độ tin cậy thấp hơn ngưỡng ở setting, chuyển thành NEUTRAL
            if score < NEUTRAL_DEFAULT_THRESHOLD:
                sentiment = "NEUTRAL"

            # --- BƯỚC 3: Trả về kết quả
            return {
                "text": text,
                "sentiment": sentiment,
                "score": round(score, 4), # làm tròn đến 4 chữ số thập phân
            }

    except Exception as e:
        st.error("Lỗi phân tích: " + str(e))
        return {"text": text, "sentiment": "NEUTRAL", "score": 0.0}
