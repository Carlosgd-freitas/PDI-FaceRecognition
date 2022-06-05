import face_recognition
import pickle
import cv2
import utils

def Reconhecimento():
    """
    Inicializa o processo de reconhecimento facial através da webcam do usuário. Este processo pode ser
    finalizado a qualquer momento ao pressionar a tecla [Q].
    """

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    # Carregando o dicionário "data" salvo no arquivo binário "features"
    data = pickle.loads(open('features', "rb").read())
    
    # Inicializando a webcam
    print("A webcam foi inicializada.")
    print("Pressione a tecla [Q] enquanto a janela da Webcam estiver selecionada para finalizar a execução do programa.")
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # O código é executado enquanto os frames estiverem sendo capturados ou a tecla [Q] não for pressionada
    while True:
        # Captura um frame da webcam
        ret, frame = video_capture.read()
        if not ret:
            print('ERRO: O frame da câmera não pode ser capturado.')
            break

        # Convertendo o frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Localizando faces no frame
        faces = face_cascade.detectMultiScale(gray,
                                            scaleFactor=1.05,
                                            minNeighbors=5,
                                            minSize=(60, 60),
                                            flags=cv2.CASCADE_SCALE_IMAGE)
    
        # Convertendo o frame para RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Gerando os encodings das faces localizadas no frame
        encodings = face_recognition.face_encodings(rgb)

        names = [] # Vetor contendo os nomes dos indivíduos que foram localizados
        confidences = [] # Vetor contendo os valores de confiança para as faces localizadas
        matchedEncodings = [] # Vetor contendo os encodings das faces dos indivíduos que foram localizados

        # Para cada enconding
        for encoding in encodings:
            # Comparando o enconding do frame com os encodings extraídos da base de dados 
            matches = face_recognition.compare_faces(data["encodings"], encoding)

            # Primeiramente, um indivíduo será atribuído como "Desconhecido"
            name = "Desconhecido"

            # Se algum casamento foi realizado entre o enconding em questão e os encodings extraídos
            if True in matches:
                # Posições em que um casamento ocorreu (True)
                matchedIndexes = [i for (i, b) in enumerate(matches) if b]

                # Vetor contendo os nomes referentes à cada índice
                matchedNames = []

                # Dicionário que contará o número de casamentos para cada nome
                counts = {} 

                # Percorre o vetor que contém as posições em que casamentos ocorreram
                for i in matchedIndexes:
                    # Nome do indivíduo referente ao respectivo índice (i)
                    name = data["names"][i]

                    # Incrementando a contagem em 1 para o nome em questão
                    counts[name] = counts.get(name, 0) + 1

                    # Adicionando o nome à lista de nomes referentes à cada índice (i)
                    matchedNames.append(name)

                    # Adicionando o encoding à lista de encodings referentes à cada índice (i)
                    matchedEncodings.append(data["encodings"][i])

                # O indivíduo será atribuído com o nome com a maior contagem
                name = max(counts, key=counts.get)
    
            # Calculando a maior confiança obtida (em porcentagem) e atualizando a lista dos valores de confiança
            conf = utils.CalcularConfianca(encoding, matchedEncodings) * 100
            confidences.append(conf)

            # Atualizando a lista que contém os nomes dos indivíduos presentes no frame
            names.append(name)

            # Percorrendo as faces reconhecidas
            for ((x, y, w, h), name, conf) in zip(faces, names, confidences):
                # Desenhando a bounding box no frame
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 128), 2)

                # Montando o texto que será escrito na tela
                if conf > 0:
                    text = name + " (" + "{:.2f}".format(conf) + " %)"
                else:
                    text = name

                # Escrevendo o texto no frame
                cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 128), 2)

        cv2.imshow("Webcam", frame)

        # O programa será encerrado quando o usuário apertar a tecla [Q]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fechando as janelas da webcam
    video_capture.release()
    cv2.destroyAllWindows()
