print("Executing the script for realz")

def button_clicked(widget, data=None):
	widget.set_label("Well, this was clicked!")

builder.get_object('button1').connect('clicked', button_clicked)