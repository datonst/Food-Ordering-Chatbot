# Mục lục

1. chatbot-TTNM ứng dụng đặt đồ ăn bằng giọng nói
2. Thiết lập ứng dụng trọng máy
3. Cách thức hoạt động
---
---
# 1. chatbot-TTNM ứng dụng đặt đồ ăn bằng giọng nói

chatbot-TTNM là một dự án chatbot đơn giản được thiết kế cho khóa học TTNM. Chatbot được xây dựng bằng Llama và tích hợp các kỹ thuật Xử lý ngôn ngữ tự nhiên (NLP) cơ bản.

Đây là một Web hỗ trợ đặt đồ ăn cho người khiếm khuyết về tay với ới các tính năng như điều khiển bằng giọng nói và phản hồi âm thanh, web này sẽ giúp nâng cao chất lượng cuộc sống của người khuyết tật, tạo điều kiện để họ tự lập và hòa nhập hơn trong cộng đồng

---
---
# 2. Thiết lập ứng dụng trọng máy

## 2.1. Chuẩn bị môi trường
  - Đảm bảo bạn đã cài đặt các công cụ sau trên máy của mình:
    + Python 3.8+
    + Git để sao chép mã nguồn.
    + Node.js (nếu dự án yêu cầu giao diện web).
    + Docker (tùy chọn, nếu bạn muốn triển khai trong container).
      
## 2.2 Clone repo
  -  Tải mã nguồn về máy của bạn bằng lệnh sau: git clone https://github.com/datonst/chatbot-TTNM

## 2.3. Cài đặt dependencies
  - Sử dụng pip:
    + Bước 1: python3 -m venv venv
    + Bước 2: source venv/bin/activate  # Trên macOS/Linux hoặc venv\Scripts\activate  # Trên Windows
    + Bước 3: pip install -r requirements.txt
  - Nếu dự án sử dụng Poetry:
    + poetry install
      
### 2.3.1. Triển khai trên môi trường thực tế
  - Docker: Nếu có file Dockerfile, build container:
    + docker build -t llm-food-delivery .
    + docker run -p 8000:8000 llm-food-delivery
  - Cloud Services:
    + Heroku, AWS Elastic Beanstalk, hoặc Google Cloud Run.
    + Đảm bảo upload .env và cấu hình đúng biến môi trường.

# 3. Cách thức hoạt động
