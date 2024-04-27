import csv
import os
import joblib
import pandas as pd
import platform
from random import randint


class Pessoa:
    def __init__(self, idade, sexo, peso, altura, tp_sanguineo, gosto_musical, pratica_esporte, jogo_pref):
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.tp_sanguineo = tp_sanguineo
        self.gosto_musical = gosto_musical
        self.pratica_esporte = pratica_esporte
        self.jogo_pref = jogo_pref

'''def busca_hospedeiro(idade, sexo, peso, altura, tp_sanguineo, gosto_msc, esporte, jogo_pref):
    with open('hospedeiros.csv', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)

        for linha in leitor:
            if idade in linha and sexo in linha and peso in linha and altura in linha and tp_sanguineo in linha and gosto_msc in linha and esporte in linha and jogo_pref in linha:
                return True
        return False'''

def mostrar_tipos(escolhas):
    print('Informe o tipo sanguíneo: \n')

    for i in range(len(tp_sanguineo)):
        print(f'[{i+1}]{tp_sanguineo[i]}')

    op = int(input())
    while True:
        if op >= 1 and op <= 8:
            escolhas.append(tp_sanguineo[op-1])
            break
        else:
            op = int(input())

    print('Informe o gosto musical: \n')
    for i in range(len(gosto_musical)):
        print(f'[{i+1}]{gosto_musical[i]}')

    op = int(input())
    while True:
        if op >= 1 and op <= 9:
            escolhas.append(gosto_musical[op-1])
            break
        else:
            op = int(input())

    print('Informe o esporte que pratica: \n')
    for i in range(len(esporte)):
        print(f'[{i+1}]{esporte[i]}')
    op = int(input())
    while True:
        if op >= 1 and op <= 7:
            escolhas.append(esporte[op-1])
            break
        else:
            op = int(input())

    print('Informe o jogo preferido: \n')
    for i in range(len(jogos)):
        print(f'[{i+1}]{jogos[i]}')
    op = int(input())
    while True:
        if op >= 1 and op <= 12:
            escolhas.append(jogos[op-1])
            break
        else:
            op = int(input())

    return escolhas


def show_hospedeiros():
    os.system(clear)
    df = pd.read_csv('hospedeiros.csv')
    print('══════════════════════════════════════════════')
    for i in range(len(df)):
        linha_escolhida = df.iloc[i]
        idade = linha_escolhida['Idade']
        sexo = linha_escolhida['Sexo']
        peso = linha_escolhida['Peso']
        altura = linha_escolhida['Altura']
        tp_sangue = linha_escolhida['Tipo sanguineo']
        gosto_msc = linha_escolhida['Gosto Musical']
        prtc_esporte = linha_escolhida['Pratica Esporte']
        jogo_pref = linha_escolhida['Jogo preferido']
        print(f'Idade: {idade}\nSexo: {sexo}\nPeso: {peso}\nAltura: {altura}\nTipo Sanguíneo: {tp_sangue}'
              f'\nGosto Musical: {gosto_msc}\nPratica qual Esporte: {prtc_esporte}\nJogo Preferido: {jogo_pref}')
        predict(idade, sexo , peso, altura, tp_sangue, gosto_msc, prtc_esporte, jogo_pref)

        print('══════════════════════════════════════════════')

def predict(idade, sexo , peso, altura, tp_sangue, gosto_msc, prtc_esporte, jogo_pref):
    if os.path.exists('baseDados_hospedeiros.pkl'):
        sexo = sexo.replace('M', '0')
        sexo = sexo.replace('F', '1')

        tp_sangue = tp_sangue.replace('A+', '0')
        tp_sangue = tp_sangue.replace('A-', '1')
        tp_sangue = tp_sangue.replace('B+', '2')
        tp_sangue = tp_sangue.replace('B-', '3')
        tp_sangue = tp_sangue.replace('AB+', '4')
        tp_sangue = tp_sangue.replace('AB-', '5')
        tp_sangue = tp_sangue.replace('O+', '6')
        tp_sangue = tp_sangue.replace('O-', '7')

        gosto_msc = gosto_msc.replace('POP', '0')
        gosto_msc = gosto_msc.replace('ROCK', '1')
        gosto_msc = gosto_msc.replace('PAGODE', '2')
        gosto_msc = gosto_msc.replace('SERTANEJO', '3')
        gosto_msc = gosto_msc.replace('HIP-HOP/RAP', '4')
        gosto_msc =gosto_msc.replace('ELETRONICA', '5')
        gosto_msc =gosto_msc.replace('FUNK', '6')
        gosto_msc = gosto_msc.replace('METAL', '7')
        gosto_msc = gosto_msc.replace('DEMAIS GENEROS', '8')

        prtc_esporte = prtc_esporte.replace('FUTEBOL', '0')
        prtc_esporte = prtc_esporte.replace('BASQUETE', '1')
        prtc_esporte = prtc_esporte.replace('VOLEI', '2')
        prtc_esporte = prtc_esporte.replace('LUTA', '3')
        prtc_esporte = prtc_esporte.replace('ATLETISMO', '4')
        prtc_esporte =prtc_esporte.replace('eSPORTS', '5')
        prtc_esporte = prtc_esporte.replace('NADA', '6')

        jogo_pref = jogo_pref.replace('COUNTER-STRIKE', '0')
        jogo_pref = jogo_pref.replace('MINECRAFT', '1')
        jogo_pref = jogo_pref.replace('FORTNITE', '2')
        jogo_pref = jogo_pref.replace('THE WITCHER', '3')
        jogo_pref = jogo_pref.replace('VALORANT', '4')
        jogo_pref = jogo_pref.replace("ASSASSIN'S CREED", '5')
        jogo_pref = jogo_pref.replace('WORLD OF WARCRAFT', '6')
        jogo_pref = jogo_pref.replace('FIFA', '7')
        jogo_pref = jogo_pref.replace('LEAGUE OF LEGENDS', '8')
        jogo_pref = jogo_pref.replace('DOTA', '9')
        jogo_pref = jogo_pref.replace('ROCKET LEAGUE', '10')
        jogo_pref = jogo_pref.replace('OUTRO - POUCO RELEVANTE', '11')
        if tp_sangue == 'A2':
            tp_sangue = '4'
        elif tp_sangue == 'A3':
            tp_sangue = '5'

        model = joblib.load('baseDados_hospedeiros.pkl')
        nova_linha = {
            'Idade': idade,
            'Sexo': int(sexo),
            'Peso': peso,
            'Altura': altura,
            'Tipo sanguineo': int(tp_sangue),
            'Gosto Musical': int(gosto_msc),
            'Pratica Esporte': int(prtc_esporte),
            'Jogo preferido': int(jogo_pref)
        }

        df = pd.DataFrame([nova_linha])

        previsao = model.predict(df)
        '''print(f'Força: {previsao[0][0]:.3f}')
        print(f'Velocidade: {previsao[0][1]:.3f}')
        print(f'Inteligência: {previsao[0][2]:.3f}')'''
        Forca_global = previsao[0][0]
        Velocidade_global = previsao[0][1] + randint(0, 5)
        Inteligencia_global = previsao[0][2]
        print(f'Força: {Forca_global:.3f}')
        print(f'Velocidade: {Velocidade_global:.3f}')
        print(f'Inteligência: {Inteligencia_global:.3f}')
        FVI[0] = Forca_global
        FVI[1] = Velocidade_global
        FVI[2] = Inteligencia_global


def pato_zumbi():
    os.system(clear)
    if os.path.exists('hospedeiros.csv'):
        print('[1]Identificar Zumbi')
        print('[0]Sair')
        op = int(input())
        os.system(clear)
        while True:
            if op == 1:
                df= pd.read_csv('hospedeiros.csv')
                indice_aleatorio = randint(0, len(df)-1)
                linha_aleatoria = df.iloc[indice_aleatorio]
                idade = linha_aleatoria['Idade']
                sexo = linha_aleatoria['Sexo']
                peso = linha_aleatoria['Peso']
                altura = linha_aleatoria['Altura']
                tp_sangue = linha_aleatoria['Tipo sanguineo']
                gosto_msc = linha_aleatoria['Gosto Musical']
                prtc_esporte = linha_aleatoria['Pratica Esporte']
                jogo_pref = linha_aleatoria['Jogo preferido']
                predict(idade, sexo , peso, altura, tp_sangue, gosto_msc, prtc_esporte, jogo_pref)

                soma = FVI[0] + FVI[1] + FVI[2]
                distancia = randint(25, 50)
                print()
                print(f'Um zumbi foi avistado a cerca de {distancia} metros!!')
                print('-------------------------------------------------------------')
                if soma >= 240:
                    print('O zumbi identificado é Extremamente perigoso')
                elif soma >= 200:
                    print('O zumbi identificado é muito perigoso')
                elif soma >= 160:
                    print('O zumbi identificado é perigoso')
                elif soma >= 115:
                    print('O zumbi identificado contem risco moderado')
                else:
                    print('O zumbi identificado é praticamente inofencivo')

                menor = min(FVI)
                indice_menor = FVI.index(menor)

                maior = max(FVI)
                indice_maior = FVI.index(maior)
                print('-------------------------------------------------------------')
                fraqueza = ''
                if indice_menor == 0:
                    print('O ponto fraco deste zumbi é a força')
                    fraqueza = 'Força'
                elif indice_menor == 1:
                    print('O ponto fraco deste zumbi é a velocidade')
                    fraqueza = 'Velocidade'
                elif indice_menor == 2:
                    print('O ponto fraco deste zumbi é a inteligência')
                    fraqueza = 'Inteligência'
                print('-------------------------------------------------------------')
                if indice_maior == 0:
                    print('O principal atributo do zumbi é a força')
                    print('O recomendado seria um ataque com 2 patos')
                elif indice_maior == 1:
                    print('O principal atributo do zumbi é a velocidade')
                    print('O recomendado seria um ataque através do voo')
                elif indice_maior == 2:
                    print('O principal atributo do zumbi é a Inteligência')
                    print('O recomendado seria um ataque surpresa')
                print('-------------------------------------------------------------')
                print('[1]Atacar')
                print('[2]Desistir de atacar')
                op = int(input())
                os.system(clear)
                while True:
                    if op == 1:
                        if indice_maior == 0:
                            print('Os patos foram equipados')
                        else:
                            print('O pato foi equipado')
                        print('Pronto para atacar o zumbi!')
                        print('Fraqueza: ',fraqueza)
                        chance_acerto = 1
                        if FVI[indice_menor] > 70:
                            chance_acerto = 0
                        print('\n[1]Atacar a fraqueza Força')
                        print('[2]Atacar a fraqueza Velocidade')
                        print('[3]Atacar a fraqueza Inteligência')
                        print('[4]Desistir de atacar')
                        op = int(input())
                        if op == 1:
                            if fraqueza == 'Força':
                                print('O zumbi foi eliminado com sucesso!!')
                            else:
                                if chance_acerto == 0 and randint(1, 10) > 6:
                                    print('Mesmo não atacando a fraqueza corretamente')
                                    print('O zumbi foi eliminado com sucesso!!')
                                elif chance_acerto == 1 and randint(1, 10) > 3:
                                    print('Mesmo não atacando a fraqueza corretamente')
                                    print('O zumbi foi eliminado com sucesso!!')
                                else:
                                    print('O ataque não foi feito na fraqueza do zumbi e ele resistiu ao ataque')
                            break
                        if op == 2:
                            if fraqueza == 'Velocidade':
                                print('O zumbi foi eliminado com sucesso!!')
                            else:
                                if chance_acerto == 0 and randint(1, 10) > 6:
                                    print('Mesmo não atacando a fraqueza corretamente')
                                    print('O zumbi foi eliminado com sucesso!!')
                                elif chance_acerto == 1 and randint(1, 10) > 3:
                                    print('Mesmo não atacando a fraqueza corretamente')
                                    print('O zumbi foi eliminado com sucesso!!')
                                else:
                                    print('O ataque não foi feito na fraqueza do zumbi e ele resistiu ao ataque')
                            break
                        if op == 3:
                            if fraqueza == 'Inteligência':
                                print('O zumbi foi eliminado com sucesso!!')
                            else:
                                if chance_acerto == 0 and randint(1, 10) > 6:
                                    print('Mesmo não atacando a fraqueza corretamente')
                                    print('O zumbi foi eliminado com sucesso!!')
                                elif chance_acerto == 1 and randint(1, 10) > 3:
                                    print('Mesmo não atacando a fraqueza corretamente')
                                    print('O zumbi foi eliminado com sucesso!!')
                                else:
                                    print('O ataque não foi feito na fraqueza do zumbi e ele resistiu ao ataque')
                            break
                        if op == 4:
                            break

                    elif op == 2:
                        break
                    else:
                        print('[1]Atacar')
                        print('[2]Desistir de atacar')
                        op = int(input())



            elif op == 0:
                break
            else:
                pass
            print('[1]Identificar Zumbi')
            print('[0]Sair')
            op = int(input())
    else:
        print('O arquivo nã existe, por isso não há dados suficientes para identificar')
        input("Pressione Enter para continuar...")

def catlg_hospedeiro():
    os.system(clear)
    print('CADASTRO DO HOSPEDEIRO')
    Nome_arquivo = 'hospedeiros.csv'

    while True:
        idade = int(input('Informe a idade: '))
        if idade >= 6 and idade <= 90:
            break
    while True:
        sexo = input('Informe o sexo(M/F): ').upper()
        if sexo == 'M' or sexo == 'F':
            break
    while True:
        peso = float(input('Informe o peso: '))
        altura = float(input('Informe a altura: '))
        if peso >= 20 and peso <= 130 and altura >= 1.25 and altura <= 2.10:
            break

    escolhas = []
    mostrar_tipos(escolhas)
    tp_sanguineo = escolhas[0]
    gosto_musical = escolhas[1]
    pratica_esportes = escolhas[2]
    jogo_pref = escolhas[3]


    #if busca_hospedeiro(str(idade), sexo, str(peso), str(altura), tp_sanguineo, gosto_musical, pratica_esportes, jogo_pref):
     #   print('\033[91mOs dados que foram inseridos já existem!!\33[0m')

    hospedeiro = Pessoa(idade, sexo, peso, altura, tp_sanguineo, gosto_musical, pratica_esportes, jogo_pref)

    print(f'Idade: {hospedeiro.idade} | Sexo: {hospedeiro.sexo}'
          f' | Peso: {hospedeiro.peso} | Altura: {hospedeiro.altura} | Tipo sanguíneo: {hospedeiro.tp_sanguineo}'
          f' | Gosto musical: {hospedeiro.gosto_musical} | Esporte: {hospedeiro.pratica_esporte}'
          f' | Jogo preferido: {hospedeiro.jogo_pref}')


    op = int(input('Deseja salvar esses dados?\n[1]SIM\n[2]NÃO\n'))

    while True:
        if op == 1:
            try:
                with open(Nome_arquivo, "r"):
                    cabecalho = []
            except FileNotFoundError:
                cabecalho = ["Idade", "Sexo","Peso" ,"Altura", "Tipo sanguineo", "Gosto Musical", "Pratica Esporte", "Jogo preferido"]

            with open(Nome_arquivo, "a", newline="") as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                if cabecalho:
                    escritor.writerow(cabecalho)
                escritor.writerow([hospedeiro.idade, hospedeiro.sexo, hospedeiro.peso, hospedeiro.altura,
                                   hospedeiro.tp_sanguineo, hospedeiro.gosto_musical, hospedeiro.pratica_esporte,
                                   hospedeiro.jogo_pref])
            print('Dados salvos com sucesso!')
            break
        elif op == 2:
            print('Os dados não foram salvos!')
            break
        else:
            print('Por favor digite 1 ou 2')
            op = int(input())
    input("Pressione Enter para continuar...")


def menu():
    os.system(clear)
    menu_itens = ["[1]Catalogar Hospedeiro", "[2]Mostrar os Atributos dos Zumbis já salvos", "[3]Identificar Zumbi", "[0]Sair"]
    largura = max(len(item) for item in menu_itens)
    linha_superior = '╔' + '═' * (largura + 2) + '╗'
    linha_inferior = '╚' + '═' * (largura + 2) + '╝'

    print('\n\t\t\t\t\t\t  MENU')
    print('\t', linha_superior)
    for item in menu_itens:
        print(f'\t ║ {item:{largura}} ║')
    print('\t', linha_inferior)

FVI = [0, 0, 0]
Forca_global = 0
Velocidade_global = 0
Inteligencia_global = 0
tp_sanguineo = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
gosto_musical = ['POP', 'ROCK', 'PAGODE','SERTANEJO','HIP-HOP/RAP', 'ELETRONICA', 'FUNK', 'METAL', 'DEMAIS GENEROS']
esporte = ['FUTEBOL', 'BASQUETE', 'VOLEI', 'LUTA', 'ATLETISMO', 'eSPORTS', 'NADA']
jogos = ['COUNTER-STRIKE', 'MINECRAFT', 'FORTNITE', 'THE WITCHER', 'VALORANT', "ASSASSIN'S CREED",
        'WORLD OF WARCRAFT', 'FIFA', 'LEAGUE OF LEGENDS', 'DOTA', 'ROCKET LEAGUE', 'OUTRO - POUCO RELEVANTE']

clear = 'clear'
if platform.system() == 'Windows':
    clear = 'cls'

while True:
    menu()
    op = int(input())
    if op == 1:
        catlg_hospedeiro()
    elif op == 2:
        show_hospedeiros()
    elif op == 3:
        pato_zumbi()
    elif op == 0:
        break
    else:
        pass
