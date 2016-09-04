# -*- coding: utf-8 -*-
import copy

class matriz(object):
    matriz = []
    is_quadrada = False
    def __init__(self, lin:int, col:int, matriz):
        print()
        self.linhas = lin
        self.colunas = col
        self.matriz = matriz
        self.gera_matriz(matriz)

    #Método para gerar valores na matriz automaticamente
    def gera_matriz(self,matriz):
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                linha.append(0)
            self.matriz.append(linha)


    #Método para preencher a matriz com valores fornecidos pelo usuário
    def ler_matriz(self):
        s = ""
        print("Informe os valores para a matriz por gentileza: ")
        for i in range(self.linhas):
            for j in range(self.colunas):
                #Trata erros caso o usuário informe algo diferente de número
                while True:
                    s = input('matriz %i,%i = '%(i,j))
                    if s.isdigit():
                        self.matriz[i][j] = int(s)
                        break
                    else:
                        print("ERRO: Favor informe um número válido")
        print()

    def mostrar(self):
        print(self)
        if len(self.matriz) > 0:
            print("Matriz: ")
            for i in range(self.linhas):
                print(self.matriz[i])
            print()
        else:
            print("ERRO: Tamanho inválido para a matriz")
