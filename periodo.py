periodo = (input("Digite o período em que você estuda, M para Matutino, V para Vespertino e N para Noturno: "))

if periodo == 'M' or periodo == 'm':
    print(f"Um bom dia pra você que estuda no perído da manhã!")
elif periodo == 'V' or periodo == 'v':
    print(f"Uma boa tarde pra você que estuda no perído da tarde!")
elif periodo == 'N' or periodo == 'n':
    print(f"Uma boa noite pra você que estuda no perído da noite!")