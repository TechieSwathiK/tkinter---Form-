# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label 





# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

# Function to display a Message
def display():







	# Specify where to add the details inside the text box
	text_box.insert(END, greet)
	text_box.insert(END, message)
	text_box.insert(END, date.today())

# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically






# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()
