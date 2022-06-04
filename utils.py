import numpy as np

def RotuloEmNome(rotulo):
    """
    Recebe um número inteiro, correspondente ao rótulo de um indivíduo, e retorna o nome correspondente
    àquele indivíduo.
    """

    if rotulo == 1:
        return "Carlos_Freitas"
    
    elif rotulo == 2:
        return "Laura_Martins"
    
    else:
        return "Desconhecido"

def NomeEmRotulo(nome):
    """
    Recebe o nome de um indivíduo presente na base de dados e retorna o rótulo correspondente àquele indivíduo.
    """

    if nome == "Carlos_Freitas":
        return 1
    
    elif nome == "Laura_Martins":
        return 2
    
    else:
        return 0

def GerarArrayRotulos(nomes):
    """
    Recebe uma estrutura contendo nomes de indivíduos presente na base de dados e retorna um numpy array contendo
    os rótulos correspondente àqueles indivíduos.
    """
    array = list()

    for nome in nomes:
        rotulo = NomeEmRotulo(nome)
        array.append(rotulo)
    
    array = np.array(array, dtype = 'int32')
    return array
