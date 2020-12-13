#TKINTER GUI File Open and Save as
#IL NOTEPAD

from tkinter import *
import tkinter.messagebox as tkmsg
from tkinter import filedialog
import base64

imgSrc = "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"
fh = open("ico.png", "wb")
fh.write(base64.b64decode(imgSrc))
fh.close()



currpath = "";

def autoAlert(msg):
    l2.configure(text=msg)
    
def new():
    text.delete(1.0,END)
    l1.configure(text="unsaved file")
    currpath=""
    autoAlert("New File Opened Successfully")

def openFile():
    global currpath
    if(currpath!=""):
        save()
    filename = filedialog.askopenfilename(defaultextension="*.txt",filetype=[("Text File","*.txt"),("Rich Text Format","*.rtf"),("Word","*.doc"),("Excel","*.xls")])
    if(not filename):
        autoAlert("Something went wrong")
    else:
        currpath = str(filename)
        l1.configure(text=currpath)
        file = open(filename,"r")
        text.delete(1.0,END)
        text.insert(1.0,file.read())
        file.close()
        autoAlert("File Opened Successfully")

def saveAs(p="all") :
    global currpath
    if(p=="word"):
        file = filedialog.asksaveasfile(defaultextension="*.doc",filetype=[("Word","*.doc")])
    elif(p=="excel"):
        file = filedialog.asksaveasfile(defaultextension="*.xls",filetype=[("Excel","*.xls")])
    else:
        file = filedialog.asksaveasfile(defaultextension="*.txt",filetype=[("Text File","*.txt"),("Rich Text Format","*.rtf"),("All Files","*.*")])

    if(not file):
        autoAlert("Something went wrong")
    else:
        currpath = str(file.name)
        filetext = str(text.get(1.0,END))
        file.write(filetext)
        file.close()
        autoAlert("File Saved Successfully")

def save():
    global currpath
    if(currpath==""):
        saveAs("all")
    else:
        file = open(currpath,"w")
        if(file):
            filetext = str(text.get(1.0,END))
            file.write(filetext)
            file.close()
            autoAlert("File Saved Successfully")
        else:
            autoAlert("Something went wrong")
    l1.configure(text=currpath)

def selectAll():
    text.tag_add('sel',1.0,END)

def cutText():
    root.clipboard_clear()
    root.clipboard_append(str(text.selection_get()))
    root.update()
    text.delete(SEL_FIRST,SEL_LAST)
    
def copyText():
    root.clipboard_clear()
    root.clipboard_append(str(text.selection_get()))
    root.update()

def pasteText():
    text.insert(text.index(INSERT),root.clipboard_get())

def about():
    tkmsg.showinfo("About Me",'''Created and Developed by PIYUSH GARG

IL CODER

''')

def shortcut(event):
    if(event.keycode==78):
        new()
    elif(event.keycode==83):
        save()   
    elif(event.keycode==81):
        root.quit()
    elif(event.keycode==79):
        openFile()

root = Tk()
root.geometry("400x400+500+100") #default size of window
root.minsize(500,500)   #minimum size of window
root.maxsize(500,550)   #maximum size of window
root.title("IL NOTEPAD") #sets title of the window
root.configure(background="lightgray")
p1 = PhotoImage(file="ico.png")
root.iconphoto(False,p1)

l1 = Label(root,bg="lightgray",text="unsaved file")
l1.pack()

menubar = Menu(root,tearoff=0)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New",accelerator="Ctrl+N",command=new)
filemenu.add_command(label="Open",accelerator="Ctrl+O",command=openFile)
filemenu.add_command(label="Save",accelerator="Ctrl+S",command=save)
filemenu.add_command(label="Save as",command=lambda: saveAs("all"))

exportmenu = Menu(filemenu,tearoff=0)
exportmenu.add_command(label="Word",command=lambda: saveAs("word"))
exportmenu.add_command(label="Excel",command=lambda: saveAs("excel"))
filemenu.add_cascade(label="Export",menu=exportmenu)

filemenu.add_separator()
filemenu.add_command(label="Exit",accelerator="Ctrl+Q",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=cutText)
editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=copyText)
editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=pasteText)
editmenu.add_command(label="Select All",accelerator="Ctrl+A",command=selectAll)
menubar.add_cascade(label="Edit",menu=editmenu)
root.bind_all("<Control-n>",shortcut)
root.bind_all("<Control-s>",shortcut)
root.bind_all("<Control-q>",shortcut)
root.bind_all("<Control-o>",shortcut)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

text = Text(root,height=500)
text.pack()
l2 = Label(root,bg="lightgray",width=200,anchor="w",text="New File Opened Successfully")
l2.place(x=0,y=480)

root.config(menu=menubar)
root.mainloop()
