# Khởi tạo tập hợp mã sinh viên tại hai bàn tiếp nhận
ban_1 = {"SV001", "SV002", "SV003", "SV004"}
ban_2 = {"SV003", "SV004", "SV005", "SV006"}

# In thông tin hai tập hợp
print("Danh sách sinh viên đăng ký tại bàn 1:", ban_1)
print("Danh sách sinh viên đăng ký tại bàn 2:", ban_2)

# 1. Kiểm tra sinh viên đăng ký ở cả hai bàn
sinh_vien_ca_hai = ban_1.intersection(ban_2)
if sinh_vien_ca_hai:
    print("Sinh viên đăng ký ở cả hai bàn:", sinh_vien_ca_hai)
else:
    print("Không có sinh viên nào đăng ký ở cả hai bàn.")

# 2. Danh sách tổng hợp sinh viên đã đăng ký tại cả hai bàn (hợp)
tong_hop = ban_1.union(ban_2)
print("Danh sách tổng hợp sinh viên đã đăng ký:", tong_hop)

# 3. Sinh viên đăng ký ở bàn 1 nhưng không ở bàn 2
chi_ban_1 = ban_1.difference(ban_2)
print("Sinh viên đăng ký tại bàn 1 nhưng không đăng ký tại bàn 2:", chi_ban_1)
