#Generator Functions


def primes(limit):

    def is_prime(number):
        for i in xrange(2, number):
            if number % i == 0:
                return False
        return True

    p = list()
    for i in xrange(limit):
        if is_prime(i):
            p.append(i)
    return p

print primes(80)
print

def xprimes(limit):

    def is_prime(number):
        for i in xrange(2, number):
            if number % i == 0:
                return False
        return True

    for i in xrange(limit):
        if is_prime(i):
            yield i

print xprimes(80)
print
