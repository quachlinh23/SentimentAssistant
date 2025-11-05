import streamlit as st
from config.settings import APP_TITLE, APP_SOLOGAN

def css_ui():
    st.markdown("""
    <style>
        /* ===== TOÀN CỤC ===== */
        .main-title {
            text-align: center !important;
            font-weight: 800 !important;
            font-size: 2.8rem !important;
            background: linear-gradient(90deg, #1e40af, #3b82f6) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            margin: 0 0 0.5rem 0 !important;
            letter-spacing: -0.5px !important;
        }

        .slogan {
            text-align: center !important;
            font-size: 1.15rem !important;
            color: #64748b !important;
            font-style: italic !important;
            margin: -0.5rem 0 2.5rem 0 !important;
            letter-spacing: 0.4px !important;
            opacity: 0.9;
        }

        /* ===== Ô NHẬP LIỆU ===== */
        .stTextArea > div > div > textarea {
            border-radius: 18px !important;
            padding: 16px 18px !important;
            font-size: 1.1rem !important;
        }

        /* Placeholder đẹp */
        .stTextArea textarea::placeholder {
            color: #94a3b8 !important;
            font-style: italic;
            opacity: 0.8;
        }

        /* ===== NÚT PHÂN LOẠI ===== */
        div.stButton {
            display: flex !important;
            justify-content: flex-end !important;
            margin-top: 1.5rem !important;
        }

        .stButton > button {
            border-radius: 14px !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            height: 52px !important;
            width: 170px !important;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
            transition: all 0.3s ease !important;
            position: relative;
            overflow: hidden;
        }

        .stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4) !important;
        }

        .stButton > button:active {
            transform: translateY(-1px) !important;
        }

        /* Hiệu ứng khi click */
        .stButton > button::after {
            content: '';
            position: absolute;
            width: 0; height: 0;
            background: rgba(255,255,255,0.3);
            border-radius: 50%;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .stButton > button:active::after {
            width: 300px; height: 300px;
        }

        /* ===== TIÊU ĐỀ LỊCH SỬ ===== */
        .titleHistory {
            font-size: 1.9rem !important;
            font-weight: 700 !important;
            color: #1e293b !important;
            margin: 0.5rem 0 1rem 0 !important;
            padding-bottom: 0.5rem;
            display: inline-block;
        }

        /* ===== CẢI THIỆN CHUNG ===== */
        .block-container {
            padding-top: 2rem !important;
        }

        /* Ẩn header/footer mặc định */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Responsive cho mobile */
        @media (max-width: 640px) {
            .main-title {font-size: 2.2rem !important;}
            .slogan {font-size: 1rem !important;}
            .stButton > button {width: 100% !important;}
        }
    </style>
    """, unsafe_allow_html=True)

def header_ui():
    st.markdown(f"<h1 class='main-title'>{APP_TITLE}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='slogan'>{APP_SOLOGAN}</p>", unsafe_allow_html=True)