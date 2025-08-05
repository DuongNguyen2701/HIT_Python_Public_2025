#Nhập tuple ban đầu gồm các chuỗi số
chuoi_tuple = ("1", "5", "8", "3", "10")

#Chuyển đổi thành tuple số nguyên
so_tuple = tuple(map(int, chuoi_tuple))

#Tính trung bình cộng
tong = sum(so_tuple)
trung_binh = tong / len(so_tuple)

#In kết quả
print("Tuple sau khi chuyển đổi:", so_tuple)
print("Trung bình cộng:", trung_binh)
