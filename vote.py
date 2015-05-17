from Tkinter import *
import Tkinter
import tkMessageBox
import vserver

r = vserver.connect()

def voteCallBack(vote):
	r.incr(vote)
	tkMessageBox.showinfo("Vote Machine", "You voted for " + vote)
	

top = Tkinter.Tk()

choices = vserver.get_choices()

for choice in choices:
	
	callback = lambda p=choice: voteCallBack(p)
		
	Tkinter.Button(
		top, 
		text = choice,
		width = 20,
		command = callback).pack(fill=BOTH, expand=1)
	
	
top.mainloop()
	
