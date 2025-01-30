def indice_maior_elemento(lista):
    
    if len(lista) <= 1:
        
        return 0 ## se a lista so tem 1 elemento, o indice zero já é o maior
    
    else:
        
        indice_maior_restante = indice_maior_elemento(lista[1:]) ## variavel pra guardar o indice do maior elemento atual.
        
        if lista[0] > lista[1 + indice_maior_restante]: #comparacao do primeiro elemento com o maior atual, o +1 serve pra ajustar o indice, porque o indice da variavel e relativo ao segundo elemento da lista, assim se desajustando do comum, precisando do +1 pra "endireitar"
            
            return 0 # se o maior elemento for o indice zero, continua retornando zero
        
        else:
            
            return indice_maior_restante + 1 #se nao, retorna a variavel com maior indice ajustada pra encaixar com a lista original, pra isso serve o +1
    
    
print(indice_maior_elemento([1, 5, 3, 9, 2])) #retorna 3 porque e o indice, e nao o maior numero