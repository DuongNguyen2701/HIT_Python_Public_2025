# Nhập input từ người dùng
a = input().split()

# Nối chuỗi lại thành 1 chuỗi dài
chuoi = ''.join(a)

# Duyệt từng ký tự và thêm vào kết quả nếu chưa có
kq = []
for ch in chuoi:
    if ch not in kq:
        kq.append(ch)

# In kết quả
print(kq)
