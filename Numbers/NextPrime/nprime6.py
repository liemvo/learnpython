#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 07:59:12 2018

@author: liem.vo
"""

def lower_bound(ar, n, x):
    l = 0
    h = n
    while l < h:
        mid = int((l+h)/2)
        if x > ar[mid] or x == ar[mid]:
            l = mid + 1
        else:
            h = mid
            
    return l

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
indices = [1, 7, 11, 13, 17, 19, 23, 29]
def is_prime(n):
    N = len(small_primes)
    
    for i in range(N)[3:]:
        p = small_primes[i]
        q = int(n/p)
        if q < p:
            return True
        if n == q * p:
            return False
    i = 31
    M = len(indices)
    while True:
        for j in range(M)[1:]:
            q = int(n/i)
            if q < i: 
                return True
            if n == q * i:
                return False
            i += (indices[j] - indices[j-1])
            
        i += 2
        
        
def next_prime(n):
    L = 30
    N = len(small_primes)
    if n < small_primes[N-1]:
        return small_primes[lower_bound(small_primes, N, n)]
    
    M = len(indices)
    k0 = int(n/L)
    i= lower_bound(indices, M, n - k0 * L)
    n = L * k0 + indices[i]
    while not is_prime(n):
        i += 1
        if (i == M):
            k0 += 1
            i = 0
        n =L * k0 + indices[i]
        
    return n
        
    
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