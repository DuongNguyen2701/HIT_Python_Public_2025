# Nhập số lương
luong = int(input("Hãy nhập số lương trong 1 tháng của bạn: "))

# Nếu lương là 15 triệu
if luong == 15000000:
    thue = luong * 0.3
    ThuNhap = luong - thue
    print("Thuế:", int(thue))
    print("Thu nhập:", int(ThuNhap))

# Nếu lương từ 7 triệu đến 15 triệu
if 7000000 <= luong < 15000000:
    thue = luong * 0.2
    ThuNhap = luong - thue
    print("Thuế:", int(thue))
    print("Thu nhập:", int(ThuNhap))

# Nếu lương dưới 7 triệu
if luong < 7000000:
    thue = luong * 0.1
    ThuNhap = luong - thue
    print("Thuế:", int(thue))
    print("Thu nhập:", int(ThuNhap))


    