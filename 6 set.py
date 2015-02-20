# set create karne ka bas ek hi tareeqa hai: set initializer use karna
# this is like a collectin of keys and keys must be immutable. So we cannot use dictionaries or lists in sets
# unordered
# repeated elements ko automatically uda dega

a = set([10,10,1,9,'9k', (1,2,3,4)])

print a

b = set([10,1,'kutta'])

print b

c = a&b #intersection
d = a|b #union
e = a-b #set difference

print c,d,e


