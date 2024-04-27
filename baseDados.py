from random import randint
import csv
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class Pessoa:
    def __init__(self, idade, sexo, peso, altura, tp_sanguineo, gosto_musical, pratica_esporte, jogo_pref, forca, velocidade, inteligencia):
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.tp_sanguineo = tp_sanguineo
        self.gosto_musical = gosto_musical
        self.pratica_esporte = pratica_esporte
        self.jogo_pref = jogo_pref
        self.forca = forca
        self.velocidade = velocidade
        self.inteligencia = inteligencia


def insert_data():
    Nome_arquivo = 'baseDados.csv'

    for i in range(5000):
        force = 0
        speed = 0
        intelligence = 0
        altura = 0
        peso = 0
        idade = randint(12, 80)
        sexo = randint(0,1) #0 masculino   1 feminino
        if sexo == 0:
            if idade >= 12 and idade <= 14:
                altura = randint(150, 165)/100
                peso = randint(382,540)/10
                force = randint(45, 55)
                speed = randint(40, 60)
                intelligence = 50
            elif idade >=15 and idade <= 17:
                altura =randint(160, 180)/100
                peso = randint(540, 786)/10
                force = randint(60, 80)
                speed = randint(65, 85)
                intelligence = 65
            elif idade >= 18:
                altura = randint(170, 195)/100
                peso = randint(650, 841)/10
                if idade <= 30:
                    force = randint(85, 100)
                    speed = randint(85, 100)
                    intelligence = randint(75, 90)
                elif idade <= 50:
                    force = randint(50, 70)
                    speed = randint(50, 70)
                    intelligence = randint(85, 100)
                elif idade <= 70:
                    force = 25
                    speed = 20
                    intelligence = 75
                else:
                    force = 5
                    speed = 2
                    intelligence = 65
        else:
            if idade >= 12 and idade <= 14:
                altura = randint(150, 159)/100
                peso = randint(397, 630) / 10
                force = randint(45, 55)
                speed = randint(40, 60)
                intelligence = 55

            elif idade >=15 and idade <= 17:
                altura =randint(160, 172)/100
                peso = randint(510, 680) / 10
                force = randint(50, 70)
                speed = randint(60, 75)
                intelligence = 70
            elif idade >= 18:
                altura = randint(170, 185)/100
                peso = randint(543, 728) / 10
                if idade <= 30:
                    force = randint(70, 95)
                    speed = randint(75, 100)
                    intelligence = randint(80, 100)
                elif idade <= 50:
                    force = randint(40, 60)
                    speed = randint(45, 70)
                    intelligence = randint(85, 100)
                elif idade <= 70:
                    force = 20
                    speed = 18
                    intelligence = 80
                else:
                    force = 4
                    speed = 1
                    intelligence = 70



        tp_sanguineo_lista = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        tp_sanguineo = tp_sanguineo_lista[randint(0, 7)]
        force += randint(1,10)
        speed += randint(1,10)
        intelligence += randint(1,10)
        gosto_musical_lista = ['Pop', 'Rock', 'Pagode', 'Sertanejo', 'Hip-Hop/Rap', 'Eletronica', 'Funk', 'Metal', 'Demais generos estranhos']
        gosto_musical = gosto_musical_lista[randint(0, 8)]
        esporte_lista = ['Futebol', 'Basquete', 'Volei', 'Luta', 'Atletismo', 'eSports', 'Nada']
        esporte= esporte_lista[randint(0, 6)]
        if esporte == 'Futebol':
            force += randint(65, 80)
            speed += randint(65, 85)
            intelligence += randint(50, 65)
        elif esporte == 'Basquete':
            force += randint(90, 100)
            speed += randint(70, 85)
            intelligence += randint(75, 85)
        elif esporte == 'Volei':
            force += randint(70, 80)
            speed += randint(45, 60)
            intelligence += randint(80, 92)
        elif esporte == 'Luta':
            force += randint(97, 100)
            speed += randint(40, 55)
            intelligence += randint(50, 65)
        elif esporte == 'Atletismo':
            force += randint(70, 95)
            speed += 100
            intelligence += randint(40, 55)
        elif esporte == 'eSports':
            force += randint(20, 35)
            speed += randint(15, 30)
            intelligence += randint(80, 100)
        elif esporte == 'Nada':
            force += randint(15, 30)
            speed += randint(10, 25)
            intelligence += randint(25, 35)
        jogo_lista = ['Counter-Strike', 'Minecraft', 'Fortnite', 'The Witcher', 'Valorant', "Assassin's Creed", 'World of Warcraft', 'FIFA', 'League of Legends', 'Dota', 'Rocket League', 'Outro - pouco relevante']
        jogo = jogo_lista[randint(0, 11)]
        if jogo == 'Counter-Strike':
            force += randint(-5,3)
            speed += randint(1,5)
            intelligence += randint(2, 5)
        elif jogo == 'Minecraft':
            force += randint(-5,3)
            speed += randint(-4,2)
            intelligence += randint(-1, 3)
        elif jogo == 'Fortnite':
            force += randint(-5,3)
            speed += randint(1,6)
            intelligence += randint(-5, 2)
        elif jogo == 'The Witcher':
            force += randint(-5, 3)
            speed += randint(-2,2)
            intelligence += randint(-2,2)
        elif jogo == 'Valorant':
            force += randint(-5, 3)
            speed += randint(1,5)
            intelligence += randint(2, 5)
        elif jogo == "Assassin's Creed":
            force += randint(-5, 3)
            speed += randint(-2, 2)
            intelligence += randint(-2, 2)
        elif jogo == 'World of Warcraft':
            force += randint(-5, 3)
            speed += randint(-3,1)
            intelligence += randint(2,7)
        elif jogo == 'FIFA':
            force += randint(-5, 3)
            speed += randint(-2,2)
            intelligence += randint(-2,3)
        elif jogo == 'League of Legends':
            force += randint(-5, 3)
            speed += randint(1,5)
            intelligence += randint(3,7)
        elif jogo == 'Dota':
            force += randint(-5, 3)
            speed += randint(1,4)
            intelligence += randint(3,8)
        elif jogo == 'Rocket League':
            force += randint(-5, 3)
            speed += randint(-3,1)
            intelligence += randint(-2,2)
        elif jogo == 'Outro - pouco relevante':
            force += randint(-5, 3)
            speed += randint(-1,1)
            intelligence += randint(-1,-1)
        if sexo == 0:
            sexo = 'M'
        else:
            sexo = 'F'
        if idade > 65:
            esporte = esporte_lista[6]

        force /= 2
        speed /= 2
        intelligence /= 2
        if force > 100:
            force = 100
        if speed > 100:
            speed = 100
        if intelligence > 100:
            intelligence = 100

        hospedeiro = Pessoa(idade, sexo, peso, altura, tp_sanguineo, gosto_musical, esporte, jogo, force, speed, intelligence)

        if op == 1:
            try:
                with open(Nome_arquivo, "r"):
                    cabecalho = []
            except FileNotFoundError:
                cabecalho = ["Idade", "Sexo", "Peso", "Altura", "Tipo sanguineo", "Gosto Musical",
                             "Pratica Esporte", "Jogo preferido", "Forca", "Velocidade", "Inteligencia"]

            with open(Nome_arquivo, "a", newline="") as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                if cabecalho:
                    escritor.writerow(cabecalho)
                escritor.writerow([hospedeiro.idade, hospedeiro.sexo, hospedeiro.peso, hospedeiro.altura,
                                   hospedeiro.tp_sanguineo, hospedeiro.gosto_musical, hospedeiro.pratica_esporte,
                                   hospedeiro.jogo_pref, hospedeiro.forca, hospedeiro.velocidade, hospedeiro.inteligencia])

    print('Dados salvos com sucesso!')


def predict():
    if os.path.exists('baseDados_hospedeiros.pkl'):

        model = joblib.load('baseDados_hospedeiros.pkl')

        nova_linha = {'Idade': 80, 'Sexo': 0, 'Peso': 80, 'Altura': 1.85,
                      'Tipo sanguineo': 3, 'Gosto Musical': 4, 'Pratica Esporte': 6, 'Jogo preferido': 0}
        nova_linha_df = pd.DataFrame(nova_linha, index=[0])

        previsao = model.predict(nova_linha_df)
        print('Força:', previsao[0][0])
        print('Velocidade:', previsao[0][1])
        print('Inteligencia:', previsao[0][2])
    else:
        hospedeiros = pd.DataFrame()
        try:
            hospedeiros = pd.read_csv('baseDados.csv')
            # print(hospedeiros.head())
            hospedeiros['Sexo'] = hospedeiros['Sexo'].replace('M', 0)
            hospedeiros['Sexo'] = hospedeiros['Sexo'].replace('F', 1)

            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('A+', 0)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('A-', 1)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('B+', 2)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('B-', 3)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('AB+', 4)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('AB-', 5)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('O+', 6)
            hospedeiros['Tipo sanguineo'] = hospedeiros['Tipo sanguineo'].replace('O-', 7)

            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Pop', 0)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Rock', 1)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Pagode', 2)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Sertanejo', 3)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Hip-Hop/Rap', 4)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Eletronica', 5)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Funk', 6)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Metal', 7)
            hospedeiros['Gosto Musical'] = hospedeiros['Gosto Musical'].replace('Demais generos estranhos', 8)

            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('Futebol', 0)
            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('Basquete', 1)
            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('Volei', 2)
            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('Luta', 3)
            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('Atletismo', 4)
            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('eSports', 5)
            hospedeiros['Pratica Esporte'] = hospedeiros['Pratica Esporte'].replace('Nada', 6)

            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Counter-Strike', 0)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Minecraft', 1)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Fortnite', 2)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('The Witcher', 3)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Valorant', 4)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace("Assassin's Creed", 5)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('World of Warcraft', 6)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('FIFA', 7)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('League of Legends', 8)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Dota', 9)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Rocket League', 10)
            hospedeiros['Jogo preferido'] = hospedeiros['Jogo preferido'].replace('Outro - pouco relevante', 11)


        except FileNotFoundError:
            print("Arquivo 'baseDados.csv' não encontrado.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

        # Exemplo de conjunto de dados fictício

        # Converter os dados em um DataFrame
        columns = ['Idade', 'Sexo', 'Peso', 'Altura', 'Tipo sanguineo', 'Gosto Musical', 'Pratica Esporte',
                   'Jogo preferido', 'Forca', 'Velocidade', 'Inteligencia']
        df = pd.DataFrame(hospedeiros, columns=columns)

        # Separar as variáveis independentes (X) e as variáveis dependentes (y)
        x = df.drop(['Forca', 'Velocidade', 'Inteligencia'], axis=1)
        y = df[['Forca', 'Velocidade', 'Inteligencia']]
        df.drop('Gosto Musical', axis=1)

        # Dividir o conjunto de dados em treinamento e teste
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

        # Treinar um modelo de regressão linear
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        mse = mean_squared_error(y_test, y_pred)
        print(f'Erro Médio Quadrático: {mse}')
        joblib.dump(model, 'baseDados_hospedeiros.pkl')


def menu():
    print('[1]Inserir os dados na base de dados')
    print('[2]Salvar aprendizado de maquina .pkl')
    print('[0]Sair')

while True:
    menu()
    op = int(input())
    if op == 1:
        insert_data()
    elif op == 2:
        predict()
    elif op == 0:
        break
    else:
        pass