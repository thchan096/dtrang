# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:41:12 2024

@author: Student
"""

x = float(input("Quãng đường mà taxi đi được (km):"))
if x <=1:
    print("Phí đi taxi (vnđ): 20*x")
elif x > 1 and x <= 3:
    print("Phí đi taxi (vnđ): ", x*13)
elif x >= 4 and x <= 8:
    print("Phí đi taxi (vnđ): ", (3*13)+12*(x-3))
else:
    phí = 3*13+5*12+10*(x-8)
    if phí > 100:
       print("Phí đi taxi (vnđ): ", phí*0.92)
    else:
        print("Phí đi taxi (vnđ): ", 3*13+5*12+10*(x-8))