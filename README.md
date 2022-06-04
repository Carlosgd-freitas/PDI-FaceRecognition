# PDI-FaceRecognition
Implementação do Trabalho Prático da disciplina de Processamento de Imagens.

## Instalação de Bibliotecas
Instalando a biblioteca numpy:
```pip install numpy```

Instalando a biblioteca dlib no windows:
```pip install dlib-19.22.99-cp39-cp39-win_amd64```

Instalando a biblioteca opencv-contrib:
```pip install opencv-contrib-python```

Instalando a biblioteca face_recognition:
```pip install face_recognition```

## Executando o Código
Para executar o código, basta rodar a linha de comando ```python main.py```. Esteja ciente que, para indivíduos que não estejam presentes na base de dados, o programa irá atribuir "Desconhecido" ao reconhecer suas faces.

## Adicionando Dados à Base de Dados
1. Crie uma pasta, com o nome do indivíduo, dentro da pasta **Database**.
2. Adicione imagens deste indivíduo na pasta criada.

## Argumentos Opcionais
Ao adicionar o argumento ```--noextraction``` ao executar o código, a etapa de extração de características dos indivíduos presentes na base de dados será pulada. Isso é útil para agilizar o programa no caso de execuções subsequentes com o mesmo estado da base de dados (nenhuma imagem foi adicionada, removida ou alterada).
