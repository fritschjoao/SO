# Classe CPU
class CPU:
    # Construtor
    def __init__(self):
        # Memórias:
        self.__programa = None # Memória do programa
        self.__dados = None # Memória de dados

        # Registradores:
        self.__pc = None  # Contador do programa
        self.__acum = None  # Acumulador

        # Código Interrupção:
        self.__estado = None  # Estado (normal, instrução ilegal ou violação de memória)

        # Outros:
        self.__instrucao = None # Instrução atual da CPU
        self.__argumento = None # Argumento atual da CPU

    # Altera o conteúdo da memória de programa
    def altera_programa(self, programa):
        self.__programa = programa

    # Altera o conteúdo da memória de dados
    def altera_dados(self, dados):
        self.__dados = dados

    # Retorna o conteúdo da memória de dados
    def salva_dados(self):
        return self.__dados

    # Lẽ o estado da CPU
    def interrupcao(self):
        return self.__estado
    
    # Coloca a CPU em modo normal
    def retorna_interrupcao(self):
        if (self.__estado != "normal"):
            self.__estado = "normal"
            self.__pc += 1

    # Retorna a instrução em PC
    def instrucao(self):
        return self.__instrucao

    # Retorna o estado interno da CPU
    def salva_estado(self):
        return self.__pc, self.__acum, self.__estado

    # Altera o estado interno da CPU
    def altera_estado(self, e):
        self.__pc = e.pc
        self.__acum = e.acum
        self.__estado = e.estado

    # Leitura a um endereço da memória de programa
    # Retona o endereço em n se foi possível, ou -1 se houve acesso inválido
    def le_endereco_programa(self, n):
        if (n >= len(self.__programa)):
            return -1
        else:
            return self.__programa[n]

    # Leitura a um endereço da memória de dados
    # Retona o endereço em n se foi possível, ou -1 se houve acesso inválido
    def le_endereco_dados(self, n):
        if (n >= len(self.__dados)):
            return -1
        else:
            return self.__dados[n]

    # Altera um endereço da memória de dados
    # Retona True se foi possível, ou -1 se houve acesso inválido
    def altera_endereco_dados(self, n, novo_dado):
        if (n >= len(self.__dados)):
            return -1
        else:
            self.__dados[n] = novo_dado

    # INSTRUÇÕES:
    # Coloca o valor n no acumulador
    def CARGI(self, n):
        self.__acum = n

    # Coloca no acumulador o valor na posição n da memória de dados
    def CARGM(self, n):
        retorno = self.le_endereco_dados(n)
        if retorno == -1:
            self.__estado = "violacao"
        else:
            self.__acum = retorno

    # Coloca no acumulador o valor na posição que está na posição 
    # n da memória de dados
    def CARGX(self, n):
        retorno = self.le_endereco_dados(self.__dados[n])
        if retorno == -1:
            self.__estado = "violacao"
        else:
            self.__acum = retorno

    # Coloca o valor do acumulador na posição n da memória de dados
    def ARMM(self, n):
        retorno = self.altera_endereco_dados(n, self.__acum)
        if retorno == -1:
            self.__estado = "violacao"
        else:
            return

    # Coloca o valor do acumulador na posição que está na posição n da memória de dados
    def ARMX(self, n):
        retorno = self.altera_endereco_dados(self.__dados[n], self.__acum)
        if retorno == -1:
            self.__estado = "violacao"
        else:
            return

    # Soma ao acumulador o valor no endereço n da memória de dados
    def SOMA(self, n):
        retorno = self.le_endereco_dados(n)
        if retorno == -1:
            self.__estado = "violacao"
        else:
            self.__acum += retorno

    # Inverte o sinal do acumulador
    def NEG(self):
        self.__acum = -(self.__acum)

    # Se A vale 0, coloca o valor n no PC
    def DESVZ(self, n):
        if self.__acum == 0:
            self.__pc = n
    # FIM INSTRUÇÕES

    # Passa a instrução para os atributos
    # "instrucao" e "argumento" da classe
    def procura_instrucao(self):
        # Pega a linha do endereço pc e coloca na lista "linha"
        # e separa o argumento por espaço (ex: linha = ["CARGI", "10"])
        retorno = self.__programa[self.__pc]
        if retorno == -1:
            self.__estado = "violacao"
            return
        else:
            linha = retorno.split(' ')
        
        # Usado apenas se o arquivo estiver configurado com mais espaços
        if '' in linha:
            linha.remove('')

        # instrucao = "CARGI"
        self.__instrucao = str(linha[0])

        # Se a lista linha possui mais de um elemento,
        # então é uma instrução com argumento
        if len(linha) > 1:
            self.__argumento = int(linha[1])
        else:
            self.__argumento = None
        
    # Verifica se a instrução é inválida
    def instrucao_invalida(self):
        # Procura se existe um método na classe com o nome 
        # da instrução
        return ( not hasattr(self, self.__instrucao) )

    # Verifica se há argumento
    def argumento(self):
        return (self.__argumento != None)
            
    # Executa uma instrução
    def executa(self):
        antigo_pc = self.__pc  # Guarda o antigo pc para teste posterior

        # Atribui os comandos
        self.procura_instrucao()

        # Verifica se não houve violação de memória no caminho
        if self.__estado == "violacao":
            return

        # Verifica se é instrução inválida
        if self.instrucao_invalida():
            self.__estado = "ilegal"
            return

        # Variável método passa a ser a instrução
        # (função chamadora)
        metodo = getattr(self, self.__instrucao)

        # Verifica se a instrução é com ou sem argumento
        if self.argumento():
            metodo(self.__argumento)
        else:
            metodo()

        # Se a instrução não alterou o valor do PC nem sinalizou interrupção, 
        # incrementa o valor do PC
        if (antigo_pc == self.__pc) and (self.__estado == "normal"):
            self.__pc += 1