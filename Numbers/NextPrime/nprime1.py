# -*- coding: utf-8 -*-

"""
Created on Mon Apr  2 07:00:29 2018

@author: liem.vo
"""

def is_prime(n):
    if n < 2: 
        return  False
    for i in range(n)[2:]:
        if n % i == 0:
            return False
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