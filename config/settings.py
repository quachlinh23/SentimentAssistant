# config/settings.py
from pathlib import Path

# Đường dẫn
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "sentiments.db"

# Model (chỉ dùng 2 model được cho phép)
MODEL_NAME = "wonrax/phobert-base-vietnamese-sentiment"  # Ưu tiên tiếng Việt

# Ngưỡng
NEUTRAL_DEFAULT_THRESHOLD = 0.5

#Từ viết tắt
ABBREVIATIONS = {
    "rat": "rất", "dc": "được", "k": "không", "ko": "không",
    "hnay": "hôm nay", "t": "tôi", "r": "rồi", "v": "và",
    "ns": "nói", "sp": "sản phẩm"
}

# Giao diện
HISTORY_LIMIT = 50
APP_TITLE = "Trợ Lý Phân Loại Cảm Xúc Tiếng Việt"
APP_SOLOGAN = "Phân tích cảm xúc tiếng Việt — nhanh, chính xác và thông minh"
MIN_CHARACTERS = 5
MAX_CHARACTERS = 50

