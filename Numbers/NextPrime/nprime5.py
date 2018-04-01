#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 07:35:53 2018

@author: liem.vo
"""

def is_prime(n):
    o = 4
    i = 5
    while True:
        q = int(n / i)
        if (q < i):
            return True
        if n == q * i:
            return False
        o ^= 6
        i += o
        

def next_prime(n):
    if n == 0 or n == 1 or n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4 or n == 5:
        return 5
    
    k = int(n/6)
    i = n - 6*k
    if i < 2:
        o = 1
    else: 
        o = 5

    x = 6 * k + o
    i = int((3 + o) / 2)
    
    while not is_prime(x):
        i ^= 6
        x += i
    return x
        
def main():
    
    '''while True:
        try:
            number = int(input('Please enter number: '))
        except:
            print('You don\'t enter a number')
        else:
            print('Primes number: ')
            print(next_prime(number))
            break
    '''
    print(next_prime(50000000))
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("---Time %s seconds ---" % (time.time() - start_time))