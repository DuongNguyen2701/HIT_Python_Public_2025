# Nhập chuỗi s1 và s2
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

# In ra đảo ngược của chuỗi s1
s1_dao = s1[::-1]
print("Đảo ngược chuỗi s1:", s1_dao)

# Nhập 2 số nguyên a và b (1 <= a < b <= len(s2))
a = int(input("Nhập a (1 ≤ a): "))
b = int(input("Nhập b (a < b ≤ độ dài s2): "))

if 1 <= a < b <= len(s2):
    # Đảo ngược chuỗi từ vị trí a đến b (chú ý index bắt đầu từ 0)
    s2_moi = s2[:a] + s2[a:b][::-1] + s2[b:]
    print("Chuỗi s2 sau khi đảo từ vị trí a đến b:", s2_moi)
else:
    print("Giá trị a và b không hợp lệ.")
    s2_moi = s2  # Giữ nguyên s2 nếu a, b không hợp lệ

# Tạo chuỗi s3 là s1 sau khi xóa các ký tự ở vị trí chẵn (tức index chẵn: 0, 2, 4,...)
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print("Chuỗi s1 sau khi xóa ký tự ở vị trí chẵn (s3):", s3)

# Tạo chuỗi s4 là đan xen ký tự của s1 và s2
min_len = min(len(s1), len(s2))
s4 = ''

# Đan xen từng ký tự
for i in range(min_len):
    s4 += s1[i] + s2[i]

# Nếu một chuỗi dài hơn, thêm phần còn lại vào
s4 += s1[min_len:] + s2[min_len:]

print("Chuỗi s4 đan xen từ s1 và s2:", s4)
