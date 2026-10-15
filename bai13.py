can_nang = float(input("Nhập vào cân nặng (KG): "))
chieu_cao_cm = float(input("Nhập vào chiều cao (CM): "))

chieu_cao_m = chieu_cao_cm / 100

bmi = can_nang / ( chieu_cao_cm * chieu_cao_m)

print("Chỉ số BMI của bạn là: ", bmi)