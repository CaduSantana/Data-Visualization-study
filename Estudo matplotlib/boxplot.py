# Boxplot example
import matplotlib.pyplot as plt
import random

vector = []

for i in range(10):
    rand_num = random.randint(0,50)
    vector.append(rand_num)

plt.boxplot(vector)
plt.title("Boxplot")
plt.show()