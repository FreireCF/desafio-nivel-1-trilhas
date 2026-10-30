historico = []

print("=== PDV - Ponto de Venda ===")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    valor = float(input("Valor da compra: R$ "))

    if valor == 0:
        break

    if valor < 0:
        print("O valor não pode ser negativo. Tente novamente.\n")
        continue

    idade = int(input("Idade do cliente: "))

    if idade < 0:
        print("A idade não pode ser negativa. Tente novamente.\n")
        continue

    valor_final = valor

    if idade >= 65:
        valor_final = valor_final * 0.80

    if valor_final > 100:
        valor_final = valor_final * 0.90

    valor_final = round(valor_final, 2)

    print(f"Valor final: R$ {valor_final:.2f}\n")

    compra = {"valor": valor, "idade": idade, "valor_final": valor_final}
    historico.append(compra)

total_bruto = 0
total_final = 0

for compra in historico:
    total_bruto = total_bruto + compra["valor"]
    total_final = total_final + compra["valor_final"]

total_descontos = total_bruto - total_final

print("\n=== Resumo do dia ===")
print(f"Compras registradas: {len(historico)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")

arquivo = open("resumo.txt", "w", encoding="utf-8")
arquivo.write("=== Histórico de compras ===\n")
for compra in historico:
    arquivo.write(f"Valor: R$ {compra['valor']:.2f} | Idade: {compra['idade']} | Final: R$ {compra['valor_final']:.2f}\n")
arquivo.write("\n=== Resumo do dia ===\n")
arquivo.write(f"Compras registradas: {len(historico)}\n")
arquivo.write(f"Total bruto: R$ {total_bruto:.2f}\n")
arquivo.write(f"Total de descontos: R$ {total_descontos:.2f}\n")
arquivo.write(f"Total final: R$ {total_final:.2f}\n")
arquivo.close()

print("\nResumo salvo em resumo.txt")
