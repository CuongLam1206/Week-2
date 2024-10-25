def main():
    # Nhập vào chuỗi ký tự
    input_string = input("Nhập vào một chuỗi ký tự: ")
    
    # Kiểm tra có chữ "hit" hoặc "HIT" trong chuỗi
    contains_hit = "hit" in input_string or "HIT" in input_string
    print(contains_hit)  # In ra True nếu có, ngược lại False

    # Kiểm tra không có chữ số "15" trong chuỗi
    contains_15 = "15" in input_string
    print(not contains_15)  # In ra True nếu không có, ngược lại False

if __name__ == "__main__":
    main()