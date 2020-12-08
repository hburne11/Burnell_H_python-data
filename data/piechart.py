import matplotlib.pyplot as plt

#generate a pie chart with our Olympic data

values = [214, 27, 26, 30, 8, 121, 153]
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange']
labels = ['Hockey: 214 Medals', 'Biathlon: 27 Medals', 'Bobsleigh: 26 Medals', 'Curling: 30 Medals', 'Luge: 8 Medals', 'Skating: 121 Medals', 'Skiing: 153 Medals'] 

plt.pie(values, labels=labels, colors=colors)

plt.title("Hockey Prevails!", pad="20")

plt.show()