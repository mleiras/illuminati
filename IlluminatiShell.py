from cmd import Cmd
from IPython.display import clear_output
from IlluminatiWindow import IlluminatiWindow
from IlluminatiEngine import IlluminatiEngine

class IlluminatiShell(Cmd):
    intro = 'Illuminati shell. Type help or ? to list commands.\n'
    prompt = 'Illuminati> '
    
    def print_puzzle(self, puzzle):
        clear_output(wait=True)
        i=1
        print("  ",end="")
        for col_num in range(1,len(puzzle[0])+1):
            print(f"{col_num:2d}",end="")
        print()
        for linha in puzzle:
            print(f"{i:2d}",end=" ")
            i+=1
            for simbolo in linha:
                print(simbolo,end=" ")
            print()
            
    def do_mr(self, arg):
        " -  comando mostrar que leva como parâmetro o nome de um ficheiro..: mr <nome_ficheiro> \n" \
        " -  opcionalmente pode colocar um segundo parametro com o tamanho da casa..: mr <nome_ficheiro> <tamanho>\n" 
        lista_arg = arg.split()
        try:
            lista_arg = arg.split()
            eng.ler_tabuleiro_ficheiro(lista_arg[0])
            self.print_puzzle(eng.gettabuleiro())
            #self.do_ver(arg) #ou as linhas seguintes
            global janela  # pois pretendo atribuir um valor a um identificador global
            if janela is not None:
                del janela  # invoca o metodo destruidor de instancia __del__()
            janela = IlluminatiWindow(40, eng.getlinhas(), eng.getcolunas())
            janela.mostraJanela(eng.gettabuleiro())
        except Exception as e:
            print("Erro: ", e)
                          
    def do_cr(self, arg):
        " -  comando carregar que leva como parâmetro o nome de um ficheiro..: cr <nome_ficheiro> \n"
        try:
            lista_arg = arg.split()
            eng.gravar_tabuleiro_ficheiro(lista_arg[0])
            print("Tabuleiro guardado no ficheiro: "+lista_arg[0])
        except:
            print("Formato inválido!")

    def do_gr(self, arg):
        " -  comando gravar que leva como parâmetro o nome de um ficheiro..: gr <nome_ficheiro> \n"
        try:
            lista_arg = arg.split()
            eng.gravar_tabuleiro_ficheiro(lista_arg[0])
            print("Tabuleiro guardado no ficheiro: "+lista_arg[0])
        except:
            print("Formato inválido!")
    
    def do_jg(self, arg):
        " - Colocação da lâmpada se possível nas coordenadas (linha, coluna) inseridas..: jg <coordenadas> \n" \
        " - Exemplo formato das coordenadas 'jg 1 2'"
        try:
            jogada = arg.split()
            lin = int(jogada[0]) - 1
            col = int(jogada[1]) - 1
            if eng.jg(lin, col):
                self.print_puzzle(eng.gettabuleiro())
                self.do_ver(arg)
                self.do_verify_victory(arg)
            else:
                print("Casa bloqueada!")
        except:
            print("Formato de coordenadas inválido!")

    def do_mc(self, arg):
        " - Marcação da casa nas coordenadas inseridas (linha, coluna) onde será impossível colocar uma lâmpada..: mc <coordenadas> \n" \
        " - Exemplo formato 'mc 1 2'"
        try:
            jogada = arg.split()
            lin = int(jogada[0]) - 1
            col = int(jogada[1]) - 1
            if eng.mc(lin, col):
                self.print_puzzle(eng.gettabuleiro())
                self.do_ver(arg)
            else:
                print("Casa bloqueada!")
        except:
            print("Formato de coordenadas inválido!")
    
    def do_est1(self, arg):
        " - Execução da estratégia 1..: est1\n" \
        " - Casa com um número n com exatamente n casas vizinhas, então essas mesmas terão lâmpadas"
        eng.estrategia1()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)
     
    def do_est2(self, arg):
        " - Execução da estratégia 2..: est2\n" \
        " - Marcar como iluminadas todas as casas na mesma linha e coluna de uma lâmpada (que não estejam bloqueadas)"
        eng.estrategia2()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)
    
    def do_est3(self, arg):
        " - Execução da estratégia 3..: est3\n" \
        " - Bloquear todas as casas em que se verifique impossível que esta contenha uma lâmpada"
        eng.estrategia3()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)
    
    def do_est4(self, arg):
        " - Execução da estratégia 4..: est4\n" \
        " - Em casos de dois números numa diagonal (1 e 3) e haver certeza que as casas partilhadas não podem ter as duas iluminadas"
        eng.estrategia4()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)
    
    def do_est5(self, arg):
        " - Execução da estratégia 5..: est5\n" \
        " - Verifica se uma casa não iluminada só pode ser iluminada se uma dada casa tiver uma lâmpada (devido a outras restrições)"
        eng.estrategia5()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)

    def do_est6(self, arg):
        " - Execução da estratégia 6..: est6\n" \
        " - Caso as estratégias 1-5 não resolvam totalmente o puzzle, aplica-se a tentativa-erro para casas com apenas duas opções disponíveis para ficar iluminada"
        eng.estrategia6()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)
    
    def do_est7(self, arg):
        " - Execução da estratégia 7 no puzzle..: est7\n" \
        " - Caso as estratégias 1-6 não resolvam totalmente o puzzle, aplica-se a tentativa-erro para casas com 3 ou mais opções disponíveis para ficar iluminada"
        eng.estrategia7()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)

    def do_undo(self, arg):
        " - Retorna um passo atrás no tabuleiro..: undo"  
        if eng.undo():
            self.print_puzzle(eng.gettabuleiro())
            self.do_ver(arg)
        else:
            print("Encontra-se no início do tabuleiro, não é possível retornar!")

    def do_rtstart(self, arg):
        " - Retorna o puzzle para o início..: rtstart"
        eng.returnStart()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
 
    def do_resolve(self, arg):
        " - Resolve o puzzle automaticamente..: resolve" 
        eng.resolve()
        self.print_puzzle(eng.gettabuleiro())
        self.do_ver(arg)
        self.do_verify_victory(arg)

    def do_verify_victory(self, arg):
        " - Verifica o puzzle construído no momento e passa uma mensagem de resposta..: verify_victory"
        iluminado = True
        lampadas = True
        if eng.verify_lights() is False: iluminado = False
        if eng.check_numbers() is False: lampadas = False
        if iluminado and lampadas: print("Puzzle resolvido corretamente!")
        elif iluminado is False and lampadas: print("Puzzle todo iluminado, mas lâmpadas colocadas incorretamente!")
        elif iluminado and lampadas is False: print("Lâmpadas corretamente colocadas, mas puzzle não se encontra totalmente iluminado!")
        else: print("Puzzle incorreto!") 
    
    def do_ver(self, arg):
        " - Comando para visualizar o estado atual do puzzle em ambiente grafico caso seja válido: VER  \n"
        global janela  # pois pretendo atribuir um valor a um identificador global
        if janela is not None:
            del janela  # invoca o metodo destruidor de instancia __del__()
        janela = IlluminatiWindow(40, eng.getlinhas(), eng.getcolunas())
        janela.mostraJanela(eng.gettabuleiro())
    
    def do_sair(self, arg):
        "Sair do programa illuminati: sair"
        print('Obrigado por ter utilizado o illuminati, espero que tenha sido divertido!')
        global janela  # pois pretendo atribuir um valor a um identificador global
        if janela is not None:
            del janela  # invoca o metodo destruidor de instancia __del__()
        return True


if __name__ == '__main__':
    eng = IlluminatiEngine()
    janela = None
    sh = IlluminatiShell()
    sh.cmdloop()