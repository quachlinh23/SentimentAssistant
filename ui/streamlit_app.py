import streamlit as st
from ui.layout import css_ui, header_ui
from ui.events import handel_analysis, show_history
from config.settings import APP_TITLE

def run_app():
    # === Cấu hình trang ===
    st.set_page_config(
        page_title = APP_TITLE, 
        page_icon = "Speech balloon", 
        layout = "centered"
    )

    # === Giao diện chung ===
    css_ui()
    header_ui()

    # === Ô NHẬP LIỆU ===
    user_input = st.text_area(
        label="",
        height=100,
        placeholder="Nhập vào một câu tiếng Việt để phân tích cảm xúc...",
        label_visibility="collapsed",
    )

    # === NÚT PHÂN TÍCH  ===
    if st.button("Phân tích", type="primary"):
        handel_analysis(user_input)
    
    # === Lấy toàn bộ dữ liệu ===
    show_history()
