from stack import *

class IlluminatiEngine:
    def __init__(self) -> None:
        '''Cria uma nova instância do Jogo.
        '''
        self.linhas = 0
        self.colunas = 0
        self.tabuleiro = []
        self.historico = Stack()
    
    def ler_tabuleiro_ficheiro(self, filename: str) -> bool:
        '''Lê um ficheiro de texto com um puzzle para resolver.

        Parameters
        ----------
        filename : str
            nome de ficheiro de texto com o puzzle (formato .ill)

        Returns
        -------
        estado: bool
            True/False se consegue ler bem o ficheiro ou se ocorreu algum erro na sua leitura.
        '''
        try:
            print(filename)
            print("--------------------")
            ficheiro = open(filename, "r")
            lines = ficheiro.readlines()
            dim = lines[0].strip('\n').split(' ')  # obter os dois numeros da dimensao do puzzle, retirando o '\n' 
            self.linhas = int(dim[0])  # retirar o numero de linhas
            self.colunas = int(dim[1])  # retirar o numero de colunas
            self.tabuleiro = []
            del lines[0]  # remover primeira linha da lista de linhas pois ja nao precisamos
            for line in lines:
                self.tabuleiro.append(line.split())
            self.add_historico()
            estado = True
        except:
            print("Erro: na leitura do tabuleiro")
            estado = False
        else:
            ficheiro.close()
        return estado
    
    def gravar_tabuleiro_ficheiro(self, filename: str) -> bool:
        '''Guarda um novo ficheiro de texto com o puzzle atual. 

        Parameters
        ----------
        filename : str
            nome de ficheiro de texto com o puzzle (formato .ill)

        Returns
        -------
        estado: bool
            True/False se consegue guardar bem o ficheiro ou se ocorreu algum erro na sua escrita.
        '''
        try:
            ficheiro = open(filename, "w+") # abre o ficheiro para escrita
            ficheiro.write(str(self.colunas)+' '+str(self.linhas)+'\n') # escreve na 1a linha do ficheiro <NR_COLUNAS> <NR_LINHAS> do puzzle
            for linha in self.tabuleiro:
                linha_f = ''
                for coluna in linha:
                    linha_f = linha_f + coluna + ' '
                    # print('linha_f: '+linha_f)
                ficheiro.write(linha_f + '\n')
            estado = True    
        except:
            print("Erro: ao guardar o tabuleiro no ficheiro " + filename)
            estado = False
        else:
            ficheiro.close()
        return estado

    def getlinhas(self) -> int:
        '''Função que retorna o nº de linhas do tabuleiro atual

        Returns
        -------
        int
            Nº de linhas do tabuleiro atual
        '''
        return self.linhas
    
    def getcolunas(self) -> int:
        '''Função que retorna o nº de colunas do tabuleiro atual

        Returns
        -------
        int
            Nº de colunas do tabuleiro atual
        '''
        return self.colunas
    
    def gettabuleiro(self) -> list:
        '''Função que retorna o tabuleiro atual na forma de matriz

        Returns
        -------
        list
            Matriz com valores do tabuleiro do jogo
        '''
        return self.tabuleiro

    def add_historico(self) -> None:
        '''Função que adiciona à stack do histórico as alterações feitas ao tabuleiro.
        '''
        new_tab = []
        for lin in self.tabuleiro:
            linha = []
            for col in lin:
                linha.append(col)
            new_tab.append(linha)
        self.historico.push(new_tab)


    def undo(self) -> bool:
        '''Função que desfaz a última alteração no tabuleiro.

        Returns
        -------
        res : bool
            new_tab é o tabuleiro sem as alterações feitas anteriormente e que foram retiradas
        '''
        if self.historico.size() == 1:
            res = False
        else:
            self.historico.pop()
            if self.historico.size() >= 1:
                self.tabuleiro = []
                for lin in self.historico.top():
                    linha = []
                    for col in lin:
                        linha.append(col)
                    self.tabuleiro.append(linha)
            res = True
        return res

    def returnStart(self):
        while self.historico.size() != 1:
            self.historico.pop()
        self.tabuleiro = []
        for lin in self.historico.top():
            linha = []
            for col in lin:
                linha.append(col)
            self.tabuleiro.append(linha)
        return 1
        
    def jg(self, l: int, c: int) -> bool:
        '''Função que permite fazer uma jogada no tabuleiro, marcando uma lâmpada numa casa disponível ou desmarcando caso exista uma lâmpada nesse local.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que quer jogar
        c : int
            Nº inteiro que corresponde à coluna da casa que quer jogar

        Returns
        -------
        res: bool
            True/False caso a jogada seja bem sucedida (colocar/retirar uma lâmpada) ou se a tentativa foi feita numa casa bloqueada.
        '''
        pos = self.tabuleiro[l][c]
        if pos == "@":
            self.tabuleiro[l][c] = "-"
            self.add_historico()
            res = True
        elif pos in "xo.01234": 
            res = False
        else:
            self.tabuleiro[l][c] = "@"
            self.IlluminaTotal(l, c)
            self.add_historico()
            res = True
        return res
        
    def mc(self, l: int, c: int) -> bool:
        '''Função que permite fazer uma marcação no tabuleiro, marcando uma casa bloqueada numa casa disponível.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que quer marcar
        c : int
            Nº inteiro que corresponde à coluna da casa que quer marcar

        Returns
        -------
        res: bool
            True/False caso a marcação seja bem sucedida ou se a tentativa foi feita numa casa bloqueada.
        '''
        pos = self.tabuleiro[l][c]
        if pos in "xo.01234":
            res = False
        else:
            self.tabuleiro[l][c] = "."
            self.add_historico()
            res = True
        return res

    #### ESTRATÉGIA 1 ####

    def casas_vizinhas_disp(self, l: int, c: int) -> list:
        '''Função que verifica se as casas adjacentes à casa fornecida estão disponíveis.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        disp: list
            Lista de coordenadas correspondentes às casas vizinhas disponíveis
        '''
        disp = []
        poss = [(l,0,-1,0),(l,self.linhas-1,1,0),(c,0,0,-1),(c,self.colunas-1,0,1)]
        for p in poss:
            if p[0] != p[1] and self.tabuleiro[l + p[2]][c + p[3]] == "-":
                disp.append([l + p[2],c + p[3]])
        return disp

    def num_lampadas_vizinhas(self, l: int, c: int) -> int:
        '''Função que conta o número de lâmpadas em casas adjacentes à casa fornecida.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        counter: int
            Nº inteiro referenete ao nº de lâmpadas
        '''
        counter = 0
        poss = [(l,0,-1,0),(l,self.linhas-1,1,0),(c,0,0,-1),(c,self.colunas-1,0,1)]
        for p in poss:
            if p[0] != p[1] and self.tabuleiro[l + p[2]][c + p[3]] == "@":
                counter += 1
        return counter

    def estrategia1_cada_casa(self, l: int, c: int, n: int) -> None:
        '''Função de suporte para Estratégia 1 que faz a jogada caso encontre uma casa n e com exatamente n casas vizinhas disponíveis.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        n : int
            Nº inteiro que corresponde ao Nº presente nessa casa no tabuleiro
        '''
        casas_disp = self.casas_vizinhas_disp(l,c)
        num_casas_disp = len(casas_disp)
        num_lampadas = self.num_lampadas_vizinhas(l,c)
        if (n - num_lampadas == num_casas_disp) and num_casas_disp > 0:
            for casa in casas_disp:
                self.jg(casa[0], casa[1])

    def estrategia1(self) -> None:
        '''Aplicação da Estratégia 1 por todo o tabuleiro: casa com um número n com exatamente n casas vizinhas, então essas mesmas terão lâmpadas.
        '''
        for l in range(self.linhas):
            for c in range(self.colunas):
                pos = self.tabuleiro[l][c]
                if pos in "1234":
                    self.estrategia1_cada_casa(l,c,int(pos))

    #### ESTRATÉGIA 2 ####
                
    def IlluminaVert(self, l: int, c: int) -> None:
        '''Função suporte que ilumina todas as casas até encontrar um obstáculo na vertical

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        l1 = l + 1
        l2 = l - 1
        while l1 < self.getlinhas():
            if self.tabuleiro[l1][c] in "-.":
                self.tabuleiro[l1][c] = "o"
                l1 += 1
            elif self.tabuleiro[l1][c] == "o":
                l1 += 1
            else:
                break
        while l2 >= 0:
            if self.tabuleiro[l2][c] in "-.":
                self.tabuleiro[l2][c] = "o"
                l2 -= 1
            elif self.tabuleiro[l2][c] == "o":
                l2 -= 1
            else:
                break
    
    def IlluminaHoriz(self, l, c) -> None:
        '''Função suporte que ilumina todas as casas até encontrar um obstáculo na horizontal

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        c1 = c + 1
        c2 = c - 1
        while c1 < self.getcolunas():
            if self.tabuleiro[l][c1] in "-.":
                self.tabuleiro[l][c1] = "o"
                c1 += 1
            elif self.tabuleiro[l][c1] == "o":
                c1 += 1
            else:
                break
        while c2 >= 0:
            if self.tabuleiro[l][c2] in "-.":
                self.tabuleiro[l][c2] = "o"
                c2 -= 1
            elif self.tabuleiro[l][c2] == "o":
                c2 -= 1
            else:
                break
    
    def IlluminaTotal(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 2 que usa as funções suporte para iluminar todas as casas até encontrar um obstáculo (verticalmente + horizontalmente)

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        self.IlluminaVert(l, c)
        self.IlluminaHoriz(l, c)

    def estrategia2(self) -> None:
        '''Aplicação da Estratégia 2 por todo o tabuleiro: Marcar como iluminadas todas as casas na mesma linha e coluna de uma lâmpada (que não estejam bloqueadas).
        '''
        for lin in range(len(self.tabuleiro)):
            for col in range(len(self.tabuleiro[lin])):
                if self.tabuleiro[lin][col] == "@":
                    if lin < self.getlinhas() - 1 and col < self.getcolunas():
                        self.IlluminaVert(lin, col)
                    if col < self.getcolunas() - 1 and lin < self.getlinhas():
                        self.IlluminaHoriz(lin, col)
                else:
                    pass

    #### ESTRATÉGIA 3 ####

    def casas_diagonais_imp(self, l: int, c: int) -> list: 
        '''Função de suporte que verifica se as casas diagonais adjacentes à casa fornecida estão disponíveis.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        disp: list
            Lista de coordenadas correspondentes às casas diagonais adjacentes disponíveis
        '''
        disp = []
        
        if l == 0:
            if c == 0:
                poss = [(1,1)]
            elif c == (self.colunas -1):
                poss = [(1,-1)]
            else:
                poss = [(1,-1), (1,1)]
        elif l == (self.linhas -1):
            if c == (self.colunas-1):
                poss = [(-1,-1)]
            elif c == 0:
                poss = [(-1,1)]
            else: poss = [(-1,-1),(-1,1)]
        elif c == 0:
            poss = [(-1,1),(1,1)]
        elif c == (self.colunas-1):
            poss = [(-1,-1),(1,-1)]
        else:
            poss = [(-1,-1),(-1,1),(1,-1),(1,1)]
        
        for p in poss:
            if self.tabuleiro[l + p[0]][c + p[1]] == "-":
                disp.append([l + p[0],c + p[1]])
        return disp
    
    def estrategia3_casa0(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 3 para as casas com número 0: bloqueia todas as casas vizinhas disponíveis.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        #Aplicação da estratégia 3 para uma dada casa bloqueada no tabuleiro com o número 0.
        imp = self.casas_vizinhas_disp(l, c)
        if imp != []:
            for casa in imp:
                self.mc(casa[0],casa[1])

    def estrategia3_casa1(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 3 para as casas com número 1: caso essa casa já tenha uma lâmpada vizinha, bloqueia todas as outras; senão pode bloquear uma diagonal (caso tenha 2 vizinhas disponiveis que "partilhem" uma diagonal)

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        num_lampadas = self.num_lampadas_vizinhas(l, c)
        if num_lampadas == 1:
            imp = self.casas_vizinhas_disp(l, c)
            for casa in imp:
                self.mc(casa[0],casa[1])
        else:
            imp = self.casas_vizinhas_disp(l,c)
            if len(imp) == 2:
                casa_imp1, casa_imp2 = imp
                if casa_imp1[0] != casa_imp2[0] and casa_imp1[1] != casa_imp2[1]:
                    if self.tabuleiro[casa_imp1[0]][casa_imp2[1] == '-']:
                        self.mc(casa_imp1[0], casa_imp2[1])
                    else:
                        self.mc(casa_imp2[0], casa_imp1[0])


    def casas_vizinhas_bloq(self, l: int, c: int) -> list:
        '''Função de suporte que verifica se as casas vizinhas adjacentes à casa fornecida estão bloqueadas (impossíveis de colocar lâmpada, apesar de algumas deixarem passar luz).

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        bloq: list
            Lista de coordenadas correspondentes às casas vizinhas adjacentes bloqueadas
        '''
        bloq = []
        poss = [(l,0,-1,0),(l,self.linhas-1,1,0),(c,0,0,-1),(c,self.colunas-1,0,1)]
        for p in poss:
            if p[0] != p[1] and self.tabuleiro[l + p[2]][c + p[3]] in "xo.012345":
                bloq.append([l + p[2],c + p[3]])
        return bloq

    def estrategia3_casa2(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 3 para as casas com número 2: caso essa casa já tenha duas lâmpadas vizinhas, bloqueia todas as outras; senão pode bloquear diagonais (caso tenha vizinhas disponiveis que "partilhem" a diagonal)

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        num_lampadas = self.num_lampadas_vizinhas(l, c)
        if num_lampadas == 2:
            imp = self.casas_vizinhas_disp(l, c)
            for casa in imp:
                self.mc(casa[0],casa[1])
        else:
            imp = self.casas_vizinhas_disp(l,c)
            if len(imp) == 3:
                casas_bloq = self.casas_vizinhas_bloq(l,c)
                if casas_bloq != []:                    
                    casa_bloqueada = casas_bloq[0]
                    diag = self.casas_diagonais_imp(l,c)
                    for casa in diag:
                        if casa[0] == casa_bloqueada[0] or casa[1] == casa_bloqueada[1]:
                            pass
                        else:
                            self.mc(casa[0], casa[1])
                else:
                    diag = self.casas_diagonais_imp(l,c)
                    for casa in diag:
                        if casa[0] == -1 or casa[1] == -1 or casa[0] > self.linhas or casa[1] > self.colunas:
                            diag.remove(casa)
                        self.mc(casa[0], casa[1])


    def estrategia3_casa3(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 3 para as casas com número 3: caso essa casa já tenha 3 lâmpadas vizinhas, bloqueia a outra; senão pode bloquear as diagonais (uma vez que todas as vizinhas "partilham" uma diagonal)

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        num_lampadas = self.num_lampadas_vizinhas(l, c)
        if num_lampadas == 3:
            imp = self.casas_vizinhas_disp(l, c)
            for casa in imp:
                self.mc(casa[0],casa[1])
        else:
            imp = self.casas_diagonais_imp(l,c)
            for casa in imp:
                self.mc(casa[0],casa[1])
            
    def estrategia3_casa4(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 3 para as casas com número 4: bloqueia as diagonais (uma vez que todas as lâmpadas "partilham" uma diagonal)

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 
        '''
        imp = self.casas_diagonais_imp(l,c)
        for casa in imp:
                self.mc(casa[0],casa[1])

    def estrategia3(self) -> None: 
        '''Aplicação da Estratégia 3 por todo o tabuleiro: Bloquear todas as casas em que se verifique impossível que esta contenha uma lâmpada.
        '''
        for l in range(len(self.tabuleiro)):
            for c in range(len(self.tabuleiro[l])):
                if self.tabuleiro[l][c] == "0":
                    self.estrategia3_casa0(l,c)
                elif self.tabuleiro[l][c] == "1":
                    self.estrategia3_casa1(l,c)
                elif self.tabuleiro[l][c] == "2":
                    self.estrategia3_casa2(l,c)
                elif self.tabuleiro[l][c] == "3":
                    self.estrategia3_casa3(l,c)
                elif self.tabuleiro[l][c] == "4":
                    self.estrategia3_casa4(l,c)
                else:
                    pass


    #### ESTRATÉGIA 4 ####
        
    def _est4(self, l: int, c: int) -> None:
        '''Função suporte da Estratégia 4: retorna o valor necessário para adicionar aos índices e colocar a lâmpada correta.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        int
            1 ou -1
        '''
        diag = ([1, 1], [-1, -1], [1, -1], [-1, 1])
        for i in diag:
            if (l + i[0]) < self.getlinhas() and (c + i[1]) < self.getcolunas() and self.tabuleiro[l + i[0]][c + i[1]] == "1":
                return -i[0], -i[1]
        
    def estrategia4(self) -> None:
        '''Aplicação da Estratégia 4 por todo o tabuleiro: em casos de dois números numa diagonal (1 e 3) e haver certeza que as casas partilhadas não podem ter as duas iluminadas.
        '''
        for lin in range(len(self.tabuleiro)):
            for col in range(len(self.tabuleiro[lin])):
                if self.tabuleiro[lin][col] == "3":
                    indices = self._est4(lin, col)
                    if indices:
                        mov_lin = indices[0]
                        mov_col = indices[1]
                        new_line = lin + mov_lin
                        new_col = col + mov_col
                        if new_line < self.getlinhas() and self.tabuleiro[new_line][col] == "-":
                            self.jg(new_line, col)
                        if new_col < self.getcolunas() and self.tabuleiro[lin][new_col] == "-":
                            self.jg(lin, new_col)


    #### ESTRATÉGIA 5 ####

    def casas_vazias_coluna(self, l: int, c: int) -> list:
        '''Função de suporte da estratégia 5, 6 e 7 que devolve uma lista de casas vazias na mesma coluna da casa fornecida até, eventualmente, encontrar uma casa bloqueada.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        vazias: list
            Lista de casas vazias da mesma coluna da casa fornecida
        '''
        i1, up = l, True
        i2, down = l, True
        vazias = []
        while (i1 < self.linhas - 1 and up) or (i2 > 0 and down):
            # verificar casas vazias acima da casa fornecida
            if i1 < self.linhas - 1 and up:
                i1 += 1
                pos = self.tabuleiro[i1][c]
                if pos in "x01234": # casa bloqueada
                    up = False
                elif pos == "-":
                    vazias.append([i1,c])
            # verificar casas vazias abaixo da casa fornecida
            if i2 > 0 and down:
                i2 -= 1
                pos = self.tabuleiro[i2][c]
                if pos in "x01234": # casa bloqueada
                    down = False
                elif pos == "-":
                    vazias.append([i2,c])
        return vazias

    def casas_vazias_linha(self, l: int, c: int) -> list:
        '''Função de suporte da estratégia 5, 6 e 7 que devolve uma lista de casas vazias na mesma linha da casa fornecida até, eventualmente, encontrar uma casa bloqueada.

        Parameters
        ----------
        l : int
            Nº inteiro que corresponde à linha da casa que pretende
        c : int
            Nº inteiro que corresponde à coluna da casa que pretende 

        Returns
        -------
        vazias: list
            Lista de casas vazias da mesma linha da casa fornecida
        '''
        j1, right = c, True
        j2, left = c, True
        vazias = []
        while (j1 < self.colunas - 1 and right) or (j2 > 0 and left):
            # verificar casas vazias à direita da casa fornecida
            if j1 < self.colunas - 1 and right:
                j1 += 1
                pos = self.tabuleiro[l][j1]
                if pos in "x01234": # casa bloqueada
                    right = False
                elif pos == "-":
                    vazias.append([l,j1])
            # verificar casas vazias à esquerda da casa fornecida
            if j2 > 0 and left:
                j2 -= 1
                pos = self.tabuleiro[l][j2]
                if pos in "x01234": # casa bloqueada
                    left = False
                elif pos == "-":
                    vazias.append([l,j2])
        return vazias

        
    def estrategia5(self) -> None:
        '''Aplicação da Estratégia 5 por todo o tabuleiro: verifica se uma casa não iluminada só pode ser iluminada se uma dada casa tiver uma lâmpada (devido a outras restrições).
        '''
        for l in range(self.linhas):
            for c in range(self.colunas):
                total_vazias = self.casas_vazias_coluna(l,c) + self.casas_vazias_linha(l,c)
                pos = self.tabuleiro[l][c]
                # caso em que a casa atual é uma casa marcada e só há uma casa vazia à volta
                if pos == "." and len(total_vazias) == 1:
                    self.jg(total_vazias[0][0],total_vazias[0][1])
                # caso em que a casa atual está vazia e não há casas vazias à volta
                elif pos == "-" and len(total_vazias) == 0:
                    self.jg(l,c)


    #### ESTRATÉGIA 6 ####
    
    def estrategia6(self) -> None:
        '''Aplicação da Estratégia 6 por todo o tabuleiro: caso as estratégias 1-5 não resolvam totalmente o puzzle, aplica-se a tentativa-erro para casas com apenas duas opções disponíveis para ficar iluminada.
        '''
        for l in range(self.linhas):
            for c in range(self.colunas):
                total_vazias = self.casas_vazias_coluna(l,c) + self.casas_vazias_linha(l,c)
                pos = self.tabuleiro[l][c]
                new_tab = []
                for lin in self.tabuleiro:
                    linha = []
                    for col in lin:
                        linha.append(col)
                    new_tab.append(linha)
                if pos == "." and len(total_vazias) == 2:
                    for casa in total_vazias:
                        self.jg(casa[0],casa[1])
                        while self.resolve() == True:
                            self.add_historico()
                            #return True
                        if self.verify_lights() == False:
                            self.tabuleiro = new_tab
                            continue
                if self.verify_lights() == False:
                    self.tabuleiro = new_tab
                    continue

    #### ESTRATÉGIA 7 ####

    def estrategia7(self) -> None:
        '''Aplicação da Estratégia 7 por todo o tabuleiro: caso as estratégias 1-6 não resolvam totalmente o puzzle, aplica-se a tentativa-erro para casas com 3 ou mais opções disponíveis para ficar iluminada.
        '''
        for l in range(self.linhas):
            for c in range(self.colunas):
                total_vazias = self.casas_vazias_coluna(l,c) + self.casas_vazias_linha(l,c)
                pos = self.tabuleiro[l][c]
                new_tab = []
                for lin in self.tabuleiro:
                    linha = []
                    for col in lin:
                        linha.append(col)
                    new_tab.append(linha)
                if pos == "." and len(total_vazias) >= 3:
                    for casa in total_vazias:
                        self.jg(casa[0],casa[1])
                        if self.resolve() == True:
                            self.add_historico()
                            #return True
                        if self.verify_lights() == False:
                            self.tabuleiro = new_tab
                            continue

    #### RESOLVE ####

    def print_mat(self, m: list) -> None:
        '''Função auxiliar que devolve o tabuleiro de forma formatada para boa visualização.

        Parameters
        ----------
        m : list
            Puzzle em forma de matriz
        '''
        for lin in m:
            for col in lin:
                print(col, end=" ")
            print()

    def resolve(self) -> None:
        '''Função que implementa a resolução automática dos puzzles (percorre todas as estratégias definidas).
        '''
        while True:
            # criação de uma cópia do tabuleiro
            new_tab = []
            for lin in self.tabuleiro:
                linha = []
                for col in lin:
                    linha.append(col)
                new_tab.append(linha)
            # verificar se puzzle já está resolvido, para quebrar o ciclo
            if self.verify_lights() == True:
                break
            # aplicação de todas as estratégias de resolução
            self.estrategia1()
            self.estrategia2()
            self.estrategia3()
            self.estrategia4()
            self.estrategia5()
            # condição da estratégia 6 - quando o tabuleiro não sofre qualquer alteração após um ciclo
            if new_tab == self.tabuleiro:
                if self.verify_lights():
                    break
                self.estrategia6()
            if new_tab == self.tabuleiro:
                if self.verify_lights():
                    break
                self.estrategia7()
            if new_tab == self.tabuleiro:
                break

    def verify_lights(self) -> bool:
        '''Função auxiliar que verifica se existem ainda casas não iluminadas no tabuleiro.

        Returns
        -------
        bool
            Devolve True se todas as casas já estiverem iluminadas / False se ainda houver pelo menos uma casa não iluminada.
        '''
        for lin in range(len(self.tabuleiro)):
            for col in range(len(self.tabuleiro[lin])):
                if self.tabuleiro[lin][col] == "-" or self.tabuleiro[lin][col] == ".":
                    return False
        return True


    def check_numbers(self) -> bool:
        '''Função auxiliar que verifica se as casas com Nº n têm exatamente n lâmpadas adjacentes.

        Returns
        -------
        bool
            Devolve True se o número de lâmpadas adjacentes a uma casa com um Nº n é igual a n. False caso encontre alguma casa com nº lampadas diferente do seu Nº.
        '''
        for lin in range(len(self.tabuleiro)):
            for col in range(len(self.tabuleiro[lin])):
                if self.tabuleiro[lin][col].isnumeric():
                    counter = self.num_lampadas_vizinhas(lin, col)
                    if counter != int(self.tabuleiro[lin][col]): return False 
        return True

def print_mat(m):
    for lin in m:
        for col in lin:
            print(col, end=" ")
        print()


if __name__ == "__main__":
    t1 = IlluminatiEngine()
    t1.ler_tabuleiro_ficheiro("exemplos_puzzles/ex4.ill")
    #t1.resolve()
    t1.print_mat(t1.tabuleiro)
    t1.jg(1,2)
    print("--------------------")
    t1.print_mat(t1.tabuleiro)
    t1.jg(2,0)
    print("--------------------")
    t1.print_mat(t1.tabuleiro)
    t1.undo()
    print("--------------------")
    t1.print_mat(t1.tabuleiro)
    t1.undo()
    print("--------------------")
    t1.print_mat(t1.tabuleiro)
    t1.jg(2,0)
    print("--------------------")
    t1.print_mat(t1.tabuleiro)
    #t1.undo()
    #print("--------------------")
    #t1.print_mat(t1.tabuleiro)

    print("\nHISTÓRICO\n")
    while t1.historico.size() > 0:
        print_mat(t1.historico.pop())
        print("\n--------------------\n")