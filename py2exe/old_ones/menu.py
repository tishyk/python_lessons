# -*- coding: cp1251 -*-
from Tkinter import*
from tkFileDialog import*
from tkMessageBox import*
import ttk
def go():
        x,y=1,1
        c.move(krug,x,y)
        c.after(30,go)  #повторный вызов метода через 30 милесикунд

# ----------     tkMessageBox for 2.69 (tkinter.messagebox for 3.0) --------------

#askquestion('head','body') -> yes or no
#askyesno('head','body') -> True or False
showerror('head','body')#-> yes
#showinfo('head','body')#-> yes
#askokcancel('head','body')->True or False
#askyesno('head','body')->True or False
#askretrycancel('head','body')->True or False

# ----------     tkFileDialog for 2.69 (tkinter.filedialog for 3.0) --------------

#asksaveasfilename()  -> (path) "u'C:/Users/s.tischenko.SURC/Desktop/python/Menu/sdgdg.txt' "
#askopenfilename()-> (path) " u'C:/Users/s.tischenko.SURC/Desktop/python/Menu/menu.py' "
#(filetypes=[("Text files","*.txt"),("Exe files","*.exe")]) -show only with inserdet extesions
#askdirectory() -> (path)  " u'C:/Users/s.tischenko.SURC/Desktop/python/Menu' "
#askopenfile() -> " <open file u'C:/Users/s.tischenko.SURC/Desktop/python/Menu/menu.py', mode 'r' at 0x032B56A8> "
#(initialdir=initial_dir, filetypes=mask, mode='r')
#askopenfile().readlines() - object, not path!!!
#askopenfilenames() -> (path) " u'C://1.cmd C://CAUtil.exe C://icvupdo.log C://NCAsperaX.ocx' "
#asksaveasfile('a+') -> object " <open file u'C:/Users/s.tischenko.SURC/Desktop/python/Menu/1.txt', mode 'a' at 0x032B5A18> "



root=Tk()
#root.resizable(False,False)

def new_win():
    if askokcancel('New Window','Do you realy want open\n Data in New Window?'):
        win=Toplevel(root)

def close_root():
    if askyesno("Exit", "Do you want to quit?"):
        root.destroy()
    
def open_w():
    path=askopenfilename(filetypes=[("Text files","*.txt")])

def save_as():
    if askretrycancel('try again?','12345'):
        sa=asksaveasfilename()

def file_open(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\Temp"
        # the filetype mask (default is all files)
        mask = \
        [("Text and Python files","*.txt *.py *.pyw"), 
        ("HTML files","*.htm"), 
        ("All files","*.*")]        
        fin = askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
        text = fin.read()
        if text != None:
            self.text.delete(0.0, END)
            self.text.insert(END,text)

def file_save(self):
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0,END))
        fout.write(text2save)
        fout.close()




m=Menu(root)
root.config(menu=m)

fm=Menu(m)
safm=Menu(fm)

hm=Menu(m)

m.add_cascade(label='File',menu=fm)
m.add_cascade(label='Help',menu=hm)



fm.add_command(label='Open',command=open_w)
fm.add_command(label='New',command=new_win)
fm.add_command(label='Save',command=save_as)
fm.add_cascade(label="Save as..",menu=safm)
fm.add_command(label='Exit',command=close_root)

safm.add_command(label='as .html')
safm.add_command(label='as .xls')


hm.add_command(label='About')
hm.add_command(label='Help')
hm.add_command(label='How to do?')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print ('screen:',w,h)

img=PhotoImage(file = 'avatar.gif')
label = Label(image=img)
label.pack()
Button(root,image=img,text='Button').pack()
x = ttk.Separator(root).pack(fill='x',expand=1)
x = ttk.Sizegrip(root).pack(side=RIGHT)

root.mainloop()

