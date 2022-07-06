from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Trinity Healthcare DB System')
root.iconbitmap('C:/Users/admin/Desktop/GUI/game.ico')

my_img = ImageTk.PhotoImage(Image.open("tri.jpg"))
my_label = Label(image=my_img)
my_label.pack()


root.geometry("800x600")

my_menu = Menu(root)
root.config(menu=my_menu)

# click command
def our_command():
	my_label = Label(root, text="Clicked on a menu.").pack()


#Create a menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)

#Create an Options menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)


#define some variables
count = 0
size = 26
pos = 100

# Create a button
my_button = Button(root, 
	text="Patient Credentials", 
	font=("Helvetica", 15),
	fg="black")
my_button.pack(pady=10)

# Create a button
my_button = Button(root, 
	text="Billing Management", 
	font=("Helvetica", 15),
	fg="black")
my_button.pack(pady=10)

# Create a button
my_button = Button(root, 
	text="Insurance", 
	font=("Helvetica", 15),
	fg="black")
my_button.pack(pady=10)

#Create an exit button
button1_quit=Button(root, text="Exit Database", font=("Helvetica", 9),
command=root.quit)
button1_quit.pack()
button1_quit.pack(side=BOTTOM)



root.mainloop()



