# utils/helpers.py
import streamlit as st

def format_percentage(score: float) -> str:
    return f"{score:.1%}"

def clean_input(text: str) -> str:
    return " ".join(text.strip().split())

def validate_input(text: str, min_chars: int, max_chars: int):
    """Kiểm tra độ dài và tính hợp lệ của câu nhập"""
    text = text.strip()
    if not text:
        st.warning("Vui lòng nhập nội dung trước khi phân tích.")
        st.stop()
    if len(text) < min_chars:
        st.warning(f"Câu phải ≥ {min_chars} ký tự!")
        st.stop()
    if len(text) > max_chars:
        st.warning(f"Câu phải ≤ {max_chars} ký tự!")
        st.stop()
