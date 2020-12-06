import matplotlib.pyplot as plt

#generate a pie chart with our Olympic data

values = [214, 246]
colors = ['red', 'blue']
labels = ['Hockey: 214 Medals', 'Other Sports: 246'] 

plt.pie(values, labels=labels, colors=colors)

plt.title("Hockey Prevails!", pad="20")

plt.show()