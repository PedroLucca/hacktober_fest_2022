#Aluno: Pedro Lucca Monteiro Soares
import numpy as np

def LerInput():#Lê o arquivo com a sequencia e passa os dados para variáveis
    arquivo = 'input.fasta'

    f = open(arquivo, 'r') 
    lines = f.readlines() 

    fasta = []
    valores = []
    aux = ""

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
            aux += line.rstrip("\n")
            
    fasta.append(aux)
    return fasta,valores

def composicaoPareada(sequencia,k,d):#Função que gera a composition com os kdmers a partir das sequencia
    #print(sequencia)
    composicao = []
    k,d = int(k), int(d)
    tam = len(sequencia)
    for i in range(tam):
        elem1, elem2 = sequencia[i:i+k], sequencia[i+k+d:i+2*k+d]

        if (len(elem1) < k or len(elem2.rstrip("\t")) < k):
            break
        else:
            composicao.append((elem1, elem2))

    composicao.sort()#Coloca em ordem lexicográfica
    #print(composicao)
    composition = []
    nome = "k" + str(k) + "d" + str(d) + "mer.txt"
    arq = open(nome , "w")
    arq.write(">k=" + str(k) + "d=" + str(d) + "\n")
    for par in composicao:
        composition.append(par[0] + "|" + par[1])

    arq.write(str(composition))
    arq.close()
    print("\nComposição da sequencia gerada com sucesso!\nSe encontra no arquivo " + nome + "\n")


def main():#Função main responsável pela execução do programa
    sequencia, parametros = LerInput()
    composicaoPareada(sequencia[0], parametros[0], parametros[1])

if __name__ == "__main__":
    main()


