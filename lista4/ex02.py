def soma_lista_aninhada(lista):
    soma = 0
    if lista == 0:
        return lista
    else:
        for i in lista:
            if isinstance(i, (int, float)):
                soma += i
            else:
                soma += soma_lista_aninhada(i)
        return soma
                

print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))