import vserver

r = vserver.connect()
choices = vserver.get_choices()

for choice in choices:
	r.set(choice, 0)