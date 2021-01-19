class Controlador:
    def __init__(self):
        pass

    # Executa programa
    def executa(self, so):
        flag = True
        while(flag):

            # Passa o tempo
            so.timer.passa_tempo()

            if(so.timer.interrupcao() != "nenhum"):
                so.checa_interrupcao()

            # Se o estado da cpu é normal, executa
            if so.c.interrupcao() == 'normal':
                so.c.executa()

            # Se o estado for violacao ou ilegal, chama o SO
            if (so.c.interrupcao() == 'ilegal') or (so.c.interrupcao() == 'violacao'):
                flag = so.executa()

            if so.job_atual.estado():
                flag = so.avanca_job()
