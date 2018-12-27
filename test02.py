# -*- coding: utf-8 -*-
import re

p1= r'\w+(?:\.jpg|\.png)'
t1='img1.jpg,img2.png,img3.jpg,img4.jpg'
m1=re.finditer(p1,t1)
print(m1.next().string)