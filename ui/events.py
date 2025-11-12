import streamlit as st
import pandas as pd
from utils.helpers import clean_input, validate_input, show_sentiment
from core.preprocessor import preprocess_text
from core.sentiment_model import predict_sentiment
from core.database import save_result, get_history
from config.settings import MIN_CHARACTERS, MAX_CHARACTERS

def handel_analysis(user_input : str):
    raw_text = clean_input(user_input)
    validate_input(raw_text, MIN_CHARACTERS, MAX_CHARACTERS)

    with st.spinner("Đang phân tích cảm xúc..."):
        processed = preprocess_text(raw_text)
        result = predict_sentiment(processed)

        if not result:
            st.error("Phân tích thất bại!")
            st.stop()

        sentiment = result["sentiment"]
        score = result["score"]

    show_sentiment(sentiment, score)

    with st.expander("Xem chi tiết kết quả", expanded=False):
        st.json({"text": processed, "sentiment": sentiment, "score": score})

    save_result(processed, sentiment)

def show_history():
    """ """
    st.markdown("---")
    st.markdown('<h2 class="titleHistory">Lịch sử phân tích gần đây</h2>', unsafe_allow_html=True)

    history = get_history()

    if not history:
        st.info("Chưa có dữ liệu lịch sử nào được lưu.")
        return

    df = pd.DataFrame(history, columns=["Câu", "Cảm xúc", "Thời gian"])

    if "limit" not in st.session_state:
        st.session_state.limit = 50

    df_display = df.head(st.session_state.limit)

    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True,
        height=min(400, 50 + 35 * len(df_display))
    )

    st.markdown(
        f"""
        <div style="text-align: right; font-size: 15px">
            Tổng số bản ghi: <span style="color: red;"><b>{len(df)}</b></span>
        </div>
        """,
        unsafe_allow_html=True
    )

    if len(df_display) < len(df):
        if st.button("Xem thêm", key="load_more"):
            st.session_state.limit += 50
            st.rerun()
