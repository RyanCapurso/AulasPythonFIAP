tipo = input("Digite o tipo de assinatura (Basic/Silver/Gold/Platinum): ")
faturamento = input("Digite o faturamento anual: ")
faturamento = float(faturamento.replace(".", ""))

porcentagem = 0
if tipo == "Basic":
    porcentagem = 30
elif tipo == "Silver":
    porcentagem = 20
elif tipo == "Gold":
    porcentagem = 10
elif tipo == "Platinum":
    porcentagem = 5
else:
    print("Tipo de assinatura inválido. Digite Basic, Silver, Gold ou Platinum")
    exit()

bonus = faturamento * porcentagem / 100
print("O valor do bônus para a assinatura", tipo, "é:", bonus)
