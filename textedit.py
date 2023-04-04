from tkinter import *
from tkinter import filedialog
from tkinter import font
root=Tk()
root.title("text editor")
root.geometry("1200x600")
def new_file():
    my_text.delete("1.0",END)
    root.title("new file")
    
def open_file():
    my_text.delete("1.0",END)
    text_file=filedialog.askopenfilename(initialdir="C:/",title="Open file",filetypes=(("Text Files","*.txt"),))
    name=text_file
    root.title("Opened file")
    text_file=open(text_file,'r')
    stuff=text_file.read()
    my_text.insert(END,stuff)
    text_file.close()
def save_as():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/",title="Save file",filetypes=(("Text Files","*.txt"),))
    if text_file:
        name=text_file
        root.title("saved file")
        text_file=open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()
my_frame=Frame(root)
my_frame.pack(pady=2)
#scrollbar
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)
my_text=Text(my_frame,width=100,height=25,font=("Helvatica",16),undo=True,yscrollcommand=text_scroll.set)
my_text.pack()
text_scroll.config(command=my_text.yview)
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open" ,command=open_file)
file_menu.add_command(label="NEW",command=new_file)
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="Exit",command=root.quit)
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")
edit_menu.add_separator()
edit_menu.add_command(label="undo")
root.mainloop()
