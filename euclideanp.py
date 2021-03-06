# Copyright (C) 2014 kcotugno
# Distributed under the MIT software license, see the accompanying
# LICENSE file or http://www.opensource.org/licenses/MIT
#
# Author: kcotugno
# Date 5/30/14

import math


# This function check if a number is prime first by testing for the #2, then if 
# it less than 2 or divisible by 2. If non of these pre-checks return, it runs 
# through a loop which goes from 3 to the sqrt of the number only testing it 
# against odd numbers.
def isprime(num):
    if num == 2:
        return True
        
    if num < 2 or num % 2 == 0:
        return False
        
    for i in range(3, int(math.sqrt(num)) + 1, 2):
         if num % i == 0:
            return False
        
    return True


# The algorithm calculates the numbers by continually finding numbers in double 
# proportion from 1 until the sum of them is a prime number. Then, it takes the 
# product of the prime and last number in the proportion. Whence perfect numbers
# are found.
def perfection(calc):
    proportionals = [1]
    perfect = []
    
    p = 0
    while p < calc:
        
        psum = 0
        while isprime(psum) == False:
            proportionals.append((proportionals[len(proportionals) - 1]) \
                                                                   * 2)
            psum = 0
            for i in proportionals:
                psum = psum + i
                #print(psum)

        p += 1
        perfect.append(psum * proportionals[len(proportionals) - 1])
        
    return perfect
        
        
def main():
    print("Euclidean Perfection")
    print("Copyright (C) 2014 kcotugno")
    print("Distributed under the MIT software license, see the accompanying")
    print("LICENSE file or http://www.opensource.org/licenses/MIT\n")

    gotinput = False

    while gotinput == False:
        i = input("Please enter the desired number of perfection "
                                                "to calculate: ")

        try:
            int(i)

        except:
            print("Please only enter positive integers..."
                  "and not too large :)\n")

        else:
            i = int(i)

            if i <= 0:
                print("Please only enter positive integers..."
                      "and not too large :)\n")

            else:
                gotinput = True

    perfect = perfection(i)
    
    index = 0
    for p in perfect:
        index += 1
        print(format("{0}. {1}".format(index, p)))


if __name__ == "__main__":
    main()


