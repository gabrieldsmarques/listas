from functools import reduce

def calcular_medias_ponderadas(alunos):
    medias = {}
    
    for aluno, notas_pesos in alunos.items():
        notas = notas_pesos[:-1] #todas exceto a última, que é o peso
        peso = notas_pesos[-1] #só a última, que é o peso
        
        soma_ponderada = reduce(lambda x, y: x + (y * peso), notas, 0)
        
        soma_pesos = reduce(lambda x, _: x + peso, notas, 0)
        
        medias[aluno] = soma_ponderada / soma_pesos if soma_pesos !=0 else 0
        
    return medias


dict = {
 "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
 "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}

print(calcular_medias_ponderadas(dict))