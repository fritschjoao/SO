# Classe do Escalonador
class Escalonador:
    def __init__(self):
        self.__jobs = []
        self.__job_atual = None

    def inicializa(self, jobs):
        self.jobs = jobs
        