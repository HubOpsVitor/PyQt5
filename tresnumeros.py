n1 = int (input ("Digite um número: "))
n2 = int (input ("Digite outro número: "))
n3 = int (input ("Digite um último número: "))

if n1 >= n2 & n1 >= n3: 
    print(f"O número {n1} é maior")
elif n2 >= n1 & n1 >= n3:
    print(f"O número {n2} é maior")
else:
    print(f"O número {n3} é maior")