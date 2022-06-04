from imutils import paths
import face_recognition
import pickle
import cv2
import os
 
def GerarEncondingNomes(database_path, verbose = 0):
    """
    Percorre a base de dados e gera o arquivo binário "features", que conterá os encodings das faces e os nomes
    dos indivíduos para cada imagem presente no banco de dados.

    Parâmetros:
    * database_path: Caminho do diretório que contém a base de dados. A base de dados é dividida em diretórios, 
    onde cada um deles tem o nome de um indivíduo, e contém fotos deste mesmo indivíduo
    * verbose: Se possuir o valor 1, imprime as imagens que estão sendo processadas. O valor padrão é 0.
    """

    # Lista contendo os arquivos presentes na base de dados
    database = list(paths.list_images(database_path))

    knownEncodings = [] # Vetor que armazenará os encodings das faces
    knownNames = []     # Vetor que armazenará os nomes dos indivíduos

    # Percorrendo a base de dados
    for (i, imagePath) in enumerate(database):

        if verbose:
            print(f'Processando imagem no caminho: {imagePath}')

        # Extraindo o nome do indivíduo do caminho da imagem
        name = imagePath.split(os.path.sep)[1]

        # Carregando a imagem e a convertendo para RGB
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Gerando as bounding boxes e localizando faces
        bounding_boxes = face_recognition.face_locations(rgb, model='hog')

        # Gerando os encodings das bounding boxes das faces reconhecidas
        encodings = face_recognition.face_encodings(rgb, bounding_boxes)

        # Percorrendo os encodings
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    # Salvando os encodings das faces e os nomes dos indivíduos no dicionário "data"
    data = {"encodings": knownEncodings, "names": knownNames}

    # Salvando o dicionário "data" no arquivo binário "features"
    f = open("features", "wb")
    f.write(pickle.dumps(data))
    f.close()
