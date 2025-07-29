k = int(input("Nhập số lượng phần tử k: "))
a = []
for i in range(k):
    gt = int(input(f"a[{i}] = "))
    a.append(gt)

n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if k < n * m:
    print("NO")
else:
    X = []
    ChiSo = 0
    for i in range(n):
        hang = []
        for j in range(m):
            hang.append(a[ChiSo])
            ChiSo += 1
        X.append(hang)

    for hang in X:
        print(hang)
