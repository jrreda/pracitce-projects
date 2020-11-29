# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:28:02 2020

@author: Mahmoud
"""

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
numbers = '0123456789'
symbols = '[]{}()*-+_*&^%$#@!;:/\~.,<>'
all = lower + upper + numbers + symbols
length = int(input('Enter the length of your password: '))

password = "".join(random.sample(all, length))
print('Your password is:', password)