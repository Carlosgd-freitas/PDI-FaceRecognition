import math
import numpy as np
import face_recognition

def DistanciaEmConfianca(face_distance, face_match_threshold=0.6):
    """
    Recebe uma distância resultante da comparação de duas faces e um limiar, e retorna um valor de confiança.
    """
    if face_distance > face_match_threshold:
        range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range * 2.0)
        return linear_val
    else:
        range = face_match_threshold
        linear_val = 1.0 - (face_distance / (range * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

def CalcularConfianca(face_enconding_frame, face_encondings_database, face_match_threshold = 0.6):
    """
    Retorna um valor de confiança para a menor distância encontrada entre o enconding do frame da webcam
    e os encondigs da base de dados que foram casados na etapa de reconhecimento facial.
    """
    dists = face_recognition.face_distance(face_encondings_database, face_enconding_frame)

    menor = 99999
    for d in dists:
        if d < menor:
            menor = d

    return DistanciaEmConfianca(menor, face_match_threshold)

def RotuloEmNome(rotulo):
    """
    Recebe um número inteiro, correspondente ao rótulo de um indivíduo, e retorna o nome correspondente
    àquele indivíduo.
    """

    if rotulo == 1:
        return "Carlos_Freitas"
    
    elif rotulo == 2:
        return "Laura_Martins"
    
    elif rotulo == 3:
        return "Barbara_Leticia"
    
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
    
    elif nome == "Barbara_Leticia":
        return 3
    
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
