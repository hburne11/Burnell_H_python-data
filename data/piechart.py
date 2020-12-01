import matplotlib.pyplot as plt

#generate a pie chart with our Olympic data

values = [386, 239]
colors = ['green', 'gold']
labels = ['men', 'women']
plt.pie(values, labels=labels, colors=colors)

plt.show()