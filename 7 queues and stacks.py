#stacks and queuues

#they are just lists

#insertion is in stack order so there you go

#for deletion

#stacks

#use pop

#for queues

#use pop(0)


queue = []

for i in xrange(10):
    queue.append(i)
    print queue

for i in xrange(10):
    queue.pop(0)
    print queue


stack = []

for i in xrange(10):
    stack.append(i)
    print stack


for i in xrange(100):
    if len(stack)<=0:
        break
    else:
        stack.pop()
    print stack


#boundry condition checking

