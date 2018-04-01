# -*- coding: utf-8 -*-
'''
def prime(n):
    primes = []
    for i in range(n+1)[2:]:
        add = True
        for j in primes:
            if i % j == 0:
                add = False
                break;
        if add:
            primes.append(i)
    return primes
'''

def prime(n):
    for i in range(n+1)[2:]:
        if i == 2 or i==3:
            yield i
        else:
            add = True
            for j in prime(n-1):
                if i % j == 0:
                    add = False
                    break;
            if add:
                yield i

def main():
    while True:
        try:
            number = int(input('Please enter number: '))
        except:
            print('You don\'t enter a number')
        else:
            print('Primes number: ')
            print(list(prime(number)))
                
            break

if __name__ == '__main__':
    main()