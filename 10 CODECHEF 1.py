#Program to add two numbers and print the string jyon-ka-tyon and character ki ASCII value
#(4 inputs per test case)

def main():
    line = raw_input()
    tests = int(line)       #Anything to integer
    for i in xrange(tests):
        line = raw_input()
        four = line.split(" ")
        num1 = int(four[0])
        num2 = int(four[1])
        string = four[2]
        char = four[3]
        print num1+num2
        print string
        print ord(char)

main()

def splitstrip():
    string = "paapu!can't!dance!saala"
    words = string.split("!")
    print words

    words = string.split("a")
    print words


    s = "Pappu can't dance saala "
    words = s.split(" ")
    print words

    s = "Pappu can't dance saala ".strip()
    words = s.split(" ")
    print words

def joiner():
    j = ['Pappu', "can't", 'dance', 'saala']
    print "$".join(j)