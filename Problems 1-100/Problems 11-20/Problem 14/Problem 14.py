'''
Euler Project :: Problem 14

Language: Python
Started: 9/2/2021
Solved: 9/2/2021 (64.4 seconds... not Euler enough!)  
Speed (median of 3): 4.73 seconds


Description:

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Correct Answer:
837799

Notes:
A couple quick thoughts: it appears the doom of the sequence is when it hits a power of 2. Upon hitting a power of 2, the sequence length is log_2 (n) + 1
There are "doomed" numbers along the way, like 5. 5 will become 16. In fact, this determinism can be stored...

Every number's length can be stored in a dictionary - the above would be {13: 10}. If your sequence contains a 13, you can expect 10 extra terms (including the 13).
And it works! But it is 64 seconds... surely there is an optimization? Oh wait, my dictionary code wasn't working! Once that worked... less than 5 seconds!


'''
import time
startTime = time.time()

# I'm willing to hardcode this one
dicKnownSequences = {1:1, 13: 10}
mostTerms = 1
theAnswer = 1

for number in range(2,1000000):
    coTerms = 0
    nextNumber = number

    while nextNumber > 1:
        if nextNumber in dicKnownSequences:
            coTerms += dicKnownSequences[nextNumber]
            break
        else:
            coTerms += 1

        if nextNumber % 2 == 0:
            nextNumber /= 2
        else:
            nextNumber *= 3
            nextNumber += 1

    dicKnownSequences[number] = coTerms

    if coTerms > mostTerms:
        theAnswer = number
        mostTerms = coTerms

endTime = time.time()
print("{} seconds".format(endTime - startTime))
print("{} starting number has {} terms".format(theAnswer, mostTerms))

quit()

