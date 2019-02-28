__alunos__ = ["flavio.urquidi@aluno.faculdadeimpacta.com.br", "gabriel.lsantos@aluno.faculdadeimpacta.com.br"]
import auxiliares as aux

def palavra_freq(dic_livro): # função que defini qual palavra e com qual frequencia aparece em uma lista
    for palavra in dic_livro:
                if dic_livro[palavra] > maximo:
                    maximo = dic_livro[palavra]
                    freq = palavra
    fm=[maximo,freq]                
    return(fm)                          

def conta_palavra_por_livro():
    """
    Devolve um Dicionário Python onde cada chave é o nome de um livro
    da Bíblia e o valor associado é um lista com a palavra mais frequente
    e o número de ocorrências da palavra.
    """
    livros = 0 
    palavras={}
    for linha in aux.le_teste(): # conta cada linha
        if aux.eh_novo_livro(linha): #verifica se é um novo livro
            dic = {livros:0} #cria o dicionario para armazenar os livros
            dic[livros] = palavra_freq(palavras) # caso seja um novo livro vai adionar a cada livro a palavra que mais aparece e a qtd de vezes que aparece
            palavras={} #zera o dicionario que conta as palavras e a frequencia
            livros += 1 # contador para saber em que livro estamos
        for palavra in linha.split(): #divide cada linha em palavras
            if  palavra in palavras:
                palavras[palavra] += 1 #adiciona mais um no contador de palavras no dic de palavras
            else:
                 palavras[palavra] = 1 #adiciona uma palavra que ainda nao apareceu
    
    return(dic)


print(conta_palavra_por_livro)