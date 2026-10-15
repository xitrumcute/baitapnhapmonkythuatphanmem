ten_khach_hang = input("Nhập tên khác hàng: ")
so_tien = float(input("Nhập số tiền gửi (đồng): "))
lai_suat = float(input("Nhập lãi suất (%/tháng): "))

tien_lai = so_tien * (lai_suat / 100)

print("Tên khách hàng: ", ten_khach_hang)
print("Số tiền gửi: ", so_tien)
print("Lãi suất: ", lai_suat, "%/tháng")
print("Tiền lãi: ", tien_lai)