'''
Euler Project :: Problem 20

Language: Python
Started: 9/2/2021
Solved: 9/3/2021 at midnight!  
Speed (median of 3): 0.0 ms (too fast to profile)


Description:

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Correct Answer:
648

Notes:
I used a naive factorial function, but it is so fast already at 100! that
there is no need to optimize! Yet...
'''

import time
startTime = time.time()

def fnNaiveFactorial(n: int):
    if n == 0:
        return 1

    product = 1
    while n > 1:
        product *= n
        n -= 1
    
    return product

def fnSumOfDigits(numberToSum: str):
    lenNumberToSum = len(numberToSum)

    sum = 0
    for digit in range(lenNumberToSum):
        sum += int(numberToSum[digit])
    
    return sum

number = fnNaiveFactorial(100)

theAnswer = fnSumOfDigits(str(number))
endTime = time.time()

print("{} milliseconds".format(startTime-endTime))
print(theAnswer)