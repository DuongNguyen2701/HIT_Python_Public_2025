def calculate(operation, *args):
    if not args:  # nếu không có số nào được truyền vào
        return "No numbers provided"

    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else:
        return "Invalid operation"


# Nhập dữ liệu từ bàn phím 
operation = input("Nhập phép toán (add, multiply, max, min): ")

# Người dùng nhập dãy số, cách nhau bởi khoảng trắng
numbers = list(map(int, input("Nhập các số, cách nhau bởi khoảng trắng: ").split()))

# Gọi hàm với *numbers để giải nén danh sách thành nhiều tham số
print("Kết quả:", calculate(operation, *numbers))
