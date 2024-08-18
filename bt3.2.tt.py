# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:08:53 2024

@author: Student
"""

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
if a+b > c or a+c > b or b+c > a:
    if a == b or b == c or a == c:
        print("Ta duoc tam giac abc là tam giac can")
    if a == b == c:
        print("Ta duoc tam giac abc là tam giac deu")
    if a*a + b*b == c*c:
        print("Ta duoc tam giac abc là tam giac vuong")
    else:
        print("Ta duoc tam giac abc là tam giac thuong")
else:
    print("Ta duoc abc khong la tam giac")