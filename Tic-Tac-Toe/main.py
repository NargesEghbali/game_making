import tkinter as tk
from tkinter import messagebox
import pygame
pygame.mixer.init()
window=tk.Tk()

end_game_music=pygame.mixer.Sound('end_game.mp3')
#####################################################
window.geometry('380x380')
window.configure(bg='gold')
window.title('tic tac toe ')
window.iconbitmap('a.ico')

############################################

person=1
r=0
def click(b):
    global person,r
    if person==1 and b['text']==' ' :
        b.configure(text='x')
        winner()
        person=2
        r=r+1
    elif person==2 and b['text']==' ' :
        b.configure(text='o')
        winner()
        person=1
        r=r+1
    else:
       messagebox.showerror(message='this button has been selected before') 
def disabel_buttons():
    but1.config(state='disabled')
    but2.config(state='disabled')
    but3.config(state='disabled')
    but4.config(state='disabled')
    but5.config(state='disabled')
    but6.config(state='disabled')
    but7.config(state='disabled')
    but8.config(state='disabled')
    but9.config(state='disabled')


def winner():
    if but1['text']=='x' and but4['text']=='x' and but7['text']=='x':
        but1.config(bg='red')
        but4.config(bg='red')
        but7.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()
    elif but2['text']=='x' and but5['text']=='x' and but8['text']=='x':
        but2.config(bg='red')
        but5.config(bg='red')
        but8.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')   
        disabel_buttons()
    elif but3['text']=='x' and but6['text']=='x' and but9['text']=='x':
        but3.config(bg='red')
        but6.config(bg='red')
        but9.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()
    elif but1['text']=='x' and but2['text']=='x' and but3['text']=='x':
        but1.config(bg='red')
        but2.config(bg='red')
        but3.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()
    elif but4['text']=='x' and but5['text']=='x' and but6['text']=='x':
        but4.config(bg='red')
        but5.config(bg='red')
        but6.config(bg='red')
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()
    elif but7['text']=='x' and but8['text']=='x' and but9['text']=='x':
        but7.config(bg='red')
        but8.config(bg='red')
        but9.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()
    elif but1['text']=='x' and but5['text']=='x' and but9['text']=='x':
        but1.config(bg='red')
        but5.config(bg='red')
        but9.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()
    elif but3['text']=='x' and but5['text']=='x' and but7['text']=='x':
        but3.config(bg='red')
        but5.config(bg='red')
        but7.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='x is winner ')
        disabel_buttons()

    ######## for o #######################
    elif but1['text']=='o' and but4['text']=='o' and but7['text']=='o':
        but1.config(bg='red')
        but4.config(bg='red')
        but7.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but2['text']=='o' and but5['text']=='o' and but8['text']=='o':
        but2.config(bg='red')
        but5.config(bg='red')
        but8.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but3['text']=='o' and but6['text']=='o' and but9['text']=='o':
        but3.config(bg='red')
        but6.config(bg='red')
        but9.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but1['text']=='o' and but2['text']=='o' and but3['text']=='o':
        but1.config(bg='red')
        but2.config(bg='red')
        but3.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but4['text']=='o' and but5['text']=='o' and but6['text']=='o':
        but4.config(bg='red')
        but5.config(bg='red')
        but6.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but7['text']=='o' and but8['text']=='o' and but9['text']=='o':
        but7.config(bg='red')
        but8.config(bg='red')
        but9.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but1['text']=='o' and but5['text']=='o' and but9['text']=='o':
        but1.config(bg='red')
        but5.config(bg='red')
        but9.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()
    elif but3['text']=='o' and but5['text']=='o' and but7['text']=='o':
        but3.config(bg='red')
        but5.config(bg='red')
        but7.config(bg='red')
        end_game_music.play()
        messagebox.showinfo(message='o is winner ')
        disabel_buttons()



###############################################

but1=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but1))
but2=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but2))
but3=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but3))
but4=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but4))
but5=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but5))
but6=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but6))
but7=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but7))
but8=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but8))
but9=tk.Button(window,text=' ' ,font=('comic sans ms',54),command=lambda: click(but9))

but1.place(x=20,y=20,width=100,height=100)
but2.place(x=140,y=20,width=100,height=100)
but3.place(x=260,y=20,width=100,height=100)
but4.place(x=20,y=140,width=100,height=100)
but5.place(x=140,y=140,width=100,height=100)
but6.place(x=260,y=140,width=100,height=100)
but7.place(x=20,y=260,width=100,height=100)
but8.place(x=140,y=260,width=100,height=100)
but9.place(x=260,y=260,width=100,height=100)


















window.mainloop()