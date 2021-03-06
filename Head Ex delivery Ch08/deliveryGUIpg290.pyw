from tkinter import *

def save_data():
<<<<<<< HEAD
        fileD = open("deliveries.txt")
=======
        fileD = open("deliveries.txt", "a")
>>>>>>> bb58f6c8d393eb254cc4e91ff496e89b82b5a455
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.set("")
        description.delete(0, END)
        address.delete("1.0", END)
    

def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

app = Tk()
app.title('Head-Ex Deliveries')

Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)

options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()
