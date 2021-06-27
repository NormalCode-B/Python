# Tim cac so chia het cho 7 va khong phai la boi so cua 5
# j =[]
# for i in range(1999,3201):
#     if (i % 7 == 0) and (i % 5 != 0):
# #         j.append(str(i))
# # print(','.join(j))
#         print(i, end=" ")
# ----------------------------------
# Tinh giao thua
# a = int(input("Nhap a : "))
# total = 1
# for i in range(2, a+1):
#     total = total*i
# print(total)
# -------------------------------
# n = int(input("nhap so n : "))
# a = dict()
# for i in range(n+1) :
#     a[i]=i*i
# print(a)

# -----------------------tạo ra một danh sách và một tuple chứa mọi số.
# value  = input("Nhap day so :")
# l = value.split()
# t = tuple(l)
# print(l)
# print(t)

# -----------------------
# class upcase:
#     value = input("Nhap mot chuoi : ").upper()
#     def getString(self):
#         print("Lay chuoi in hoa :", self.value)
#     def printString(self):
#         print("Lay chuoi in thuong :", (self.value).lower())
#
# abc = upcase()
# abc.getString()
# abc.printString()

# class upcase:
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input("Nhap mot chuoi :")
#     def printString(self):
#         print("Lay chuoi in thuong :", self.s.upper())
# a =upcase()
# a.getString()
# a.printString()

# ---------------------- Tinh binh phuong
# class binhphuong:
#     def __init__(self):
#         self.s = ""
#     def get(self):
#         self.s = int(input("Nhap gia tri : "))
#     def print(self):
#         a = self.s ** self.s
#         print(a)
# b = binhphuong()
# b.get()
# b.print()

# x = int(input("Nhap so :"))
# def binhphuong(a):
#     return a ** 2
#
# print(binhphuong(x))

# --------------------------------------
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
# Code by Quantrimang.com
def square(num):
 '''Trả lại giá trị bình phương của số được nhập vào.
 Số nhập vào phải là số nguyên.
 '''
 return num ** 2

print (square.__doc__)