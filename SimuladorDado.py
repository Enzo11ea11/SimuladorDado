#simulador de dado

import random

class SimuladorDeDado:
    def __init__(self):
        self.valorMin = 1;
        self.valorMax = 6;
        self.mensagem = 'você gostaria de gerar novo valor?';

    def Iniciar(self):
        resposta = 'sim';
        while resposta == 'sim' or resposta == 's':
            resposta = input(self.mensagem);
            if resposta == 'sim' or resposta == 's':
                self.ValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print("Obrigado pela sua participação")
            else:
                print("Favor digitar sim ou não")

    def ValorDoDado(self):
        print(random.randint(self.valorMin,self.valorMax))

simulador = SimuladorDeDado();
simulador.Iniciar();