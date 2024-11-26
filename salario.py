salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

if salario_atual <= 280.00:
    porcentagem = 20
elif salario_atual <= 700.00:
    porcentagem = 15
elif salario_atual <= 1500.00:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario_atual * (porcentagem / 100)
novo_salario = salario_atual + aumento

print("Resumo do reajuste:")
print(f"Salário antes do reajuste: R$ {salario_atual:,.2f}")
print(f"Porcentagem de aumento aplicada: {porcentagem}%")
print(f"Valor do aumento: R$ {aumento:,.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:,.2f}")