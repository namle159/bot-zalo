import pandas as pd
# Nhập đường dẫn file excel cần sử dụng:
duong_dan= r"C:\Users\johnlee\Downloads\Plan Gửi - Tổng hợp danh sách list contact_Linkedin, Agency.xlsx" 
# Nhập tên Sheet:
file_mau= pd.read_excel(duong_dan, sheet_name= 'Tuyển dụng')