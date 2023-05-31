# Pede para o usuário informar a quantidade de votos para cada dia da semana
votos_segunda = int(input("Digite a quantidade de votos para segunda-feira: "))
votos_terca = int(input("Digite a quantidade de votos para terça-feira: "))
votos_quarta = int(input("Digite a quantidade de votos para quarta-feira: "))
votos_quinta = int(input("Digite a quantidade de votos para quinta-feira: "))
votos_sexta = int(input("Digite a quantidade de votos para sexta-feira: "))

# Verifica qual dia da semana teve mais votos
mais_votado = "segunda-feira"
if votos_terca > votos_segunda:
    mais_votado = "terça-feira"
if votos_quarta > votos_terca:
    mais_votado = "quarta-feira"
if votos_quinta > votos_quarta:
    mais_votado = "quinta-feira"
if votos_sexta > votos_quinta:
    mais_votado = "sexta-feira"

# Exibe o resultado
print("O dia mais votado foi:", mais_votado)