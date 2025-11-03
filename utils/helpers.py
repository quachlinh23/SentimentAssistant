# utils/helpers.py
import streamlit as st

def format_percentage(score: float) -> str:
    return f"{score:.1%}"

def clean_input(text: str) -> str:
    return " ".join(text.strip().split())



def show_sentiment(sentiment: str, score: float):
    """Hiển thị cảm xúc với màu sắc theo nhãn"""
    if sentiment == "POSITIVE":
        color = "green"
    elif sentiment == "NEGATIVE":
        color = "red"
    else:
        color = "gray"

    st.markdown(f"""
        <p style="color:{color}; font-size:20px;">
            <b>Cảm xúc:</b> {sentiment} | <b>Độ tin cậy:</b> {score:.1%}
        </p>
    """, unsafe_allow_html=True)
