# Nhập dữ liệu
a = input("Nhập các số: ")
so = list(map(int, a.split()))

# Đếm tần suất
tan_suat = {}
for n in so:
    tan_suat[n] = tan_suat.get(n, 0) + 1

# Lọc ra các số thỏa điều kiện
kq = []
for n, count in tan_suat.items():
    if count % 5 == 0 and count % 10 != 0:
        kq.append(n)

# In kết quả
print(*kq)
