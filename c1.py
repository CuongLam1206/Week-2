def main():
    # Nhập hai số a và b
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    
    # a cộng b
    print(f"a cộng b: {a + b}")
    
    # a trừ b
    print(f"a trừ b: {a - b}")
    
    # a nhân b
    print(f"a nhân b: {a * b}")
    
    # a chia lấy nguyên b
    if b != 0:
        print(f"a chia lấy nguyên b: {a // b}")
    else:
        print("Không thể chia cho 0.")
    
    # a mũ b
    print(f"a mũ b: {a ** b}")
    
    # a chia dư b
    if b != 0:
        print(f"a chia dư b: {a % b}")
    else:
        print("Không thể chia cho 0.")
    
    # So sánh a và b
    if a > b:
        print("a lớn hơn b")
    elif a < b:
        print("a nhỏ hơn b")
    else:
        print("a bằng b")
    
    # a AND b
    print(f"a AND b: {a & b}")
    
    # a OR b
    print(f"a OR b: {a | b}")
    
    # a XOR b
    print(f"a XOR b: {a ^ b}")
    
    # NOT a == b
    print(f"NOT a == b: {not (a == b)}")
    
    # a dịch phải 5 bit
    print(f"a dịch phải 5 bit: {a >> 5}")
    
    # a dịch trái 6 bit
    print(f"a dịch trái 6 bit: {a << 6}")
    
    # in hệ cơ số 2 đảo ngược của a
    binary_a = bin(a)[2:]  # chuyển a sang nhị phân
    reversed_binary_a = binary_a[::-1]  # đảo ngược chuỗi
    print(f"Hệ cơ số 2 đảo ngược của a: {reversed_binary_a}")

if __name__ == "__main__":
    main()