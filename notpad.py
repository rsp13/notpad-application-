from tkinter import *
from tkinter import filedialog as fd
import webbrowser
from  tkinter import colorchooser
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
import os
page=Tk()

def new():
    '''This is Top level window code'''
    def open_wfile():
        filetype=(('text file','.txt'),('all file','*.*'))
        f=fd.askopenfile(filetypes=filetype)
        text1.insert(1.0,f.readlines())
    def save_wfile():
        f=fd.asksaveasfile(initialfile='untitled.txt')
        txt=text1.get(1.0,'end')
        f.write(txt)
        f.close()
    def chose_cut(e):
        global sel
        if e:
            sel=new_file.clipboard_get()
        else:
            if text1.selection_get():
                sel=text1.selection_get()
                text1.delete('sel.first','sel.last')
                new_file.clipboard_clear()
                new_file.clipboard_append(sel)
    def chose_copy(e):
        global sel
        if e:
            sel=new_file.clipboard_get()
        else:
            if text1.selection_get():
                sel=text1.selection_get()
                new_file.clipboard_get()
                new_file.clipboard_append(sel)
    def chose_paste(e):
        global sel
        if e:
            sel=new_file.clipboard_get()
        else:
            if sel:
                paste=text1.index(INSERT)
                text1.insert(paste,sel)
                new_file.clipboard_clear()
                new_file.clipboard_append(sel)
    def chose_delete(e):
        global sel
        if e:
            sel=new_file.clipboard_get()
        else:
            if text1.selection_get():
                sel=text1.selection_get()
                text1.delete('sel.first','sel.last')
                new_file.clipboard_clear()
                new_file.clipboard_append(sel)
    def chose_color():
        color_code1=colorchooser.askcolor(title='Chose color')
        text1.config(fg=color_code1[1])
    def chose_font():
        def conf_font(f):
            text1.config(font=font.Font(family=f))

        win_font = Toplevel()
        win_font.geometry('250x250')
        fonts = Listbox(win_font, bg='wheat', fg='black')
        for f in font.families():
            fonts.insert('end', f)
        fonts.pack()
        btn = Button(win_font, text='Apply', command=lambda: conf_font(fonts.get(fonts.curselection())))
        btn.place(x=90, y=180)
        win_font.mainloop()
    def chose_bold():
        global select
        select = text1.selection_get()
        bold_font = font.Font(text, text.cget('font'))
        bold_font.configure(weight='bold')
        text1.tag_configure('bold', font=bold_font)
        current = text1.tag_names('sel.first')
        if 'bold' in current:
            text1.tag_remove('bold', 'sel.first', 'sel.last')
        else:
            text1.tag_add('bold', 'sel.first', 'sel.last')
    def chose_underline():
        underline_font = font.Font(text1, text1.cget('font'))
        underline_font.configure(underline=1)
        text1.tag_configure('underline', font=underline_font)
        current = text1.tag_names('sel.first')
        if 'underline' in current:
            text1.tag_remove('underline', 'sel.first', 'sel.last')
        else:
            text.tag_add('underline', 'sel.first', 'sel.last')
    def chose_italic():
        italic_font = font.Font(text1, text1.cget('font'))
        italic_font.configure(slant='italic')
        text1.tag_configure('italic', font=italic_font)
        current = text1.tag_names('sel.first')
        if 'italic' in current:
            text1.tag_remove('italic', 'sel.first', 'sel.last')
        else:
            text1.tag_add('italic', 'sel.first', 'sel.last')
    def chose_help():
        webbrowser.open('https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA')
    # feedback function
    def feedback():
        w = Toplevel()

        def ok():
            messagebox.showinfo('Submit', f'Your feedback is submit')

        w.geometry('400x400')
        w.title('Feddback Window')
        my_text = Text(w, bg='white', height=20, width=50, background='grey', foreground='black')
        my_text.pack()
        btn = Button(w, text='Submit', command=ok, relief=GROOVE, justify='center', bg='wheat', fg='black', bd=5,
                     height=2, width=10)
        btn.pack()
        w.mainloop()
    new_file=Toplevel()
    new_file.title('New File')
    new_file.geometry('500x500')
    #creating menubar
    new_menu=Menu(new_file)
    #For new window file menu
    mw1=Menu(new_menu,tearoff=0)
    mw1.add_command(label='New')
    mw1.add_command(label='New window')
    mw1.add_command(label='Open',command=open_wfile)
    mw1.add_command(label='SaveAs',command=save_wfile)
    mw1.add_separator()
    mw1.add_command(label='Exit',command=new_file.quit)
    # end of file menu
    #To for new window edit menu
    mw2=Menu(new_menu,tearoff=0)
    mw2.add_command(label='Undo')
    mw2.add_command(label='Redo')
    mw2.add_command(label='Cut',command=lambda :chose_cut(False))
    mw2.add_command(label='Copy',command=lambda :chose_copy(False))
    mw2.add_command(label='Paste',command=lambda :chose_paste(False))
    mw2.add_separator()
    mw2.add_command(label='Delete',command=chose_delete)
    #End of edit menu
    #To for new window custmize menu
    mw3=Menu(new_menu,tearoff=0)
    mw3.add_command(label='Font',command=chose_font)
    mw3.add_command(label='Color',command=chose_color)
    mw3.add_command(label='B',command=chose_bold)
    mw3.add_command(label='I',command=chose_italic)
    mw3.add_command(label='U',command=chose_underline)
    #End of custmize menu
    #To for new window help menu
    mw4=Menu(new_menu,tearoff=0)
    mw4.add_command(label='View Help',command=chose_help)
    mw4.add_command(label='Send Feedback')
    mw4.add_command(label='About Notepad')
    new_file.config(menu=new_menu)
    new_menu.add_cascade(label='File',menu=mw1)
    new_menu.add_cascade(label='Edit',menu=mw2)
    new_menu.add_cascade(label='Customize',menu=mw3)
    new_menu.add_cascade(label='Help',menu=mw4)
    #End of help menu
    #new window text widget
    text1=Text(new_file,height=500,width=1000,selectbackground='skyblue',selectforeground='black',undo=True)
    text1.pack()
    text1.focus()
    new_menu.bind('<Control-Key-x>',chose_cut)
    new_menu.bind('<Control-Key-c>',chose_copy)
    new_menu.bind('<Control-Key-v>',chose_paste)
    new_menu.mainloop()

'''This for main window code'''
#select new file
def new_file():
    text.delete('1.0',END)
    page.title('Notepad')

#open file function
def open_file():
    text.delete('1.0',END)
    filetype=(('text files','.txt'),('All files','.*'),('Python files','.*py'))
    f=fd.askopenfile(filetypes=filetype)
    text.insert(1.0,f.readlines())

#save file function
def save_file():
    f=fd.asksaveasfile(defaultextension='.txt',initialfile="untitled.txt",filetypes=[('Text files','.txt'),('All files','.*')])
    txt=text.get(1.0,'end')
    f.write(txt)
    f.close()

#cut text function
def cut_text(e):
    global select
    if e:
        select=page.clipboard_get()
    else:
        select = text.selection_get()
        if select:
            text.delete('sel.first','sel.last')
            page.clipboard_clear()
            page.clipboard_append(select)

#copy text function
def copy_text(e):
    global select
    if e:
        select=page.clipboard_get()
    else:
        select = text.selection_get()
        if select:
            select=text.selection_get()
            page.clipboard_clear()
            page.clipboard_append(select)

#paste text function
def paste_text(e):
    global select
    if e:
        select=page.clipboard_get()
    else:
        if select:
            paste=text.index(INSERT)
            text.insert(paste,select)
            page.clipboard_clear()
            page.clipboard_append(select)

#undo function
def edit_undo():
    text.edit_undo()

#redo function
def edit_redo():
    text.edit_redo()

#delete funtion
def delete_text(e):
    global select
    if e:
        select=page.clipboard_get()
    else:
        if select:
            select=text.selection_get()
            text.delete('sel.first','sel.last')
            page.clipboard_clear()
            page.clipboard_append(select)

#font selection function
def select_font():
    def conf_font(f):
        text.config(font=font.Font(family=f))
    win_font=Toplevel()
    win_font.geometry('250x250')
    fonts = Listbox(win_font,bg='wheat',fg='black')
    for f in font.families():
        fonts.insert('end', f)
    fonts.pack()
    btn=Button(win_font,text='Apply',command=lambda :conf_font(fonts.get(fonts.curselection())))
    btn.place(x=90,y=180)
    win_font.mainloop()

#color selection function
def color():
    color_code=colorchooser.askcolor(title='Chose color')
    text.config(fg=color_code[1]) #it takes the tuple

#bold unbold function
def text_custmize():
    global select
    select=text.selection_get()
    bold_font = font.Font(text, text.get('font'))
    bold_font.configure(weight='bold')
    text.tag_configure('bold', font=bold_font)
    current = text.tag_names('sel.first')
    if 'bold' in current:
        text.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        text.tag_add('bold', 'sel.first', 'sel.last')

#underline funtion
def text_underline():
    underline_font = font.Font(text, text.cget('font'))
    underline_font.configure(underline=1)
    text.tag_configure('underline', font=underline_font)
    current = text.tag_names('sel.first')
    if 'underline' in current:
        text.tag_remove('underline', 'sel.first', 'sel.last')
    else:
        text.tag_add('underline', 'sel.first', 'sel.last')

#italic font function
def text_italic():
    italic_font = font.Font(text, text.cget('font'))
    italic_font.configure(slant='italic')
    text.tag_configure('italic', font=italic_font)
    current = text.tag_names('sel.first')
    if 'italic' in current:
        text.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        text.tag_add('italic', 'sel.first', 'sel.last')

#help function
def help_web():
    webbrowser.open('https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA')

#feedback function
def feedback():
    w=Toplevel()
    def ok():
        messagebox.showinfo('Submit',f'Your feedback is submit')
    w.geometry('400x400')
    w.title('Feddback Window')
    my_text=Text(w,bg='white',height=20,width=50,background='grey',foreground='black')
    my_text.pack()
    btn=Button(w,text='Submit',command=ok,relief=GROOVE,justify='center',bg='wheat',fg='black',bd=5,height=2,width=10)
    btn.pack()
    w.mainloop()

#about notepad function
def about_notepad():
    admin='Rohit Parulekar'
    messagebox.showinfo('About notepad',f'This notepad created by:-Mr.{admin}')

page.geometry('500x500')
page.title('Notepad')
file_menu=Menu(page)
m1=Menu(file_menu,tearoff=0)
file_menu.add_cascade(label='File',menu=m1)
#To open for file
m1.add_command(label='New',command=new_file)
m1.add_command(label='New Window',command=new)
m1.add_command(label='Open',command=open_file)
m1.add_command(label='SaveAs',command=save_file)
m1.add_separator()
m1.add_command(label='Exit',command=page.quit)
#To open for edit menu
m2=Menu(file_menu,tearoff=0)
file_menu.add_cascade(label='Edit',menu=m2)
m2.add_command(label='Cut',command=lambda :cut_text(False),accelerator="(Ctrl+x)")
m2.add_command(label='Copy',command=lambda :copy_text(False),accelerator="(Ctrl+c)")
m2.add_command(label='Paste',command=lambda :paste_text(False),accelerator="(Ctrl+v)")
m2.add_separator()
m2.add_command(label='Undo',command=edit_undo,accelerator='(Ctrl+z)')
m2.add_command(label='Redo',command=edit_redo,accelerator='(Ctrl+y)')
m2.add_separator()
m2.add_command(label='Delete',command=lambda :delete_text(False),accelerator='(Ctrl+d)')
#to open for customize menu
m3=Menu(file_menu,tearoff=0)
file_menu.add_cascade(label='Customize',menu=m3)
m3.add_command(label='Font',command=lambda :select_font())
m3.add_command(label='Color',command=color)
m3.add_command(label='B',command=text_custmize)
m3.add_command(label='U',command=text_underline)
m3.add_command(label='I',command=text_italic)
#To open for help menu
m4=Menu(file_menu,tearoff=0)
file_menu.add_cascade(label='Help',menu=m4)
m4.add_command(label='View Help',command=help_web)
m4.add_command(label='Send Feedback',command=feedback)
m4.add_command(label='About Notpad',command=about_notepad)
#config filemenu
page.config(menu=file_menu)
#Scroollbar upword and down
scrollbar=Scrollbar(page)
scrollbar.pack(side=RIGHT,fill=Y)
#Scorolbar fro horizontal
scrollbar1=Scrollbar(page,orient='horizontal')
scrollbar1.pack(side=BOTTOM,fill=X)
#To TextArea
text=Text(page,undo=True,yscrollcommand=scrollbar.set,wrap='none',xscrollcommand=scrollbar1.set,bg='white',selectbackground='skyblue',selectforeground='black')
text.pack(expand=True,fill=BOTH)
text.focus()
#scrollbar config to textview
scrollbar.config(command=text.yview)
scrollbar1.config(command=text.xview)

#edit_bind event
page.bind('<Control-Key-x>',cut_text)
page.bind('<Control-Key-c>',copy_text)
page.bind('<Control-Key-v>',paste_text)
page.mainloop()