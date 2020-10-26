1. Cài đặt môi trường
	- Sử dung virtualen để tạo môi trường:
	python3 -m venv DATN
	- Vào môi trường ảo đã được cài đặt, có tên là DATN: 
	source DATN/bin/activate
	- Nâng cấp: 
	pip install --upgrade pip setuptools wheel
	- Sử dụng pip để cài đặt các thư viện:
	pip install -r requirment.txt
	
2. Cài đặt code

2.1 Cấu trúc source code
- Crawl_news:
    + listweb.py: chưa biến là 1 dict, lưu trữ phân tích trang của các websites.
    + crawl_news.py: file crawl các bài báo trên các trang được phân tích ở listweb 
- 
2.2 Dữ liệu
Sử dụng Selenium+Chrome Driver để thu thập dữ liệu:
- Kiểm tra version của Google chrome đang sử dụng: 85.0.4183.87
- Download driver Google chrome tương ứng: 
    https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.87/ 
- Giải nén và lưu folder chromedriver_linux64 trong folder Crawl_news

2.3 Web


3. Demo
- B1: crawl data: (Thư mục DATN để ở home/)
	+ Vào môi trường ảo đã được cài đặt, có tên là DATN: source DATN/bin/activate
	+ Vào thư mục Crawl trong DATN: cd DATN/Crawl/
	+ Chạy code crawl dữ liệu trên nhiều trang web: python3 crawl_news.py
