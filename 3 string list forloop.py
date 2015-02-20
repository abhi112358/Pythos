#A string in Python is a character array with power of Java
name = 'Abhimanyu'

print name
print name[4]
print name[2:5]
print len(name)
print name + ' Sood'
print 3 * name

#Strings are immutable to mutate strings use the above techniques
#String to char array
name = 'abhimanyu'
chars = list(name)
print chars
#now manipulate the list called chars
#then join this list back to string using the next command
verma = '@'.join(chars)
print verma


str = 'This is a this and this is not this'
sea = 'this'
str=str.replace('this','****')
print str












#A list is a dynamic array
#you insert into a list by append but access and modify like a direct array

a = [1, 2, 3, 4, 5]
print a
print a[3]
print a[3:5]
print len(a)
print 5 * a

a.append(6)
print a
v = a.pop()
print a
print v

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")#finds the index of duck
animals.insert(duck_index,"cobra")#insertion at a particular index
animals.sort()

animals.remove("cobra");
print animals


webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for i in webster:
    print webster[i]


n.pop(0)
n.remove(0)
del(n[0])



















#For loop

for char in name:
    print char

for i in a:
    print i + 3
    print i + 3,


for i in range(10):
    print i

print 100 * 'x'
for i in range(4, 10):
    print i,
print
for i in range(2, 10, 3):
    print i,

print range(1, 100) #Range generates a list, hence inefficient
print
for i in xrange(2, 15):
    print i,

print xrange(7) #It returns/generates an iterator, hence efficient

