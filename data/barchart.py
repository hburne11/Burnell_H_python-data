import matplotlib.pyplot as plt

sports = ['Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Skiing']

medals = [27, 26, 30, 214, 8, 121, 153]

width = 0.35



x_labels = [0, 50, 100, 150, 200]
y_labels = ['Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Skiing']

plt.xlabel("Sports")
plt.ylabel("Medals")

plt.bar(sports, medals)
plt.show()

