# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:00:18 2024

@author: Quynh Trang 
"""
chuoi="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
mot= chuoi.split(" , ")
hai= chuoi.replace("P. ","").replace("Q. ","").split(" , ")
print(mot)
print(hai)
