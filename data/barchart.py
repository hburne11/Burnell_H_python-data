import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

sports = ['Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Skiing']

medals = [27, 26, 30, 214, 8, 121, 153]

width = 0.35

ax.bar(sports, medals)

x_labels = [0, 50, 100, 150, 200]
y_labels = ['Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Skiing']

ax.set_ylabel("World Population by Billion")
ax.set_xlabel("Population Growth by Year")

ax.set_title("World Population Growth")

ax.show()

