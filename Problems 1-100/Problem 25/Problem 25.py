'''
Euler Project :: Problem 25

Language: Python
Started: 9/4/2021
Solved: 
Speed (median of 3): 2.99 milliseconds 


Description:

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Correct Answer:
4782


Notes:
Let's start with brute force? 
>Okay, that doesn't. My computer got too hot it crashed. There MUST be an optimization here.

Replacing the str(int(Answer)) method above with a ceil(log10(Answer)) approach was faster, but still
ridiculously slow with no answer, unless maybe I waited DAYS.

There must be a function for equating digits of Fn without caring about the values themselves.
I studied this more on wikipedia, and this is basically a geometric series around the golden ratio φ
Thus, in general, F_n = floor( n*log_10(phi) + 1) 

'''
import time

startTime = time.time()
import math

# Let's give this some memory
def fncDigitsAtIndex(index: int) -> int:
    return math.ceil(index * math.log10(1.61803))

assert fncDigitsAtIndex(1) == 1, "fncDigitsAtIndex doesn't work"
assert fncDigitsAtIndex(7) == 2, "fncDigitsAtIndex doesn't work"
assert fncDigitsAtIndex(12) == 3, "fncDigitsAtIndex doesn't work"
assert fncDigitsAtIndex(17) == 4, "fncDigitsAtIndex doesn't work"

theAnswer = 13
# Get the answer that has 999 digits.
while fncDigitsAtIndex(theAnswer) < 1000:
    theAnswer += 1
    
theAnswer += 1 #We found the last one with 999 digits above, so add one

endTime = time.time()
print("{} milliseconds".format(1000*(endTime-startTime)))
print(theAnswer)

# Gracefully quit
quit()
