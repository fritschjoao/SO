from classes.cpu import CPU
from classes.cpu_estado import CPU_Estado
from classes.controlador import Controlador
from classes.job import Job
from classes.timer import Timer

# Classe So
class So:
    # Construtor
    def __init__(self):
        # Objeto CPU
        self.c = CPU()

        # Objeto CPU_Estado
        self.e = CPU_Estado()

        # Objeto Controlador
        self.controlador = Controlador()

        # Lista de Jobs
        self.jobs = []

        # Job atual
        self.job_atual = None
        self.pos_job = 0

        # Objeto Timer
        self.timer = Timer()
    
    # Inicializa SO
    def inicializa(self):
        # Coloca 2 jobs na lista
        self.jobs.append(Job('job1.json'))
        self.jobs.append(Job('job2.json'))

        # Coloca o job inicial da lista como o atual
        self.job_atual = self.jobs[self.pos_job]
        self.pos_job += 1

        # Inicializa o Estado da CPU
        self.e.inicializa()

        # Inicaliza o Estado interno da CPU
        self.c.altera_estado(self.e)

        # Inicializa a Memória do Programa interna da CPU
        self.c.altera_programa(self.job_atual.programa())

        # Inicializa a Memória de Dados interna da CPU
        self.c.altera_dados(([0]*self.job_atual.memoria()))

        # Inicializa o Timer
        self.timer.inicializa()

        # Inicia execução do progama
        self.controlador.executa(self)

    # Avança a lista job e atualiza a cpu
    def avanca_job(self):
        # if(self.pos_job-1 == len(self.jobs)):
        #     # Print informação
        #     print("A CPU PAROU NA INSTRUÇÃO: " + str(self.c.instrucao()))
        #     print("MEMORIA DE DADOS: " + str(self.c.salva_dados()))

        if (self.pos_job < len(self.jobs)):
            self.job_atual = self.jobs[self.pos_job]
            self.pos_job += 1

            # Inicializa o Estado da CPU
            self.e.inicializa()

            # Inicaliza o Estado interno da CPU
            self.c.altera_estado(self.e)

            # Inicializa a Memória do Programa interna da CPU
            self.c.altera_programa(self.job_atual.programa())

            # Inicializa a Memória de Dados interna da CPU
            self.c.altera_dados(([0]*self.job_atual.memoria()))

            return True

        return False

    def checa_interrupcao(self):
        self.c.salva_estado(self.e) # salva estado em c
        self.c.retorna_interrupcao() # retorna estado

    # Procura se a instrução foi ilegal mesmo
    def executa(self):
        if self.c.interrupcao() == "violacao":
            print("VIOLAÇÃO DE MEMÓRIA")
            return False

        if self.c.interrupcao() == "ilegal":
            if self.c.instrucao() == "PARA":
                self.job_atual.finalizado()
                #     # Print informação
                print("TERMINANDO O JOB: " + self.job_atual.nome())
                print("A CPU PAROU NA INSTRUÇÃO: " + str(self.c.instrucao()))
                print("MEMORIA DE DADOS: " + str(self.c.salva_dados()))

                return False

            elif self.c.instrucao() == "LE":
                self.c.salva_estado(self.e) # salva o estado da cpu
                self.c.dormir()  # bota cpu para dormir
                self.timer.nova_interrupcao(self.job_atual.entrada_tempo(), self.job_atual.nome())

                self.LE()

                return True

            elif self.c.instrucao() == "GRAVA":
                self.c.salva_estado(self.e) # salva o estado da cpu
                self.c.dormir()  # bota cpu para dormir
                self.timer.nova_interrupcao(self.job_atual.saida_tempo(), self.job_atual.nome())

                self.GRAVA()

                return True
            else:
                print("INSTRUÇÃO NÃO RECONHECIDA")
                return False

    def LE(self):
        # LÊ DADO DO DISPOSITIVO E COLOCA NO ACUM
        with open(self.job_atual.entrada(), 'r') as file:
            dado = file.read().splitlines()
            self.c.setAcum(int(dado[0]))

    def GRAVA(self):
        with open(self.job_atual.saida(), 'w') as file:
            file.write(str(self.c.acum()))
        





