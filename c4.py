def main():
    # Nhập thông tin từ người dùng
    ho_ten = input("Nhập họ và tên: ")
    tuoi = input("Nhập tuổi: ")
    gioi_tinh = input("Nhập giới tính (Nam/Nữ): ")
    tinh_trang_hon_nhan = input("Nhập tình trạng hôn nhân (Độc thân/Kết hôn): ")
    
    # In thông tin ra màn hình
    print("\nThông tin nhân khẩu học của bạn HIT 15:")
    print(f"Họ và tên: {ho_ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Giới tính: {gioi_tinh}")
    print(f"Tình trạng hôn nhân: {tinh_trang_hon_nhan}")

if __name__ == "__main__":
    main()