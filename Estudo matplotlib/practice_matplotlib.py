import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
tMed = [30, 31, 27, 26, 22, 18]

plt.ylabel('Temp / C', color = 'red')
plt.xlabel('Mês', color='blue')
plt.axis(ymin = 0, ymax = 40)
plt.title('Temperaturas médias mensais')
plt.plot(meses, tMed, label = 'Temperaturas', marker = 'o')
# plt.bar(meses,tMed, label = 'Temperaturas')
# plt.scatter(meses, tMed);
plt.legend()
plt.grid(True)
plt.show()