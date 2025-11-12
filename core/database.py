# core/database.py
import sqlite3
from datetime import datetime
from config.settings import DB_PATH

# === Khởi tạo cơ sở dữ liệu và bảng nếu chưa tồn tại ===
def init_db():
    # === Tạo folder data nếu chưa tồn tại ===
    DB_PATH.parent.mkdir(exist_ok=True) 
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
# === Gọi khi module được import ===
init_db() 

# === Lưu kết quả phân tích vào DB ===
def save_result(text: str, sentiment: str):
    conn = sqlite3.connect(DB_PATH)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "INSERT INTO sentiments (text, sentiment, timestamp) VALUES (?, ?, ?)",
        (text, sentiment, timestamp)
    )
    conn.commit()
    conn.close()

# === Lấy lịch sử đã phân tích từ database ===
def get_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT text, sentiment, timestamp FROM sentiments ORDER BY timestamp DESC"
    )
    history = cursor.fetchall()
    conn.close()
    return history