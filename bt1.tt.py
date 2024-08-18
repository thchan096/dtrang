# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:22:10 2024

@author: Student
"""

distance = float(input("Nhập điểm trung bình (GPA):"))
if distance >= 3.5 and distance < 5.0:
    print("Học lực Yếu")
elif distance >= 5.0 and distance < 7.0:
    print("Học lực Trung bình")
elif distance >= 7.0 and distance < 8.0:
    print("Học lực Khá")
elif distance >= 8.0 and distance < 9.0:
    print("Học lực Giỏi")
elif distance >= 9.0 and distance <= 10.0:
    print("Học lực Xuất sắc")
else:
    print("Học lực Kém")
    