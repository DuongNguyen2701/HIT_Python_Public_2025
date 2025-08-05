# Đọc dòng đầu tiên: số lượng phần tử n và m
n, m = map(int, input().split())

# Đọc dòng thứ hai: mảng gồm n phần tử
arr = list(map(int, input().split()))

# Đọc dòng thứ ba và tư: tập hợp A và B
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Khởi tạo mức độ hạnh phúc ban đầu
happiness = 0

# Duyệt qua từng phần tử trong mảng
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1
    # Nếu không thuộc A hay B thì không thay đổi

# In ra mức độ hạnh phúc cuối cùng
print(happiness)
