'''
Euler Project :: Problem 4
Started: 6/29/2009 (In DarkBASIC!)
Solved: 9/1/2021 (In Python!)

Description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Correct Answer:
906,609

After Notes:
I seriously can't figure out how to do this one, I might look at it later.

11 Years Later:
Hmmm. First, can we not deduce the largest palindrome of two 3-digit numbers? It will involve 6 digits:

999999 strikes me as a palindrome, but of course our upper-bound is 999*999=998001. 
From here, it would be trial-and-error and that isn't really satisfying...

How about some math?

'palindrome' = a(10^3) + b(10^2) + b(10^1) + a(10^0)
             = 1,001(a) + 110(b)


'palindrome' = a(10^5) + b(10^4) + c(10^3) + c(10^2) + b(10^1) + a(10^0)
             = 100,001(a) + 10,010(b) + 1,100(c)

where 1 <= a <= 9,
      0 <= b <= 9,
      0 <= c <= 9

There is probably something to this... but Python is so easy to implement string-based searches
I think I will start with that. And... it works! I get an answer in about 1.05 seconds.

'''

# My quick way of timing, ignoring only the library imports
import time
startTime = time.time()

def fnIsPalindrome(num):
    '''Determines whether a number is a palindrome (same forwards and backwards) or not.
    @author: Tony Cardillo

    Arguments:
    num: integer

    Returns:
    bool: True if num is a palindrome; False if num is NOT a palindrome
    
    '''
    numString = str(num)
    lenNumString = len(numString)

    for digit in range(lenNumString//2):
        if numString[digit] == numString[lenNumString-digit-1]:
            pass
        else:
            return False

    return True

# Multipler 1
answer = 0

for a in range(100,1000):
    # Multiplier 2
    for b in range(100,1000):
        answerCandidate = a * b
        #print(answerCandidate)
        # If the answer is a palindrome...
        if fnIsPalindrome(answerCandidate):
            # If so, is this the largest palindrome so far?
            if answerCandidate > answer:
                # Yes, store it! (if not, we ignore it)
                answer = answerCandidate

# Print time in seconds
endTime = time.time()
print("{} seconds".format(endTime - startTime))

# Print THE ANSWER
print(answer)        
quit()