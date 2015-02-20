#IF ELIF ELSE
a = 90
b = 89
k = 'pappu'
p = complex()
if a < b:
    print str(a) + 'is greater than' + str(b)
elif a == b:
    pass
else:
    pass


if a == b:
    if b < d:
        if k == p:
            print 'something'








#WHILE LOOP
i = 0
while i < 5:
    i += 1
    print i







#FUNCTIONS
#all passing values between functions is BY REFERENCE
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print is_even(2)
print is_even(5)
print is_even(0)

print 100 * 'X'

def function(string, stringg):
    print string
    print stringg


a = function('Hello', 'World')
print a


print 100 * 'x'
