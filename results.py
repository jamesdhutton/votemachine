#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import vserver

r = vserver.connect()

choices = vserver.get_choices()

ind = np.arange(len(choices))  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
rects = ax.bar(ind, [0] * len(choices), width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Votes')
ax.set_title('Vote Results')
ax.set_xticks(ind+width/2)
ax.set_xticklabels( choices )
ax.set_xlim(0, max(ind)+width)

def drawgraph():	
	for i in range(len(choices)):
		rects[i].set_height(int(r.get(choices[i])))
	ax.set_ylim((0, max(map( lambda r: r.get_height(), rects)) + 1))
			
cmd = "r"
while cmd == "r":
	drawgraph()
	plt.draw()
	fig.show()	
	cmd = raw_input('Enter r to refresh or any other key to quit: ')
	

