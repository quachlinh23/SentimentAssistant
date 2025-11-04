import streamlit as st
import pandas as pd
from utils.helpers import show_sentiment
from core.preprocessor import preprocess_text
from core.sentiment_model import predict_sentiment
from core.database import save_result, get_history
from config.settings import APP_TITLE, MIN_CHARACTERS, MAX_CHARACTERS, APP_SOLOGAN

def run_app():
    st.set_page_config(page_title=APP_TITLE, page_icon="Speech balloon", layout="centered")

    # === CSS ĐẸP, MƯỢT, CHUẨN ===
    st.markdown("""
    <style>
        /* TIÊU ĐỀ CHÍNH */
        .main-title {
            text-align: center !important;
            font-weight: 700 !important;
            font-size: 2.5rem !important;
            color: black !important;  /* Xanh lá đậm */
            margin: 0 0 1rem 0 !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        /* SLOGAN */
        .slogan {
            text-align: center !important;
            font-size: 1.1rem !important;
            color: #475569 !important;  /* Xám đậm */
            font-style: italic !important;
            margin-top: -0.3rem !important;
            margin-bottom: 2rem !important;
            letter-spacing: 0.3px !important;  /* Giãn nhẹ chữ */
        }
        /* Ô NHẬP LIỆU */
        .stTextArea > div > div > textarea {
            border-radius: 16px !important;
            padding: 14px !important;
            font-size: 1.1rem !important;
            outline: none !important;
        }
        .stTextArea > div > div > textarea:focus {
            outline : none !important;
            box-shadow: none !important;  
            border-color: transparent !important;
        }
        /* NÚT PHÂN LOẠI - CĂN PHẢI */
        div.stButton {
            display: flex !important;
            justify-content: flex-end !important;
            margin-top: 1rem !important;
        }
        .stButton > button {
            border-radius: 12px !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            height: 48px !important;
            width: 160px !important;
            background-color: rgb(24,144,255) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 4px 8px rgba(30, 64, 175, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        .stButton > button:hover {
            opacity: 0.9 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 16px rgba(30, 64, 175, 0.4) !important;
        }

        /* TIÊU ĐỀ LỊCH SỬ */
        .titleHistory {
            font-size: 1.8rem !important;
            font-weight: 600 !important;
            color: black !important;
            margin: 0 0 0 0 !important;
            text-align: left !important;
        }

        /* Placeholder */
        ::placeholder {
            color: #94a3b8 !important;
            font-style: italic;
        }

        /* Ẩn viền focus mặc định trình duyệt */
        textarea:focus { outline: none !important; }
    </style>
    """, unsafe_allow_html=True)

    # === TIÊU ĐỀ CHÍNH, SOLOGAN ===
    st.markdown(f"<h1 class='main-title'>{APP_TITLE}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='slogan'>{APP_SOLOGAN}</p>", unsafe_allow_html=True)

    # === Ô NHẬP LIỆU ===
    user_input = st.text_area(
        label="",
        height=140,
        placeholder="Nhập vào một câu tiếng Việt để phân tích cảm xúc...",
        label_visibility="collapsed"
    )

    # === NÚT PHÂN LOẠI (căn phải tự động) ===
    st.button(
        "Phân loại",
        type="primary",
        use_container_width=False,
        key="analyze"
    )

    # === XỬ LÝ PHÂN TÍCH ===
    if st.session_state.get("analyze", False):
        raw_text = user_input.strip()

        if not raw_text:
            st.warning("Vui lòng nhập nội dung trước khi phân tích.")
            st.stop()
        if len(raw_text) < MIN_CHARACTERS:
            st.warning(f"Câu phải ≥ {MIN_CHARACTERS} ký tự!")
            st.stop()
        if len(raw_text) > MAX_CHARACTERS:
            st.warning(f"Câu phải ≤ {MAX_CHARACTERS} ký tự!")
            st.stop()

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

        # === LỊCH SỬ ===
    st.markdown("---")
    st.markdown('<h2 class="titleHistory">Lịch sử phân tích gần đây</h2>', unsafe_allow_html=True)

    # Lấy toàn bộ dữ liệu
    history = get_history()

    if history:
        df = pd.DataFrame(history, columns=["Câu", "Cảm xúc", "Thời gian"])

        # Lưu giới hạn hiển thị trong session
        if "limit" not in st.session_state:
            st.session_state.limit = 50  # Hiển thị 50 bản ghi đầu tiên

        # Cắt dữ liệu theo giới hạn
        df_display = df.head(st.session_state.limit)

        st.dataframe(
            df_display,
            use_container_width=True,
            hide_index=True,
            height=min(400, 50 + 35 * len(df_display))
        )

        # Hiển thị tổng số bản ghi
        st.markdown(
            f"""
            <div style="text-align: right; font-size: 15px">
                Tổng số bản ghi: <span style="color: red;"><b>{len(df)}</b></span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Nếu còn dữ liệu thì hiển thị nút "Xem thêm"
        if len(df_display) < len(df):
            if st.button("Xem thêm", key="load_more"):
                st.session_state.limit += 50  # Mỗi lần tăng thêm 50
                st.rerun()
        else:
            st.caption("✅ Đã hiển thị toàn bộ dữ liệu.")
    else:
        st.info("Chưa có dữ liệu lịch sử nào được lưu.")
