# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))

# Nhập n xâu ký tự, lưu vào danh sách a
a = []
for i in range(n):
    s = input(f"Nhập phần tử thứ {i+1}: ")
    a.append(s)

# Tạo tuple b từ danh sách a
b = tuple(a)

# In tuple b
print("Tuple b:", b)

# Đếm số lượng phần tử trong b có dạng số (toàn là chữ số)
count = 0
for item in b:
    if item.isdigit():
        count += 1

# In kết quả đếm
print("Số phần tử có dạng số trong tuple b:", count)
