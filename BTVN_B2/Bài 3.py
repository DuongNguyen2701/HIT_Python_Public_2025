# Nhập n
n = int(input("Hãy nhập số nguyên dương n: "))

# Tránh số âm
while n < 0:
    n = int(input("Hãy nhập chữ số nguyên dương n: "))

# Đặt biến a có giá trị là n dưới dạng xâu ký tự
a = str(n)

# Đặt biến SoChuSo có giá trị tương đương với số ký tự của xâu ký tự a
SoChuSo = len(a)

# Đặt biến Tong có giá trị tổng của các ký tự được chuyển về định dạng số nguyên (biến kt có giá trị là xâu có 1 ký tự thuộc biến a) trong xâu ký tự a
Tong = sum(int(kt) for kt in a)


print("Số chữ số:", SoChuSo)
print("Tổng chữ số:", Tong)

