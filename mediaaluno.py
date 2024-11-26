media = float(input("Digite a média do aluno:  "))

if media >= 6:
    print(f"O aluno com média de {media} está aprovado")
elif media <= 4:
    print(f"O aluno com média de {media} está reprovado")
else:
    print(f"O aluno com média de {media} está em recuperação")
