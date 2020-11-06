class CPU_Estado:
    def __init__(self):
        self.pc = None
        self.acum = None
        self.estado = None

    def inicializa(self):
        self.pc = 0
        self.acum = 0
        self.estado = "normal"


class CPU:
    def __init__(self):
        self.e = None
        self.programa = None
        self.dados = None

        self.instrucao = None
        self.argumento = None

    def alteraEstado(self, e):
        self.e = e

    def alteraPrograma(self, programa):
        self.programa = programa

    def alteraDados(self, dados):
        self.dados = dados

    def interrupcao(self):
        return self.e.estado

    def CARGI(self, n):
        self.e.acum = n

    def CARGM(self, n):
        self.e.acum = self.dados[n]

    def CARGX(self, n):
        self.e.acum = self.dados[self.dados[n]]

    def ARMM(self, n):
        self.dados[n] = self.e.acum

    def ARMX(self, n):
        self.dados[self.dados[n]] = self.e.acum

    def SOMA(self, n):
        self.e.acum += self.dados[n]

    def NEG(self):
        self.e.acum = -self.e.acum

    def DESVZ(self, n):
        if self.e.acum == 0:
            self.e.pc = n

    def executa(self):
        metodo = None # Executa a instrucao
        antigo_pc = self.e.pc # Guarda o antigo PC para testar depois da execução

        # Coloca na lista linha a instrução e o argumento separados
        # Exemplo linha = ['CARGI', '6']
        linha = self.programa[self.e.pc].split(' ')
        if '' in linha:
            linha.remove('')

        # Primeiro elemento é posto no objeto instrução
        # instrução = 'CARGI'
        self.instrucao = linha[0]

        # Se a instrução não existir, significa que acabou
        # então o estado é alterado para ilegal
        if not hasattr(self, self.instrucao):
            self.e.estado = 'ilegal'
            return

        # Variável método passa a ser a instrução
        # (função chamadora)
        metodo = getattr(self, self.instrucao)

        # Se a instrução possui argumentos
        if len(linha) > 1:
            self.argumento = int(linha[1])
            metodo(self.argumento) # Executa com argumento
        else: # Se não
            metodo() # Executa sem
        
        # Se não alterou o valor do pc, incrementa-o
        if antigo_pc == self.e.pc:
            self.e.pc = self.e.pc + 1


def extraiArquivo():
    arquivo = open('programa.txt', 'r')
    programa = arquivo.read().splitlines()
    arquivo.close()
    return programa

def main():
    cpu = CPU()
    cpu_estado = CPU_Estado()

    cpu_estado.inicializa()
    cpu.alteraEstado(cpu_estado)
    cpu.alteraPrograma(extraiArquivo())
    cpu.alteraDados([0]*20)
    
    cpu.executa()

    while cpu.interrupcao() == "normal":
        cpu.executa()

    print("A CPU PAROU NA INSTRUÇÃO: " + str(cpu.instrucao))
    print("MEMORIA DE DADOS: " + str(cpu.dados))

main()

