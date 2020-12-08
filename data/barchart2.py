import matplotlib.pyplot as plt

gender = ['Men', 'Women']																																																																																																																																

medals = [281, 179]

width = 0.35



x_labels = [0, 50, 100, 150, 200]
y_labels = ['Men', 'Women']

plt.xlabel("Gender")
plt.ylabel("Medals")

plt.bar(gender, medals)
plt.show()

