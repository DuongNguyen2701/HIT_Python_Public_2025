print("Chào mừng tới bia Hà Nội")
print("Chúng tôi đang có khuyến mại cứ 3 vỏ chai bia sẽ được đổi 1 chai bia mới hoàn toàn miễn phí")
print("Mỗi chai bia có giá 28 xu")

# Nhập số xu
Xu = int(input("Hãy nhập số xu bạn có: "))

# Xác định số chai bia có thể mua được bằng xu
SoChaiBia = int(Xu / 28)

# Xác định số chai bia nhận được nhờ khuyến mại
BiaFree = int(SoChaiBia / 3)

# Tổng số chai bia có thể nhận được
Tong = SoChaiBia + BiaFree


print("Số chai bia có thể mua được là:", Tong)