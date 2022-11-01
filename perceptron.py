import numpy as np

class Perceptron:
    def __init__(self, n, variaveis, pesos_aux, taxa):
        self.n = n
        self.pesos = pesos_aux
        self.variaveis = variaveis
        self.parada = 0
        self.taxa = taxa

    def algoritmo(self):
        self.x_var = []
        self.y_var = []
        self.pesos = np.array(self.pesos)
        self.k = 0

        for i in range(0, self.n+2):
            for j in range(0, self.n+2):
                self.variaveis[i][j] = float(self.variaveis[i][j])

        passo = 0
        while True:
            self.x_var = self.variaveis[passo][:-1]
            self.y_var = self.variaveis[passo][-1]
            
            self.x_var = np.array(self.x_var)
            self.y_var = int(self.y_var)

            net = (self.x_var*self.pesos)
            net_aux = 0

            for i in net:
                net_aux += i

            if net_aux >= 0:
                net_aux = 1
            else:
                net_aux = 0
            
            erro = self.y_var - net_aux
            
            for i in range(0,self.n+1):
                self.pesos[i] = self.pesos[i] + self.taxa*erro*self.x_var[i]

        
            resultado = self.pesos[0]*self.x_var[0] + self.pesos[1]*self.x_var[1] + self.pesos[2]*self.x_var[2]

            if resultado >= 0:
                resultado = 1
            else:
                resultado = 0

            if resultado == self.y_var:
                self.parada = self.parada + 1
            else:
                self.parada = 0

            passo = passo + 1
            
            if passo >= 4:
                passo = 0
                self.k = self.k + 1
                print("** Iteração : ", self.k)
                print("Entradas: ", self.x_var)
                print("Erro: ", erro)
                print("Pesos: ", self.pesos)
                print("-------------\n")
            

            if self.parada == 4:
                break
            
        

    def predict(self, x, y):
        u = self.pesos[0]*1 + self.pesos[1]*x + self.pesos[2]*y
        if u >= 0:
            u = 1
        else:
            u = 0
        
        return u