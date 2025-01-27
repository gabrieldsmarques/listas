numbers = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
]
def soma(matriz):
    n = len(matriz)
    somap = 0
    somas = 0
    
    for i in range(n):
        somap += matriz[i][i]
        somas += matriz[i][n - i - 1]
        
    return somap, somas

somap, somas = soma(numbers)

print(f"A soma da diagonal principal é: {somap}")
print(f"A soma da diagonal secundária é: {somas}")