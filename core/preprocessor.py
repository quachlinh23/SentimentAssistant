# core/preprocessor.py
import re
from underthesea import word_tokenize
from config.settings import ABBREVIATIONS, MIN_CHARACTERS, MAX_CHARACTERS

# === Tiền xử lý văn bản ===
# Loại bỏ khoảng trắng thừa 
# Chuyển chữ hoa thành chữ thường
# Mở rộng từ viết tắt
def normalize_text(text: str) -> str:
    text = text.strip().lower()
    for abbr, full in ABBREVIATIONS.items():
        text = re.sub(rf'\b{abbr}\b', full, text, flags=re.IGNORECASE)
    return re.sub(r'\s+', ' ', text).strip()

# === Hàm tiền xử lý chính === 
# Tiền xử lý văn bản đầu vào
# chuẩn hóa và token hóa thành từ riêng lẻ
def preprocess_text(text: str) -> str | None:
    if len(text) < MIN_CHARACTERS:
        return None
    if len(text) > MAX_CHARACTERS:
        text = text[:MAX_CHARACTERS]

    text = normalize_text(text)
    try:
        tokens = word_tokenize(text)
        return " ".join(tokens)
    except:
        return text