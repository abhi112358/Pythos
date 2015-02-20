#A list of first 10 whole numbers
x = list()
for i in xrange(10):
    x.append(i)

print x
print

y = range(10)
print y
print

#List Comprehension

z = [i for i in xrange(10)]
print


even = [2 * i for i in xrange(1, 100)]
print even

#Static Array, if append isn't used
initial = [0 for i in xrange(10)]
print initial


length = 4
width = 3
height = 3

points = [(x, y, z) for x in xrange(5) for y in xrange(4) for z in xrange(4)]
print points
print


def is_prime(number):
    for i in xrange(2, number):
        if number % i == 0:
            return False
    return True

primes = [i for i in xrange(100) if is_prime(i)]
print primes
print

t = (i for i in xrange(100) if is_prime(i))
print t

