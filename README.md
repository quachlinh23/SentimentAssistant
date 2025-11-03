# 🧠 Vietnamese Sentiment Assistant

Ứng dụng **Trợ lý phân loại cảm xúc tiếng Việt** sử dụng mô hình Transformer để nhận diện và phân loại cảm xúc trong văn bản tiếng Việt: 
> 🟢 Tích cực (**Positive**) • ⚪ Trung tính (**Neutral**) • 🔴 Tiêu cực (**Negative**)

---

## 📘 Giới thiệu

**SentimentAssistant** là ứng dụng học máy (Machine Learning) giúp **phân tích cảm xúc tiếng Việt** dựa trên mô hình **Transformer**.  
Ứng dụng có khả năng:

-  🧩 Phân loại cảm xúc từ văn bản tiếng Việt.  
-  💾 Lưu trữ kết quả vào cơ sở dữ liệu.  
-  🌐 Hiển thị kết quả trực quan qua giao diện **Streamlit** thân thiện.

---

## ⚙️ Kiến trúc hệ thống

### 📁 Cấu trúc thư mục
<pre> ```
└── 📁SentimentAssistant
    └── 📁config                                # Cấu hình chung của dự án
        └── __pycache__/                        # Tệp biên dịch Python tự động sinh
        ├── __init__.py                         # Khai báo module Python
        ├── settings.py                         # Chứa các thiết lập hệ thống: đường dẫn DB, model, tham số cấu hình
    └── 📁core                                  # Lõi xử lý nghiệp vụ chính (logic chính của ứng dụng)
        └── 📁__pycache__
        ├── __init__.py
        ├── database.py                         # Quản lý kết nối và thao tác với cơ sở dữ liệu SQLite (`sentiments.db`)
        ├── preprocessor.py                     # Xử lý văn bản đầu vào: làm sạch, chuẩn hóa, tách từ, loại bỏ ký tự đặc biệt
        ├── sentiment_model.py                  # Tải và chạy mô hình Transformer (như BERT/DistilBERT) để phân loại cảm xúc
    └── 📁data                                  # Lưu trữ dữ liệu nội bộ
        ├── sentiments.db                       # Cơ sở dữ liệu SQLite lưu lịch sử phân tích
    └── 📁ui                                    # Giao diện người dùng
        └── __pycache__/
        ├── __init__.py
        ├── streamlit_app.py                     # Giao diện web chính của ứng dụng (Streamlit)
    └── 📁utils                                 # Công cụ phụ trợ (helper functions)
        └── 📁__pycache__                       #  Các hàm tiện ích hỗ trợ
        ├── __init__.py
        ├── helpers.py                          # Các hàm tiện ích: ghi log, định dạng đầu ra, ánh xạ nhãn cảm xúc
    ├── app.py                                  # File khởi chạy chính của ứng dụng
    ├── README.md                               # Tài liệu mô tả tổng quan, cài đặt và hướng dẫn sử dụng
    └── requirements.txt                        # Danh sách thư viện Python cần cài để chạy ứng dụng
``` </pre>

## ⚙️ Luồng xử lý (Processing Flow)

Dưới đây là quy trình xử lý tổng thể của **SentimentAssistant**, từ khi người dùng nhập văn bản đến khi kết quả được hiển thị:

<pre> ```
[Đầu vào: Câu tiếng Việt]
            ↓ (Preprocessing)
[Component 1: Tiền xử lý] → Câu đã chuẩn hóa
            ↓(Sentiment Analysis)
[Component 2: Phân loại cảm xúc] → Nhãn (POSITIVE, NEUTRAL, NEGATIVE)
            ↓ (Validation)
[Component 3: Hợp nhất & xử lý lỗi] Đầu ra dictionary hoặc lỗi
            ↓
[Core Engine: Lưu & hiển thị]
``` </pre>

## Công nghệ sử dụng

|       Thành phần             | Phiên bản      |           Mô tả                    |
|------------------------------|----------------|------------------------------------|
| **Python**                   | 3.10           | Ngôn ngữ chính                     |
| **Streamlit**                | 1.38.0         | Xây dựng giao diện web             |
| **PyTorch (CPU)**            | 2.3.0          | Nền tảng deep learning             |
| **Transformers**             | 4.44.0         | Mô hình ngôn ngữ BERT / DistilBERT |
| **TorchVision / TorchAudio** | 0.18.0 / 2.3.0 | Hỗ trợ xử lý dữ liệu               |
| **Underthesea**              | 6.8.0          | Xử lý ngôn ngữ tự nhiên tiếng Việt |
| **SQLite3**                  | Built-in       | Lưu trữ kết quả cảm xúc            |


## Yêu cầu
- Python ≥ 3.8  
- pip (trình quản lý gói Python)  
- Môi trường CPU (không yêu cầu GPU)

## Các bước cài đặt
```bash
# Clone dự án
git clone https://github.com/quachlinh23/SentimentAssistant.git
cd SentimentAssistant

# Cài đặt thư viện
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run app.py