# Classe CPU_Estado
class CPU_Estado:
    # Construtor
    def __init__(self):
        # Registradores:
        self.pc = None  # Contador do programa
        self.acum = None  # Acumulador

        # Código Interrupção:
        self.estado = None  # Estado (normal, instrução ilegal ou violação de memória)

    # Inicializa o estado interno da CPU
    def inicializa(self):
        self.pc = 0
        self.acum = 0
        self.estado = "normal"