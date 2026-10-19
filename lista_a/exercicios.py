"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
  pass
    total = 0
    for n in lista:
        if n < 0:
            total = total + 1
    return total


def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
pass

if len(lista) == 0:
        return 0
    soma = 0
    for n in lista:
        soma = soma + n
    resultado = soma / len(lista)
    return resultado

def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    pass

if len(lista) == 0:
        return []
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    nova = []
    ja_tirou = False
    for n in lista:
        if n == maior and ja_tirou == False:
            ja_tirou = True
        else:
            nova.append(n)
    return nova

def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    pass

nova = []
    soma = 0
    for n in lista:
        soma = soma + n
        nova.append(soma)
    return nova

def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    pass

nova = []
    for sublista in lista_de_listas:
        for item in sublista:
            nova.append(item)
    return nova

# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    pass

 posicao = -1
    tamanho = len(lista)
    for i in range(tamanho):
        if lista[i] == alvo:
            posicao = i
    return posicao


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    pass

 total = 0
    for n in lista:
        if n == alvo:
            total = total + 1
    return total

def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    pass

tamanho = len(lista)
    for i in range(tamanho):
        if lista[i] > limite:
            return i
    return -1

def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    pass

 inicio = 0
    fim = len(lista) - 1
    posicao = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            posicao = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return posicao

# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    pass

 soma = 0
    operacoes = 0
    for n in lista:
        operacoes = operacoes + 1
        if n % 2 == 0:
            soma = soma + n
    return soma, operacoes

def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    pass

 maior = lista[0]
    comparacoes = 0
    tamanho = len(lista)
    for i in range(1, tamanho):
        comparacoes = comparacoes + 1
        if lista[i] > maior:
            maior = lista[i]
    return maior, comparacoes

def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    pass

     comparacoes = 0
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            comparacoes = comparacoes + 1
            if lista[i] + lista[j] == alvo:
                return True, comparacoes
    return False, comparacoes



def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    pass

 if len(lista) <= 1:
        return True, 0
    comparacoes = 0
    tamanho = len(lista)
    for i in range(tamanho - 1):
        comparacoes = comparacoes + 1
        if lista[i] > lista[i + 1]:
            return False, comparacoes
    return True, comparacoes

# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    pass

 inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        temporaria = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = temporaria
        inicio = inicio + 1
        fim = fim - 1

def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    pass

 inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio = inicio + 1
        fim = fim - 1
    return True

def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    pass

  inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        soma = lista[inicio] + lista[fim]
        if soma == alvo:
            return inicio, fim
        elif soma < alvo:
            inicio = inicio + 1
        else:
            fim = fim - 1
    return -1, -1

def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    pass

soma_atual = 0
    for i in range(k):
        soma_atual = soma_atual + lista[i]
    melhor_soma = soma_atual
    tamanho = len(lista)
    for i in range(k, tamanho):
        soma_atual = soma_atual + lista[i] - lista[i - k]
        if soma_atual > melhor_soma:
            melhor_soma = soma_atual
    return melhor_soma

def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pass

 balanco = 0
    for caractere in texto:
        if caractere == "(":
            balanco = balanco + 1
        elif caractere == ")":
            balanco = balanco - 1
        if balanco < 0:
            return False
    if balanco == 0:
        return True
    else:
        return False