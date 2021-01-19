import json

# Classe Job:
class Job:
    def __init__(self, arquivo):
        data = self.extrai_json(arquivo)

        self.__nome = arquivo
        self.__programa = self.extrai_programa(data["programa"])
        self.__memoria = int(data["memoria"])
        self.__entrada = data["entrada"]
        self.__saida = data["saida"]

        self.__estado = False

    def extrai_json(self, arquivo):
        with open("./descritores/" + arquivo, 'r', encoding='utf-8') as file:
            return json.load(file)

    def extrai_programa(self, programa):
        with open("./programas/" + programa, 'r', encoding='utf-8') as file:
            return file.read().splitlines()

    def programa(self):
        return self.__programa

    def memoria(self):
        return self.__memoria

    def entrada(self):
        return self.__entrada['local']

    def saida(self):
        return self.__saida['local']

    def entrada_tempo(self):
        return int(self.__entrada['tempo'])

    def saida_tempo(self):
        return int(self.__saida['tempo'])

    def nome(self):
        return self.__nome

    def finalizado(self):
        self.__estado = True

    def estado(self):
        return self.__estado