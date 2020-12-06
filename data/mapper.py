import matplotlib.pyplot as plt

hfont = {'fontname':'Lato'}

# draw a simple line chart showing population growth

sports = ['Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Skiing']

medals = [27, 26, 30, 214, 8, 121, 153]
# plot our chart with the data above, and also format the line color and width
plt.plot(sports, medals, color=(0/255, 100/255, 100/255), linewidth=6.0)
plt.ylabel("World Population by Billion")
plt.xlabel("Population Growth by Year")

plt.title("World Population Growth", pad="20"), 

#run the show method this lives inside the pyplot package
plt.show()