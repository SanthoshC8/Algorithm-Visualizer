import numpy as np
from matplotlib import animation as animation, pyplot as plt, cm

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

langs = ['C', 'C2', 'Java', 'Python', 'PHP']
students = [1,2,3,4,5]
ax.bar (langs,students)

plt.show()





"""
fig = plt.figure()

data = [1, 4, 3, 2, 6, 7, 3]
colors = ['red', 'yellow', 'blue', 'green', 'black']
bars = plt.bar(data, data, facecolor='green', alpha=0.75)

def animate(frame):
   global bars
   index = np.random.randint(1, 7)
   bars[frame].set_height(index)
   bars[frame].set_facecolor(colors[np.random.randint(0, len(colors))])

ani = animation.FuncAnimation(fig, animate, frames=len(data))
"""
