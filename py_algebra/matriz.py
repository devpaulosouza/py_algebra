# -*- coding: utf-8 -*-
from py_algebra import form as def_type

class matriz(object):
    matriz = []
    diagonal_principal = []
    diagonal_secundaria = []
    def __init__(self, lin:int, col:int):
        print()
        self.linhas = lin
        self.colunas = col
        self.matriz = []
        self.is_quadrada = lin == col and lin != 0
        self._gera_matriz()

    #Método para gerar uma matriz nula
    def _gera_matriz(self):
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
                    try:
                        # Preenche com o valor em float ou inteiro, dependendo do valor digitado
                        s = input('matriz %i,%i = '%(i,j))
                        self.matriz[i][j] = def_type.def_type(s)
                    except(ValueError):
                        print("Erro ao preencher a matriz. Digite um valor válido!")
                    else:
                        break
        self._atualizar_diagonais()
        print()

    # Método para alterar algum valor da matriz
    def alterar(self, i, j, v):
        try:
            self.matriz[i][j] = v
        except IndexError:
            print("Erro ao mudar valor. Indice para a matriz inválido!")
        else:
            self._atualizar_diagonais()

    def __str__(self):
        return str(self.matriz)

    def __add__(self, a):
        # Testa se matrizes são de mesma ordem
        if (self.linhas == a.linhas and self.colunas == a.colunas):
            resultante = matriz(a.linhas, a.colunas)
            for i in range(a.linhas):
                for j in range(a.colunas):
                    resultante.alterar(i, j, self.matriz[i][j] + a.matriz[i][j])
        else:
            resultante = -1
        return resultante

    def __sub__(self, a):
        # Testa se matrizes são de mesma ordem
        if (self.linhas == a.linhas and self.colunas == a.colunas):
            resultante = matriz(a.linhas, a.colunas)
            for i in range(a.linhas):
                for j in range(a.colunas):
                    resultante.alterar(i, j, self.matriz[i][j] - a.matriz[i][j])
        else:
            resultante = -1
        return resultante

    def __mul__(self, a):
        tipo = type(a)
        # se a é um escalar:
        if tipo == int or tipo == float:
            resultante = matriz(self.linhas, self.colunas)
            # multiplica cada elemento da matriz pelo escalar
            for i in range(self.linhas):
                for j in range(self.colunas):
                    resultante.alterar(i, j, self.matriz[i][j]*a)
        # caso a for uma matriz, verifica se é possivel a multiplicação l==c
        elif tipo == matriz and self.colunas == a.linhas:
            resultante = matriz(self.linhas, a.colunas)
            # percorre todos elementos da matriz
            for i in range(self.linhas):
                for j in range(self.linhas):
                    somatorio = 0.0
                    # percorre todos os elementos coluna a ser multiplicada da matriz a
                    for k in range(self.colunas):
                        somatorio = somatorio + self.matriz[i][k] * a.matriz[k][j]
                    # Corrige o tipo do elemento (int or float)
                    somatorio = def_type.def_type(somatorio)
                    resultante.alterar(i,j,somatorio)
        else:
            resultante = -1

        return resultante

    def _atualizar_diagonais(self):
        diagonal_secundaria = []
        diagonal_principal = []
        if self.is_quadrada:
            # "percorre" por todos os índices da matriz
            for i in range(self.linhas):
                for j in range(self.colunas):
                    # se i + j for igual a ordem da matriz + 1 então faz parte da diagonal secundária
                    if i+j == i+1:
                        diagonal_principal.append(int(self.matriz[i][i]))
                    elif i+j == self.linhas + 1:
                        diagonal_secundaria.append(int(self.matriz[i][j]))

            self.diagonal_secundaria = diagonal_principal
            self.diagonal_secundaria = diagonal_secundaria
        else:
            self.diagonal_principal = -1
            self.diagonal_secundaria = -1

    def gera_pivo (self, linha):
        v = self.matriz[linha]
        var_pivotada = 0
        try:
            for i in range(self.colunas):
                var_pivotada = v[i]
                if var_pivotada != 0:
                    break
                else:
                    var_pivotada = var_pivotada if var_pivotada > 0 else -var_pivotada
            if var_pivotada:
                for i in range(self.colunas):
                    aux = v[i]/var_pivotada
                    v[i] = def_type.def_type(aux)
        except IndexError:
            print ("Erro: linha a ser pivotada não existe")
        else:
            self.matriz[linha] = v

    def zera_coluna(self, linha_pivotada):
        coluna = -1
        # procura a coluna a ser zerada. (onde existir pivô)
        for i in range(self.colunas):
            if self.matriz[linha_pivotada][i] == 1:
                coluna = i
                break
        try:
            if self.matriz[linha_pivotada][coluna] == 1:
                for i in range(self.linhas):
                    aux = -self.matriz[i][coluna]
                    for j in range(self.colunas):
                        if i != linha_pivotada:
                            valor = aux*self.matriz[linha_pivotada][j]+self.matriz[i][j]
                            self.alterar(i,j,valor)
        except IndexError:
            print ("Erro: coluna a ser pivotada não existe")
        except UnboundLocalError:
            print("Erro: linha %d não está pivotada"%linha_pivotada)

    def gauss_jordan(self):
        aux = []
        for i in range(self.linhas):
            if i < self.colunas:
                # troca as linhas se não for possivel pivotar
                if self.matriz[i][i] == 0:
                    for j in range(self.linhas):
                        # troca aqui:
                        if self.matriz[j][i] != 0:
                            aux = matriz[i]
                            self.matriz[i] = self.matriz[j]
                            self.matriz[j] = aux
                else:
                    self.gera_pivo(i)
                    self.zera_coluna(i)
