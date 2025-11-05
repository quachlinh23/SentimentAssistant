# config/settings.py
from pathlib import Path

# --- Đường dẫn cơ sở dữ liệu ---
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "sentiments.db"

# --- Định nghĩa model ---
MODEL_NAME = "wonrax/phobert-base-vietnamese-sentiment"

# --- Ngưỡng độ tin cậy để phân loại NEUTRAL ---
NEUTRAL_DEFAULT = 0.5

# --- Định nghĩa danh sách các từ viết tắt ---
ABBREVIATIONS = {
    "rat": "rất", "dc": "được", "k": "không", "ko": "không",
    "hnay": "hôm nay", "t": "tôi", "r": "rồi", "v": "và",
    "ns": "nói", "sp": "sản phẩm"
}

# --- Giới hạn ký tự cho phân tích ---
HISTORY_LIMIT = 50
MIN_CHARACTERS = 5
MAX_CHARACTERS = 50

# --- Cấu hình giao diện của ứng dụng ---
APP_TITLE = "Trợ Lý Phân Loại Cảm Xúc Tiếng Việt"
APP_SOLOGAN = "Phân tích cảm xúc tiếng Việt — nhanh, chính xác và thông minh"
