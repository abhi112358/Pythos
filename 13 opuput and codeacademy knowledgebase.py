

total=1.2284
print("%.2f" % total)


ministry = "The Ministry of Silly Walks"
print len(ministry)
print ministry.upper()

from datetime import datetime
now = datetime.now()
print now
print now.year
print now.month
print now.day
print '%s:%s:%s' % (now.hour, now.minute, now.second)


def biggest_number(*args):
    print max(args)
    return max(args)
biggest_number(-10, -5, 5, 10)



print type("hello")
print type(12)
print type(-12)
print type((1,2,3))
print type([1,2,3])
print type(set([1,2,3]))
print type( {1:"@",2:"hello"} )
if type(s)==int or type(s)==float:
        return abs(s)







