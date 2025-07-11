Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

Bài 2:  Tìm hiểu trước kiến thức buổi 2 về :
- Các kiểu dữ liệu trong Python
- Các toán tử trong Python
- Mệnh đề điều kiện và vòng lặp
- Kiểu dữ liệu True, False


Bài 1:
Vì sao Python được xem là ngôn ngữ thông dịch?
1. Không cần biên dịch trước thành mã máy (machine code):
- Python không tạo ra file .exe hoặc mã máy chạy trực tiếp. Thay vào đó, mã nguồn Python (.py) được chạy trực tiếp bởi trình thông dịch (interpreter).

2. Chạy qua trình thông dịch (interpreter):
- Khi chạy một chương trình Python, trình thông dịch sẽ đọc từng dòng mã, chuyển sang bytecode, sau đó thực thi ngay.

3. Tồn tại file bytecode (.pyc) là kết quả trung gian:
- Python thực tế biên dịch mã nguồn thành bytecode (dạng trung gian, không phải mã máy).
- Nhưng bytecode vẫn cần được trình thông dịch Python thực thi, không chạy trực tiếp trên CPU như mã máy.

Bài 2:

##  1. CÁC KIỂU DỮ LIỆU TRONG PYTHON

- `int`     : Số nguyên (ví dụ: `1`, `-5`, `0`)
- `float`   : Số thực (ví dụ: `3.14`, `-2.0`)
- `str`     : Chuỗi ký tự (ví dụ: `"Hello"`, `'abc'`)
- `bool`    : Kiểu logic `True` / `False`
- `list`    : Danh sách có thể thay đổi (ví dụ: `[1, 2, 3]`)
- `tuple`   : Bộ dữ liệu không thay đổi (ví dụ: `(1, 2)`)
- `dict`    : Từ điển (ví dụ: `{"ten": "An", "tuoi": 20}`)
- `set`     : Tập hợp không trùng lặp (ví dụ: `{1, 2, 3}`)

**Ví dụ:**
```python
x = 5
print(type(x))  # <class 'int'>
```

---

##  2. CÁC TOÁN TỬ TRONG PYTHON

###  Toán tử số học:
| Toán tử | Ý nghĩa     | Ví dụ       |
|---------|-------------|-------------|
| `+`     | Cộng        | `3 + 2 = 5` |
| `-`     | Trừ         | `5 - 2 = 3` |
| `*`     | Nhân        | `3 * 4 = 12`|
| `/`     | Chia thực   | `5 / 2 = 2.5`|
| `//`    | Chia nguyên | `5 // 2 = 2`|
| `%`     | Chia dư     | `5 % 2 = 1` |
| `**`    | Lũy thừa    | `2 ** 3 = 8`|

###  Toán tử so sánh:
- `==` : Bằng  
- `!=` : Khác  
- `>`  : Lớn hơn  
- `<`  : Nhỏ hơn  
- `>=` : Lớn hơn hoặc bằng  
- `<=` : Nhỏ hơn hoặc bằng  

###  Toán tử logic:
- `and` : Và (`True and False → False`)
- `or`  : Hoặc (`True or False → True`)
- `not` : Phủ định (`not True → False`)

---

##  3. MỆNH ĐỀ ĐIỀU KIỆN VÀ VÒNG LẶP

###  Câu lệnh điều kiện:
```python
x = 10
if x > 0:
    print("Số dương")
elif x == 0:
    print("Số 0")
else:
    print("Số âm")
```

###  Vòng lặp for:
```python
for i in range(5):
    print(i)  # In ra từ 0 đến 4
```

###  Vòng lặp while:
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

###  Lệnh break và continue:
- `break`    : Thoát khỏi vòng lặp  
- `continue` : Bỏ qua phần còn lại, chuyển sang vòng lặp kế tiếp

---

##  4. KIỂU DỮ LIỆU TRUE, FALSE (BOOL)

- Là kiểu logic chỉ có 2 giá trị:
  - `True`  → Đúng
  - `False` → Sai

###  Một số giá trị có giá trị bool là `False`:
- `0`, `0.0`
- `""` (chuỗi rỗng)
- `[]` (list rỗng), `{}` (dict/set rỗng)
- `None`

###  Những giá trị còn lại thường là `True`:
- `1`, `"abc"`, `[1, 2]`, `{"a": 1}`

**Ví dụ:**
```python
print(bool(0))         # False
print(bool("Python"))  # True
```




