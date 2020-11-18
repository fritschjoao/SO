# ELC1080 | Sistemas Operacionais | 20b
# Trabalho 1 – Simulação de escalonamento de processos
# Professor: Benhur Stein
# Aluno: João Gabriel Fritsch
# Matrícula: 201911074
# Arquivo main

from classes.cpu import CPU
from classes.cpu_estado import CPU_Estado

# Retorna uma lista de strings em que cada elemento é uma linha do arquivo
def extraiArquivo():
    arquivo = open('programa.txt', 'r')
    programa = arquivo.read().splitlines()
    arquivo.close()
    return programa

# Função main
def main():
    # Memória de Programa
    programa = extraiArquivo()

    # O n é o numero de linhas do programa
    n = len(programa)

    # Memória de Dados (lista com n zeros)
    dados = ([0]*n)

    # Objeto CPU
    c = CPU()

    # Objeto CPU_Estado
    e = CPU_Estado()

    # Inicializa o Estado da CPU
    e.inicializa()

    # Inicaliza o Estado interno da CPU
    c.altera_estado(e)

    # Inicializa a Memória do Programa interna da CPU
    c.altera_programa(programa)

    # Inicializa a Memória de Dados interna da CPU
    c.altera_dados(dados)

    # Executa até achar instrução ilegal
    while c.interrupcao() == "normal":
        c.executa()

    # Print informação
    print("A CPU PAROU NA INSTRUÇÃO: " + str(c.instrucao()))
    print("MEMORIA DE DADOS: " + str(c.salva_dados()))

if __name__== '__main__':
    main()