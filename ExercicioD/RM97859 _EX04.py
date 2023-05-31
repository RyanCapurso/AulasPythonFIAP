# Recebe os minutos atuais
minutos_atuais = int(input("Digite os minutos atuais: "))

# Calcula o fatorial
fatorial = 1
for i in range(1, minutos_atuais + 1):
    fatorial *= i

# Exibe a senha de desbloqueio
senha = "LIBERDADE" + str(fatorial)
print("A senha para desbloqueio é:", senha)