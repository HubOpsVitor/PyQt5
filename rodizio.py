placa = int(input("Digite o final de sua placa veicular: "))

if placa==1 or placa==2:
    print("Rodízio na segunda-feira")
elif placa==3 or placa==4:
    print("Rodízio na terça-feira")
elif placa==5 or placa==6:
    print("Rodízio na quartaa-feira")
elif placa==7 or placa==8:
    print("Rodízio na quinta-feira")
elif placa==9 or placa==0:
    print("Rodízio na sexta-feira")
else:
    print("Placa inválida")