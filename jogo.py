#chegar e finais diferentes na historia, utilizando respostas diferentes

#Cenario: Eu estou em uma guerra entre nações, e nós temos 2 lados: LadoA e LadoB. Somente o ladoA irá vencer, e o ladoB irá
#perder! entao eu tenho que tomar as deciçoes corretas para chegar a vitória

class JogoDeAventura:
    def  __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (Norte/Sul)' #norte = LadoA, sul = LadoB
        self.pergunta2 = 'Voce prefere espada ou escudo? (Espada/Escudo)' #espada = LadoA, Escudo = LadoB
        self.pergunta3 = 'Qual é a sua especialidade? (Batalha/Tatica)' #Batalha = ladoA = tático = ladoB
        self.finalHistoria1 = 'Voce será um heroi de batalha!'
        self.finalHistoria2 = 'Voce será um heroi protegendo nosas tropas'
        self.finalHistoria3 = 'Voce irá se sacrificar na batalha'
        self.finalHistoria4 = 'Voce não é capaz de lutar nessa batalha'


    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'Norte':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'Espada':
                    print(self.finalHistoria1)
            if resposta1B == 'Escudo':
                    print (self.finalHistoria2)
        if resposta1 == 'Sul':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'Batalha':
                    print(self.finalHistoria3)
            if resposta1B == 'Tatica':
                    print(self.finalHistoria4)

jogo = JogoDeAventura()
jogo.Iniciar()
