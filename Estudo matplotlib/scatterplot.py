import matplotlib.pyplot as plt

#Dados
x = [1, 3, 5 ,7 ,9]
y = [2, 3, 7 ,1 ,0]
# z = [200, 25, 400, 3300, 1000]

title = "Scatterplot - gráfico de dispersão"
xAxis = "X Axis"
yAxis = "Y Axis"

#Legendas
plt.title(title)
plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.scatter(x, y, label = "Pontos", color = "g", s = 100) #s = z
plt.plot(x, y, linestyle = "-.", color = "#990000")
plt.legend()

plt.savefig("output.pdf", dpi = 1200) # Precisa ser executada antes de show(), pois este esvazeia a memória de execução 
plt.show()