import matplotlib.pyplot as plt

#Dados
x1 = [1, 3, 5 ,7 ,9]
y1 = [2, 3, 7 ,1 ,0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

#Títulos

title = "Bar graph"
xAxis = "X Axis"
yAxis = "Y Axis"

#Legenda
plt.title(title)
plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.bar(x1, y1)
plt.bar(x2, y2)

plt.show()