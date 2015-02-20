c = 10
d = 0

def method():
    global c,d #to use global variable use this line
    c+=1
    print c

method()

print c






def method1(c):
    c+=1
    print c

method1(999)

print c



def method2():
    print c,d #access ho jayenge lekin modify nahi ho sakte bina gloal wali line likhe



#global lists or dictionaries me ye panga nahi hai, vo directly use kari jaa sakte hai

#strings or tuples mutable hi nahi hai to ye poora concept unke liye pointless ho jata hai


