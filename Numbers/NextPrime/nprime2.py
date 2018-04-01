#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 07:11:29 2018

@author: liem.vo
"""

def is_prime(n):
    if n < 2: 
        return  False
    
    i = 2
    while True:
        x = int(n / i)
        if x < i:
            return True
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime(n):
    x = n
    while not is_prime(x):
        x += 1
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
