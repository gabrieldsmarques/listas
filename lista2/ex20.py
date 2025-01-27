n = int(input('Decida até onde a sequência vai: '))
n1, n2 = 0, 1
n3 = 0
aux = 0

while aux <= n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    aux +=1
    print(n3)
        