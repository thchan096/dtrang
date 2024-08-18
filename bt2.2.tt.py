# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:05:45 2024

@author: Student
"""

import math
 
print("ax2 + bx + c = 0")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
          if c == 0:
              print("Phương trình vô số nghiệm")
          else:
              print("Phương trình vô nghiệm")
    else:
        if c == 0:
            print("Phương trình 1 nghiệm x = 0")
        else:
            print("Phương trình 1 nghiệm x = ", -c/b)
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)))
    else:
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 = ", (-(b) + math.sqrt(delta))/(2*a))
        print("x2 = ", (-(b) - math.sqrt(delta))/(2*a))

