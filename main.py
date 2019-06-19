/*


*/


from tkinter import *
import tkinter.filedialog as filedialog

root = Tk("Text Editor")

// Save file
def saveas():
    global text

    t = text.get("1.0", "end-1c")

        //Saves file
    savelocation = filedialog.asksaveasfilename(
        initialdir="/", title="Select file", filetypes=(("All", "*.txt"), ("all files", "*.*")))

    //Ends and closes the file browser
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

//Button propertys for save
button = Button(root, text="Save", command=saveas)
button.grid()


def FontHelvetica():

    //Adds font Helvetica
    global text
    text.config(font="Helvetica")


def FontCourier():

    //adds font Courier
    global text
    text.config(font="Courier")

//Adds the menu button for the fonts
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
                          command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
                          command=FontHelvetica)

text = Text(root)
text.grid()


root.mainloop()
