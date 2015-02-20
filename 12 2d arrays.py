rows = 3
cols = 6
dd = [[0 for i in xrange(cols)] for j in xrange(rows)]
print dd

dd[2][2] = 4
print dd
print

#Old is gold method

dd2 = list()
for i in xrange(rows):
    tmp = list()
    for j in xrange(cols):
        tmp.append(0)
    dd2.append(tmp)

print dd2
print