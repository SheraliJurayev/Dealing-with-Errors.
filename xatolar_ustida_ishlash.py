# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 00:44:51 2023

@author: Sh_Jurayeff
"""

# age =input("Yoshingizni  kiriitng:")
# try:
#     age = int(age)
#     print("Siz {2023 - age} - yilda tug'ilgansiz.")
# except: 
#     print("Iltimos butun son kiriting.")    


import json
files = ["data.json" , "numbers.json" , "patient.json" , "notfile"] 
for filename in files:
    try:
        with open(filename) as file:
            numbers = json.load(file)
    except FileNotFoundError:
        print(f"{filename} degan file mavjud emas")
    else:
       pass
                