f=1
x=input()
x=int(x)
while x<0:
    print ("Type again your3 positive integer")
    x=input()
    x=int(x)
if x > 1 :
    i = x
    while i!=1 :
        f = f * i
        i = i - 1
print("the factorial of " + str(x) + " is " + str(f))