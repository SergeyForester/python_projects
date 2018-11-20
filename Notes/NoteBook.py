__author__ ='Burik Sergey'
from tkinter import *
from tkinter import filedialog as fd

# file = open('file.txt','w') 

# def opener():
# 	f = open('file.txt') 	
# 	#text is a Text widget 
# 	text.insert(1.0, f.read()) 


# def saver():
# 	letter = text.get(1.0, END)
# 	f = open('file.txt', "w")
# 	f.write(letter)

def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()
 
def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()	
	

root = Tk()

button_sav = Button(text="Save file",command=extractText)
button_sav.pack()

button_open = Button(text="Open file", command=insertText)
button_open.pack()

text = Text(width=75, height=25)
text.pack()

frame = Frame()
frame.pack()
 
# b_delete = Button(frame, text="Удалить", command=deleteText)
# b_delete.pack(side=LEFT)
 
label = Label(text='Created by Burik Sergey')
label.pack()
 
root.mainloop()

