# Growth of Brazil's Population
# Source: DataSus
import matplotlib.pyplot as plt

data = open("populacao_brasileira.csv").readlines()

x = [] # Population qtd array
y = [] # Year number array

for i in range(len(data)):
    if i != 0:
        linha = data[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
# print(x) # debugging

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color = "k", linestyle = "--")
plt.title("Growt of Brazil's Population from 1980 to 2016")
plt.xlabel("Year")
plt.ylabel("Population x 100,000,000")
plt.savefig("bra_population.pdf", dpi = 1200)
plt.show()