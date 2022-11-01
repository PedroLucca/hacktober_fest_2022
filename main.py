from perceptron import Perceptron
import argparse

variaveis = []
novo_array = []
entrada = open('entrada.txt', 'r')
for line in entrada:
    variaveis.append(line.rstrip("\n"))
for i in variaveis:
    novo_array.append(i.split(" "))
variaveis = novo_array

parser = argparse.ArgumentParser(description='Receber os pesos do algoritmo.')
parser.add_argument('peso1', metavar='peso1', type=float)
parser.add_argument('peso2', metavar='peso2', type=float)
parser.add_argument('peso3', metavar='peso3', type=float)

args = parser.parse_args()
pesos_aux = [args.peso1, args.peso2, args.peso3]

taxa = input("Digite a taxa de aprendizado: ")

pc = Perceptron(2, variaveis, pesos_aux, float(taxa))
pc.algoritmo()

print("--- Finalizado ---\n")
print("Testando valores: \n")
print("Resultado(0,0): ", pc.predict(0,0))
print("Resultado(0,1): ", pc.predict(0,1))
print("Resultado(1,0): ", pc.predict(1,0))
print("Resultado(1,1): ", pc.predict(1,1))
