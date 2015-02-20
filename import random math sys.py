import math
import random
import sys

from math import * #with this you can write sqrt() instead of math.sqrt()

print math.sin(math.pi)
print 100 * 'x'
print random.randrange(10) #Gives a random integer in [0, 10)
print random.randrange(2, 10)

print random.random() #[0, 1)

l = [1, 2, 3, 4, 5]
random.shuffle(l)
print l

print random.randint(1, 10) #[1, 10]

print 100 * 'x'

for i in xrange(10):
    sys.stdout.write(str(i))  #Takes strings only

for i in xrange(10):
    sys.stdout.write(str(i) + '\n')  #Takes strings only