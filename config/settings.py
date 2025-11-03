# config/settings.py
from pathlib import Path

# Đường dẫn
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "sentiments.db"

# Model (chỉ dùng 2 model được cho phép)
MODEL_NAME = "vinai/phobert-base-v2"  # Ưu tiên tiếng Việt
# MODEL_NAME = "distilbert-base-multilingual-cased"  # Backup nếu cần

# Ngưỡng
POSITIVE_THRESHOLD = 0.7
NEGATIVE_THRESHOLD = 0.3
NEUTRAL_DEFAULT_THRESHOLD = 0.5  # Dùng khi score < 0.5 → NEUTRAL

# Giao diện
HISTORY_LIMIT = 50
APP_TITLE = "Trợ lý Phân Loại Cảm Xúc Tiếng Việt"
MIN_CHARACTERS = 5
MAX_CHARACTERS = 50