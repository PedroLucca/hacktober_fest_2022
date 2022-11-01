#Aluno: Pedro Lucca Monteiro Soares
from kdMer import LerInput
from collections import defaultdict

class Remontagem():
    def __init__(self, kdmers, k , d):#Criação das variaveis iniciais
        self.kdmers = kdmers
        self.k = int(k)
        self.d = int(d)
        self.fazer_grafo()

    def ha_caminho(self):#Verifica se há caminho Euleriano no grafo
        return self.existeCaminhoEuleriano

    def get_circuito(self):#Retorna circuito
        return self.circuito

    def get_sequencia(self):#Retorna a sequencia
        return self.sequencia

    def fazer_grafo(self):#Constroi o grafo inicial
        self.grafo = []
        self.d_arestas = {}
        self.d_lista_adjacentes = defaultdict(list)
        
        for tupla in self.kdmers:
            vertice_origem = tupla[0][0:self.k-1] + tupla[1][0:self.k-1]
            aresta = tupla[0] + tupla[1]
            vertice_destino = tupla[0][1:] + tupla[1][1:]

            self.grafo.append((vertice_origem, aresta, vertice_destino))
            self.d_lista_adjacentes[vertice_origem].append(vertice_destino)
            self.d_arestas[vertice_origem + vertice_destino] = aresta
            

        self.fazer_lista_adj()
        self.fazer_caminhos_e()

    def get_grafo(self):#Retorna o grafo feito
        return self.grafo

    def fazer_lista_adj(self):#Faz a lista de adjacencias do grafo
        lista_adj = ""

        for vertice_chave in self.d_lista_adjacentes:
            lista_adj += vertice_chave + " -> "
            lista_vertices = self.d_lista_adjacentes[vertice_chave]

            for vertice in lista_vertices:
                lista_adj += vertice + " -> "
            lista_adj += "\n"

    
    def get_lista_adj(self):#Retorna a lista de adjacentes
        return self.d_lista_adjacentes
    
    def fazer_caminhos_e(self):#Gera o caminho euleriano do grafo
        self.existeCaminhoEuleriano = False

        self.graus_entrada, self.graus_saida = {}, {}
        dict_lista_adj = self.get_lista_adj()

        for vertice_chave in dict_lista_adj:
            self.graus_saida[vertice_chave], self.graus_entrada[vertice_chave] = 0, 0
            lista_vertices = dict_lista_adj[vertice_chave]

            for vertice in lista_vertices:
                self.graus_saida[vertice], self.graus_entrada[vertice] = 0, 0
        
        for vertice_chave in dict_lista_adj:
            lista_vizinhos = dict_lista_adj[vertice_chave]
            self.graus_saida[vertice_chave] = len(lista_vizinhos)

            for vizinho in lista_vizinhos:
                self.graus_entrada[vizinho] += 1

        todos_tem_mesmo_grau = True
        qte_vertices_grau_diferente = 0
        vertices_grau_diferente = []

        for vertice in self.graus_entrada:

            if (self.graus_entrada[vertice] != self.graus_saida[vertice]):
                todos_tem_mesmo_grau = False

                if (qte_vertices_grau_diferente > 2):
                    break
                else:
                    vertices_grau_diferente.append(vertice)
                    qte_vertices_grau_diferente += 1
        
        vertice_inicio = ""

        if (todos_tem_mesmo_grau == True):
            self.existeCaminhoEuleriano = True
            if (len(self.graus_entrada) > 0):
                vertice_inicio = self.graus_entrada.keys()[0]
            else:
                vertice_inicio = self.graus_saida.keys()[0]
        else:
            if (qte_vertices_grau_diferente == 2):
                vertice1, vertice2 = vertices_grau_diferente[0], vertices_grau_diferente[1]
                if ((self.graus_saida[vertice1] + self.graus_entrada[vertice1]) == 1) and ((self.graus_entrada[vertice2] + self.graus_saida[vertice2]) == 1):
                    self.existeCaminhoEuleriano = True
                    if (self.graus_saida[vertice1] > self.graus_entrada[vertice1]):
                        vertice_inicio = vertice1[:]
                    else:
                        vertice_inicio = vertice2[:]
        
        if (self.existeCaminhoEuleriano == True):
            pilha, self.circuito = [], []
            vertice_corrente = vertice_inicio

            while(True):
                if(self.graus_saida[vertice_corrente] == 0 and len(pilha) == 0):
                    break
                else:
                    if(self.graus_saida[vertice_corrente] == 0):
                        self.circuito.append(vertice_corrente)
                        vertice_corrente = pilha.pop()
                    else:
                        pilha.append(vertice_corrente)
                        vizinho = self.d_lista_adjacentes[vertice_corrente].pop()
                        self.graus_saida[vertice_corrente] -= 1
                        self.graus_entrada[vizinho] -= 1
                        vertice_corrente = vizinho[:]
            
            self.circuito.append(vertice_inicio)
            self.circuito = self.circuito[::-1]
            caminho_euleriano = vertice_inicio[:]
            tam_caminho = len(self.circuito)

            for i in range(1, tam_caminho - 1):
                caminho_euleriano += " -> " + self.circuito[i]
            caminho_euleriano += " -> " + self.circuito[tam_caminho - 1]

            self.remontar()
    
    def remontar(self):#Faz a remontagem da sequencia a partir do caminho gerado
        arestas, tam_circuito = [], len(self.circuito) 

        for i in range(tam_circuito):
            if(i < tam_circuito - 1):
                chave = self.circuito[i] + self.circuito[i + 1]
                arestas.append(self.d_arestas[chave])
        
        len_arestas = len(arestas)
        self.sequencia = arestas[0][:self.k]
        sufixos = ''

        for i in range(1, len_arestas):
            if i == (len_arestas - self.d - 1):
                sufixos += arestas[len_arestas - self.d - 1][self.k:self.k + self.d]
            if self.k < self.d:
                if i > (len_arestas - self.d - 1):
                    sufixos += arestas[i][-1]
            self.sequencia += arestas[i][:self.k][-1]

        self.sequencia += sufixos

        if self.k >= self.d:
            self.sequencia += arestas[-1][self.k:]

        arq = open('Remontagem.fasta', 'w')
        arq.write(">k=" + str(self.k) + "d=" + str(self.d) + "\n")
        arq.write(self.sequencia)
        arq.close()


def LerKdmer(arquivo):#Lê o arquivo com os kdmers e passa os dados para variáveis
    f = open(arquivo, 'r') 
    lines = f.readlines() 

    kdmers = []
    valores = []

    for line in lines:
        if line.find('>') == 0: 
            line = line.rstrip("\n")
            line = line.split("=")
            k = line[1]
            k = k.rstrip("d")
            d = line[2]
            valores.append(k)
            valores.append(d)
        else:
            lista = line.split(",")

            for par in lista:
                par = par.replace("[", "")
                par = par.replace("]", "")
                par = par.replace("'", "")
                par = par.replace(" ", "")
                aux = par.split("|")
                kdmers.append(aux)
            
    return kdmers,valores


def main():#Função main responsável pela execução do programa
    sequencia, parametros = LerInput()
    kdmer, valores = LerKdmer("k" + parametros[0] + "d" + parametros[1] +"mer.txt")
    
    k, d = valores[0], valores[1]

    grafo = Remontagem(kdmer, k, d)

    if (grafo.ha_caminho()):
        if (grafo.get_sequencia() == sequencia[0]):
            print('\nSequência remontada com sucesso!\nVerifique o arquivo Remontagem.fasta\n')
        else:
            print('Erro: foi gerada uma sequência diferente da original.')
    else:
        print('Não há caminho Euleriano!')

if __name__ == "__main__":
    main()