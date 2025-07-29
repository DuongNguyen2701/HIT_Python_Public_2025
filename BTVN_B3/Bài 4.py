# Nhập chuỗi họ tên chưa chuẩn hóa
HoVaTen = input("Nhập họ tên: ")

# Chuẩn hóa: 
# - strip() để xóa khoảng trắng thừa ở đầu/cuối
# - lower() để đưa tất cả về chữ thường
# - split() để tách từng từ
# - capitalize() để viết hoa chữ cái đầu mỗi từ
CacTu = HoVaTen.strip().lower().split()
HoTenChuan = ' '.join([Tu.capitalize() for Tu in CacTu])

# In kết quả
print("Họ tên sau khi chuẩn hóa:", HoTenChuan)
