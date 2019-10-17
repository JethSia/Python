# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:09:48 2019

@author: Jeth Sia
"""
### FUNCTIONS ###
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
        for j in range(i-1):
            B = (j*(j+1)*(2*j+1))//6
            C = A - B
            if is_palindromic(C) and C<x:
                L.add(C)
    return sum(L)
   

### MAIN PROGRAM ###

num = 10**8
print(solution(num))
