y = float(input("Hãy nhập tiền gửi: "))
x = float(input("Hãy nhập lãi suất hàng năm: "))

print("Lãi suất hàng năm là: ", x, "%")

tien_goc = y
for i in range(1, 4):
    thang_dau = (i - 1) * 6 + 1
    thang_cuoi = i * 6
    print(f"\nChu kỳ tiết kiệm thứ {i:02}: "
          f"{thang_dau:02} - {thang_cuoi:02}")
    
    print("Tiền gốc: ", tien_goc)

    tien_lai = tien_goc * x * 6 / 12
    print("Tiền gốc + lãi 6 tháng là: ", tien_goc)

# Tính lãi không chu kỳ hạn từ tháng 19 đến tháng 20
print("\nChu kỳ tiết kiệm thứ 04: 19 - 20")
print("Lãi suất không kỳ hạn: 0.012 trên năm")
print("Tiền gốc: ", tien_goc)

tien_lai = tien_goc * 0.012 * 2 / 12 
print("Tiền lãi không kỳ hạn 2 tháng là: ", tien_lai)

tien_nhan = tien_goc + tien_lai
print("Tổng tiền nhận sau 20 tháng là: ", tien_nhan)

tien_lai = tien_goc * 0.012 * 2 / 12
print("Tiền lãi 2 tháng cuối: ", int(tien_lai))

tien_nhan = tien_goc + tien_lai
print("Tiền gốc + lãi 2 tiếp theo là: ", tien_nhan)