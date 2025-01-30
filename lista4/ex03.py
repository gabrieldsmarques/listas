def contar_caracteres(s, c):
    if s == "": ##se a string for vazia, n tem letra pra repetir, logo retorna 0
        return 0
    else:
        if s[0] == c: ## se a primeira letra for igual a letra desejada, retorna 1 + o chamado da função, assim gerando um loop até que a stirng esteja vazia, devolvendo o número de vezes que a letra se repete + 1
            return 1 + contar_caracteres(s[1:], c)
        else:
            return contar_caracteres(s[1:], c) ##se a primeira não bater, começa pela segunda letra e o loop segue até o fim da string, completando a função da mesma forma.
print(contar_caracteres("banana", "a"))