# Classe Timer

class Interrupcao:
    def __init__(self, tempo, tipo):
        self.tempo = tempo
        self.tipo = tipo

class Timer:
    def __init__(self):
        self.__contador = None
        self.__interrupcoes = None

    def inicializa(self):
        self.__contador = 0
        self.__interrupcoes = []

    def passa_tempo(self):
        self.__contador += 1

    def tempo_atual(self):
        return self.__contador

    def interrupcao(self):
        interrupcao = None
        flag = False
        i = 0
        for i in range(len(self.__interrupcoes)):
            if self.__interrupcoes[i].tempo == self.__contador:
                flag = True
                interrupcao = self.__interrupcoes[i]

        if flag:
            j = self.__interrupcoes.pop(i)
            return j.tipo
        
        return "nenhum"
                
    def nova_interrupcao(self, tempo, tipo):
        self.__interrupcoes.append(Interrupcao(self.__contador+tempo, tipo))

    