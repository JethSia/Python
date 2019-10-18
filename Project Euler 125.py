# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:06:25 2019

@author: Jeth Sia
"""
def is_palindromic(x):
    return str(x) == str(x)[::-1]

def solution(x):
    L = set()
    sqrt_x = int(x**0.5)
    if sqrt_x < x**0.5:
        y = sqrt_x + 1
    else:
        y = sqrt_x
    
    
    for i in range(1, y):
        A = (i*(i+1)*(2*i+1))//6
        j = i-2
        while j >= 0:
            B = A - (j*(j+1)*(2*j+1))//6
            if B>x:
                break
            elif is_palindromic(B):
                L.add(B)
            j -= 1
    return sum(L)
   

### MAIN PROGRAM ###

num = 10**7
print("SUM: ", solution(num))
