import matplotlib.pyplot as plt

hfont = {'fontname':'Lato'}

# draw a simple line chart showing population growth

game = ['1', '2', '3', '4', '5', '6', '7', '8']

goals = [4, 2, 1, 5, 4, 3, 6, 3]
# plot our chart with the data above, and also format the line color and width
plt.plot(game, goals, color=(0/255, 100/255, 100/255), linewidth=6.0)
plt.ylabel("Goals")
plt.xlabel("Game")

plt.title("Goals per Game", pad="20"), 

#run the show method this lives inside the pyplot package
plt.show()