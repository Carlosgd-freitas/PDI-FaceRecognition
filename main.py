import argparse
import extracao_caracteristicas
import webcam_reconhecimento

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument('--noextraction', action='store_true',
                    help='A Etapa de Extração de Características do banco de dados não será executada.')
args = parser.parse_args()

# Caminho do diretório que contém a base de dados. A base de dados é dividida em diretórios, onde cada um deles
# tem o nome de um indivíduo, e contém fotos deste mesmo indivíduo
database_path = 'Database'

if __name__ == '__main__':

    # Primeira Etapa: Extração de Características
    if(not args.noextraction):
        print('Inicializando etapa de extração de características no banco de dados...')
        extracao_caracteristicas.GerarEncondingNomes(database_path, verbose = 1)
        print("A extração de características foi finalizada, e os dados foram salvos no arquivo binário 'features'.\n")

    # Segunda Etapa: Reconhecimento Facial na Webcam
    print('Inicializando etapa de reconhecimento facial na webcam...')
    webcam_reconhecimento.Reconhecimento()
    print('Encerrando o programa.\n')
