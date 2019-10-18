"""
Created on Thu Oct 17 21:06:25 2019
Project Euler Problem 125: Palindromic Sums

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. 
Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.

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

num = 10**8
print("SUM: ", solution(num))
