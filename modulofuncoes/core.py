def somaLista(valores=[]):
    """
    A função somaLista recebe uam lista de números 
    e faz a soma de todos os números da lista e retorna
    o resultado da soma.
    Parameteres
    _________________________________________________  
    valores: int[]
        Lista de números para a soma
  
        Returns
    _________________________________________________
        Retorna a soma de uma lista
    """

    resultado = 0
    for i in valores:
        resultado+=i

    return resultado

def MaiorValor(lista=[]):

    """
A funçãoo maiorValor encontra o maior
em uma lista númérica

Parameteres
    _________________________________________________  
    lista: int[]
        Lista de números para a soma
  
        Returns
    _________________________________________________
        Retorna o maior valor da lista

    """

    m = lista[0]
    for i in lista:
        if i > m:
            m = i

    return m

def inverter(palavra=""):
    # Vamos utiliza o comando len(length)
    # len(length-comprimento) para obter
    # a quantidade de caracteres da palavra
    qtd = len(palavra)
    invertida = ""
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida
    
def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"
