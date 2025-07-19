# Nhập tháng và năm
thang = int(input("Hãy nhập tháng: "))
while (thang < 1) or (thang > 12):
    thang = int(input("Hãy nhập tháng hợp lệ: "))
nam = int(input("Hãy nhập năm: " ))

# Xét năm nhuận
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    if thang == 2:
        print("29")
    elif thang in {1, 3, 5, 7, 8, 10, 12}:
        print("31")
    else:
        print("30")

#Xét năm không nhuận
else:
    if thang == 2:
        print("28")
    elif thang in {1, 3, 5, 7, 8, 10, 12}:
        print("31")
    else:
        print("30")
    


