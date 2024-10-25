def main():
    # In ra chuỗi
    greeting = "Chao mung den CLB Tin Hoc HIT"
    print(greeting)
    
    # In ra câu
    club_info = "CLB Tin Hoc HIT truc thuoc Khoa CNTT - 10 diem"
    print(club_info)

    # Chuỗi để thực hiện các phép toán
    example_string = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"

    # In ra tất cả các chữ cái in hoa trong chuỗi
    uppercase_letters = ''.join([char for char in example_string if char.isupper()])
    print("Các chữ cái in hoa:", uppercase_letters)

    # In ra các chữ cái thường của chuỗi
    lowercase_letters = ''.join([char for char in example_string if char.islower()])
    print("Các chữ cái thường:", lowercase_letters)

    # Kiểm tra xem từ 'CNTT' có thuộc chuỗi không
    if 'CNTT' in example_string:
        print("Yes")
    else:
        print("No")

    # Thay thế các chữ hoa thành thường và ngược lại
    swapped_case = example_string.swapcase()
    print("Chuỗi sau khi thay thế chữ hoa thành thường và ngược lại:", swapped_case)

if __name__ == "__main__":
    main()