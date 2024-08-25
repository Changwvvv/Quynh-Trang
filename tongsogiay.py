# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:18:30 2024

@author: Quynh Trang
"""
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
Tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây: ", Tong_giay)