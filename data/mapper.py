import matplotlib.pyplot as plt

hfont = {'fontname':'Lato'}

# draw a simple line chart showing population growth

years = ['1994', '1998']

medals = [163, 294]
# plot our chart with the data above, and also format the line color and width
plt.plot(years, medals, color=(0/255, 100/255, 100/255), linewidth=6.0)
plt.ylabel("Medals")
plt.xlabel("Years")

plt.title("Medals won over the years", pad="20"), 

#run the show method this lives inside the pyplot package
plt.show()