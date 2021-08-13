ch=input()
n= -1
while ((n<0) or (n>len(ch)-1)) :
    n=input()
    n=int(n)
ch1=''
for i in range(len(ch)) :
    if i != n :
        ch1 = ch1 + ch[i]
print(ch1)