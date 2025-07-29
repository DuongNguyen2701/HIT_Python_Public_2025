# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử N: "))

# Nhập list gồm n phần tử là số nguyên
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    a.append(x)

print("List ban đầu:", a)

# Nhập số X và đếm số lần xuất hiện trong list
x = int(input("Nhập số X để kiểm tra số lần xuất hiện: "))
print(f"Số {x} xuất hiện {a.count(x)} lần trong list.")

# Thay thế các phần tử từ vị trí 2 -> 7 (tức index 1 đến 6) nếu đủ dài
if len(a) >= 7:
    a[1:7] = [8, 5, 4, 0, 1, 3]
    print("List sau khi thay thế:", a)
else:
    print("List không đủ dài để thay thế từ vị trí 2 -> 7.")

# Tìm số lớn nhất và nhỏ nhất
print("Số lớn nhất trong list:", max(a))
print("Số nhỏ nhất trong list:", min(a))

# Nhập số Y và chèn vào đầu list
y = int(input("Nhập số Y để chèn vào đầu list: "))
a.insert(0, y)
print("List sau khi chèn Y vào đầu:", a)

# Kiểm tra thứ tự sắp xếp
if a == sorted(a):
    print("TĂNG")
elif a == sorted(a, reverse=True):
    print("GIẢM")
else:
    print("NO")
