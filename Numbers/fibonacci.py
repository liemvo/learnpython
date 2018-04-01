# -*- coding: utf-8 -*-

def fibonacci_generator(n):
    a,b = 1, 1
    for i in range(n):
        yield a
        a,b = b,a+b

def main():
    while True:
        try:
            number = int(input('Please enter number: '))
        except:
            print('You don\'t enter a number')
        else:
            
            print('Fibonacci list: ')
            print(list(fibonacci_generator(number)))
                
            break
if __name__ == '__main__':
    main()
