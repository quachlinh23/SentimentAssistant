# ui/streamlit_app.py
import streamlit as st
from utils.helpers import show_sentiment
from core.preprocessor import preprocess_text
from core.sentiment_model import predict_sentiment
from core.database import save_result, get_history
from config.settings import (
    APP_TITLE, HISTORY_LIMIT, MIN_CHARACTERS, MAX_CHARACTERS
)

def run_app():
    st.set_page_config(page_title=APP_TITLE, page_icon="smiling face")
    st.title(APP_TITLE)
    st.markdown("### Nhập câu tiếng Việt → Phân loại cảm xúc")

    user_input = st.text_area(
        "Câu cần phân tích:",
        height=120,
        placeholder="VD: Hôm nay tôi rất vui"
    )

    if st.button("Phân loại", type="primary"):
        raw_text = user_input.strip()

        # BƯỚC 3: Hợp nhất & xử lý lỗi
        if not raw_text:
            st.error("Vui lòng nhập nội dung!")
            st.stop()

        if len(raw_text) < MIN_CHARACTERS:
            st.error(f"Câu phải ≥ {MIN_CHARACTERS} ký tự!")
            st.stop()

        if len(raw_text) > MAX_CHARACTERS:
            st.error(f"Câu phải ≤ {MAX_CHARACTERS} ký tự!")
            st.stop()

        # BƯỚC 1 + 2: Tiền xử lý + Phân loại
        with st.spinner("Đang xử lý..."):
            processed = preprocess_text(raw_text)
            sentiment, score = predict_sentiment(processed)

        # Hiển thị kết quả
        show_sentiment(sentiment, score)

        # Tạo dictionary (yêu cầu đồ án)
        result_dict = {"text": processed, "sentiment": sentiment}
        with st.expander("Xem chi tiết (dictionary)"):
            st.json(result_dict)

        # Lưu vào SQLite
        save_result(processed, sentiment)

    # Hiển thị lịch sử
    if st.checkbox(f"Hiển thị lịch sử ({HISTORY_LIMIT} kết quả gần nhất)"):
        history = get_history(HISTORY_LIMIT)
        if history:
            for text, sentiment, ts in history:
                st.markdown(f"**{ts}** | `{text}` → **{sentiment}**")
        else:
            st.info("Chưa có dữ liệu.")