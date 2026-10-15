import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input("Nhap so nguyen n = "))

n = abs(n)

print("Gia tri tuyet doi =", n)