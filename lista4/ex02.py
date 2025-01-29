def soma_lista_aninhada(lista):
    if type(lista) == list:
        return soma_lista_aninhada(sum(lista))
    else:
        return lista

print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))