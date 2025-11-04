# core/preprocessor.py
from underthesea import word_tokenize
from unidecode import unidecode
import re
from config.settings import ABBREVIATIONS


def restore_diacritics(text: str) -> str:
    no_diacritic = unidecode(text)
    try:
        # Tách từ → ghép lại bằng khoảng trắng
        tokens = word_tokenize(no_diacritic)
        return " ".join([token for token, _ in tokens])
    except:
        return text

def preprocess_text(text: str) -> str:
    if not text:
        return ""

    text = text.strip()

    # 1. Dịch không dấu
    text = restore_diacritics(text)

    # 2. Chữ thường
    text = text.lower()

    # 3. Thay viết tắt
    for abbr, full in ABBREVIATIONS.items():
        text = re.sub(r'\b' + re.escape(abbr) + r'\b', full, text)

    # 4. Tách từ
    try:
        tokens = word_tokenize(text)
        text = " ".join([token for token, _ in tokens])
    except:
        pass

    # 5. CHỈ XÓA "chứ" KHI DO UNDERTHESEA TỰ THÊM
    text = re.sub(r'\bquá\s+chứ\b(?=[\s\.,;!\?]|$)', 'quá', text, flags=re.IGNORECASE)

    # 6. Giới hạn 50 ký tự
    if len(text) > 50:
        text = text[:47] + "..."

    return text.strip()