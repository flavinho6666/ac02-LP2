__alunos__ = ["flavio.urquidi@aluno.faculdadeimpacta.com.br", "gabriel.lsantos@aluno.faculdadeimpacta.com.br"]
import auxiliares as aux


def conta_palavra_por_livro():
    """
    Devolve um Dicionário Python onde cada chave é o nome de um livro
    da Bíblia e o valor associado é um lista com a palavra mais frequente
    e o número de ocorrências da palavra.
    """

    cont_livro = 0

    dicionariozao = {}
    dic_livro = {}

    for linha in aux.le_teste:
        if aux.eh_novo_livro(linha):

            cont_livro += 1
            dic_livro = {}

        maximo = 0 
        freq = ''

        for palavra in dic_livro:
            if dic_livro[palavra] > maximo:
                maximo = dic_livro[palavra]
                freq = palavra          

            dicionariozao[cont_livro] = [freq, maximo]

        for palavra in linha.split():
            if palavra in dic_livro:
                dic_livro[palavra] += 1
            else:
                dic_livro[palavra] = 1

    return dicionariozao


conta_palavra_por_livro()
# dicionario [id =, lista(nome, count)]