name = input("Nhập họ và tên: ")

name = " ".join(name.strip().split())
name = name.title()

print("name: ", name)