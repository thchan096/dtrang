# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:48:23 2024

@author: Student
"""

print("Giải phương trình bậc 2: ax + b = 0 (a khác 0)")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0 and b == 0:
    print("Phương trình vô nghiệm")
else:
    print("Nghiệm của phương trình là: ", -b/a)