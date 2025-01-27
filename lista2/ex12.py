a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))


def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



def primes_list(a, b):
    primes = []
    for num in range(a, b+1):
        if prime(num):
            primes.append(num)
    return primes
    
primes = primes_list(a,b)

print(f"A lista de primos no intervalo escolhido é: {primes}")