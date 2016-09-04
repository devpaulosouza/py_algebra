# -*- coding: utf-8 -*-
import copy

class matriz(object):
    matriz = []
    diagonal_principal = []
    diagonal_secundaria = []
    def __init__(self, lin:int, col:int, matriz):
        print()
        self.linhas = lin
        self.colunas = col
        self.matriz = matriz
        self.gera_matriz(matriz)
        self.is_quadrada = lin == col and lin != 0

    #Método para gerar uma matriz nula
    def gera_matriz(self,matriz):
        for i in range(self.linhas):
            #cria linha
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
        self.atualizar_diagonal_principal()
        self.atualizar_diagonal_secundaria()
        print()

    def mostrar(self):
        print(self)
        if len(self.matriz) > 0:
            for i in range(self.linhas):
                print(self.matriz[i])
            print()
        else:
            print("ERRO: Tamanho inválido para a matriz")

    def atualizar_diagonal_principal(self):
        diagonal = []
        if self.is_quadrada:
            for i in range(self.linhas):
                diagonal.append(int(self.matriz[i][i]))
            self.diagonal_principal = diagonal


    def atualizar_diagonal_secundaria(self):
        diagonal = []
        if self.is_quadrada:
            # "percorre" por todos os índices da matriz
            for i in range(self.linhas):
                for j in range(self.colunas):
                    # se i + j for igual a ordem da matriz + 1 então faz parte da diagonal secundária
                    if i+j == i+1:
                        diagonal.append(int(self.matriz[i][i]))
            self.diagonal_secundaria = diagonal
