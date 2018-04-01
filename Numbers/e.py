# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from math import e
def e_with_precision(n):
    return '{:.{}f}'.format(e, n)

def main():
    while True:
        try:
            number = int(input('Please enter number between 3 and 48: '))
        except:
            print('You don\'t enter a number')
        else:
            if number < 3 or number > 50:
                print('Number must be between 3 and 48')
            else:
                print(e_with_precision(number))
                
            break

if __name__ == '__main__':
    main()