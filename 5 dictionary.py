d = {1 : 'One', 8 : 'Eight', None: 78, True : [5, 6, 7], (7, 8) : {1 : 1}}
#keys must be immutable. hence dictionary and lists can't be used as keys but strings and tuples can be
print d


for key in d:
    print d[key]

d[90] = 'Ninety'# if key 90 is already present then its value will be changed to 'Ninety'  otherwise a new key value pair will be added to the dictionary

#dictionaries are unordered . the iterator iterates keys in random order

print d

#empty dictionary
dempty = {}

#or

dempty = dict()

del d[90]
print d

