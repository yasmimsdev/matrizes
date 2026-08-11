notas = [[7,8,6], [5,9,7], [8,6,10]]
# print(notas[1][1]) = mostra o número 9, pois acessa a linha 1 e coluna 1

#for i in range(len(notas)):
#    print(notas[i]) = notas [0], notas[1], notas[2]

for i in range (len(notas)):
    for j in range (len(notas)):
        print(notas[i][j])
# = Percorre e mostra todos os números presentes na matriz, um por um.