import numpy as np
C = 50
H = 30
I = []
D = []

print('When finished write "DONE"')
x = input ()

while (x!="DONE") :
    x = int(x)
    I.append(x)
    x = input()

for z in I :
    Q1 = (2 * C * z ) / H
    Q = np.sqrt(Q1)
    D.append(round(Q))

print(D)