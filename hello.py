import numpy as np
import pandas as pd

#1st question
lst=[]
for i in range(2000, 3201):
    if (i%7 == 0) and (i%5!=0):
        lst.append(i)
print(lst)

#2nd question
f=1
x=input()
x=int(x)
while (type(x)!= int) or (x<0):
    print ("Type again your  positive integer")
    x=input()
    x=int(x)
if x > 1 :
    i = x
    while i!=1 :
        f = f * i
        i = i - 1
print("the factorial of " + str(x) + " is " + str(f))

#3rd question 
x=input()
Dic = {}
for i in range (x) :
    s = i+1 
    s2 = s * s
    Dic[s]=s2
print (Dic)

#4th questionp
ch=input()
n= -1
while ((n<0) or (n>len(ch)-1)) :
    n=input()
    n=int(n)
ch1=''
for i in ch :
    if i != n :
        ch1 = ch1 + ch[i]
print(ch1)

#5th question
arr=np.array([[0, 1], [2, 3] ,[4, 5]])
lst = arr.tolist()
print(lst)

#6th question
a1=[0,1,2]
a2=[2,1,0]
print(np.cov(a1,a2))

#7th question
C = 50
H = 30
I = []
D = []

x = input ()
x = int(x)
I.append(x)

for z in I :
    Q1 = (2 * C * z ) / H
    Q = Q1 * Q1
    D.append(round(Q))

print (D)