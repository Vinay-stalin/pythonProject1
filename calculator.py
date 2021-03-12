
i='Yes'

while(i=='Yes'):
    a = input("Enter first integer")
    b = input("Second value")
    c = input('+,-,/,*')
    if (c == '+'):
        print(int(a) + int(b))
    if (c == '-'):
        print(int(a) - int(b))
    if (c == '*'):
        print(int(a) * int(b))
    if (c == '/'):
        print(int(a) / int(b))
    n=input("aGAIN? if no please enter n")
    if(n=='n'):
        exit()
print('Thank you')


