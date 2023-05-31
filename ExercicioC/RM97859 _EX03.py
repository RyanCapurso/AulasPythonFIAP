soma_impar = 0
soma_par = 0

for i in range(1, 51):
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    if i % 2 != 0:
        soma_impar += nota
    else:
        soma_par += nota

media_impar = soma_impar / 25
media_par = soma_par / 25

print("A média da turma dos alunos ímpares é:", media_impar)
print("A média da turma dos alunos pares é:", media_par)

if media_impar > media_par:
    print("A turma dos alunos ímpares teve a maior nota.")
elif media_impar < media_par:
    print("A turma dos alunos pares teve a maior nota.")
else:
    print("As turmas dos alunos ímpares e pares tiveram a mesma nota.")