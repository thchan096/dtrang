# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:51:16 2024

@author: Student
"""

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
if a+b>c and a+c>b and b+c>a:
    print("Ta có a, b, c là 3 cạnh của tam giác")
else:
    print("Ta có a, b, c không là 3 cạnh của tam giác")