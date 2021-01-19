# Classe CPU_Estado
class CPU_Estado:
    # Construtor
    def __init__(self):
        # Registradores:
        self.__pc = None  # Contador do programa
        self.__acum = None  # Acumulador

        # Código Interrupção:
        self.__estado = None  # Estado (normal, instrução ilegal ou violação de memória)

    # Inicializa o estado interno da CPU
    def inicializa(self):
        self.__pc = 0
        self.__acum = 0
        self.__estado = "normal"

    # Retorna o estado
    def estado(self):
        return self.__pc, self.__acum, self.__estado

    # Altera o valor do acumulador
    def altera_acumulador(self, acum):
        self.__acum = acum
    
    # Retorna o valor do acumulador
    def acumulador(self):
        return self.__acum