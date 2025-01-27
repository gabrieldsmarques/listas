a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

saud = """ 
Seja bem vindo a minha calculadora básica, escolha a operação que deseja fazer:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão          
"""
print(saud)
op = int(input())

if op == 1:
    print("Certo! O resultado é:", a+b)
elif op == 2:
    print("Certo! O resultado é:", a-b)
elif op == 3:
    print("Certo! O resultado é:", a*b)
elif op == 4:
    print("Certo! O resultado é:", a/b)
else:
    print("A operação escolhida não existe!")