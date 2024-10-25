decimal_num = int(input("Nhap so o dang thap phan: "))   # Nhập vào số từ bàn phím

octal_number = ""   # khởi tạo chuỗi lưu trữ số bát phân

while decimal_num > 0:
    octal_number = str(decimal_num % 8) + octal_number
    decimal_num = decimal_num // 8

print(f"So bit can de bieu dien: {len(octal_number) * 3}")   # Tính số bit bằng cách nhân số chữ số bát phân với 3

print(dir(decimal_num))   # Lấy danh sách các thuộc tính và phương thức của biến number