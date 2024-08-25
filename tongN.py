# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:56:12 2024

@author: Quynh Trang
"""
N = int(input("Nhập số nguyên có 2 chữ số: "))
if 10 <= N <= 99:
    chuc = N // 10
    donvi = N % 10
else:
    print(" Không đúng nhập lại: ")
print(" Tổng các chữ số của N Là: ", chuc + donvi )
    
    
