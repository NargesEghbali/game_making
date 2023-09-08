import tkinter as tk 
from PIL import Image,ImageTk
import numpy as np
import pygame
pygame.mixer.init()

winner_music=pygame.mixer.Sound('mixkit-medieval-show-fanfare-announcement-226.wav')


#################################################################################

   

def ston_show():
    global my_score,pc_score
    ston_image=Image.open('ston.png')
    ston_image_resized=ston_image.resize((100,100))
    ston_image_tk=ImageTk.PhotoImage(ston_image_resized)

    my_choice_label.config(image=ston_image_tk)
    my_choice_label.image_names=ston_image_tk

   
    #######
    images_adress=['ston.png','scisorse.jpg','paper.jpg']
    random_image_address=np.random.choice(images_adress)
    random_image=Image.open(random_image_address)
    random_image_resized=random_image.resize((100,100))
    random_image_tk=ImageTk.PhotoImage(random_image_resized)

    pc_chice_label.config(image=random_image_tk)
    pc_chice_label.image_names=random_image_tk

    #######
    dic_pc_choices={'ston.png':'ston','scisorse.jpg':'scisorse','paper.jpg':'paper'}
    pc_choice=dic_pc_choices[ random_image_address]
    if pc_choice=='paper':
        pc_score=pc_score+1
    elif pc_choice=='stone':
        pass
    elif pc_choice=='scisorse':
        my_score=my_score+1
    ############

    my_score_label.config(text='my score:'+str(my_score))
    pc_score_label.config(text='pc score:'+str(pc_score))
    
    if my_score==10:
        winner_music.play()
    elif pc_score==10:
        winner_music.play()    

####################################################################
def paper_show():
    global my_score,pc_score
    paper_image=Image.open('paper.jpg')
    paper_image_resized=paper_image.resize((100,100))
    paper_image_tk=ImageTk.PhotoImage(paper_image_resized)
    
    my_choice_label.config(image=paper_image_tk)
    my_choice_label.image_names=paper_image_tk


    #######
    images_adress=['ston.png','scisorse.jpg','paper.jpg']
    random_image_address=np.random.choice(images_adress)
    random_image=Image.open(random_image_address)
    random_image_resized=random_image.resize((100,100))
    random_image_tk=ImageTk.PhotoImage(random_image_resized)
    
    pc_chice_label.config(image=random_image_tk)
    pc_chice_label.image_names=random_image_tk
    #######
    dic_pc_choices={'ston.png':'ston','scisorse.jpg':'scisorse','paper.jpg':'paper'}
    pc_choice=dic_pc_choices[ random_image_address]
    if pc_choice=='paper':
        pass
    elif pc_choice=='stone':
        my_score=my_score+1
    elif pc_choice=='scisorse':
        pc_score=pc_score+1
    ############
    my_score_label.config(text='my score:'+str(my_score))
    pc_score_label.config(text='pc score:'+str(pc_score))
    if my_score==10:
        winner_music.play()
    elif pc_score==10:
        winner_music.play() 
#######################################################################
def scisors_show():
    global my_score,pc_score
    scisors_image=Image.open('scisorse.jpg')
    scisors_image_resized=scisors_image.resize((100,100))
    scisors_image_tk=ImageTk.PhotoImage(scisors_image_resized)

    my_choice_label.config(image=scisors_image_tk)
    my_choice_label.image_names=scisors_image_tk

   
    #######
    images_adress=['ston.png','scisorse.jpg','paper.jpg']
    random_image_address=np.random.choice(images_adress)
    random_image=Image.open(random_image_address)
    random_image_resized=random_image.resize((100,100))
    random_image_tk=ImageTk.PhotoImage(random_image_resized)

    pc_chice_label.config(image=random_image_tk)
    pc_chice_label.image_names=random_image_tk
    #######
    dic_pc_choices={'ston.png':'ston','scisorse.jpg':'scisorse','paper.jpg':'paper'}
    pc_choice=dic_pc_choices[ random_image_address]
    if pc_choice=='paper':
        my_score=my_score+1
    elif pc_choice=='stone':
        pc_score=pc_score+1
    elif pc_choice=='scisorse':
        pass
    ############
    my_score_label.config(text='my score:'+str(my_score))
    pc_score_label.config(text='pc score:'+str(pc_score))

    if my_score==10:
        winner_label=tk.Label(window,text='You won')
        winner_music.play()
    elif pc_score==10:
        winner_music.play() 

#########################################################################
global my_score,pc_score
my_score=0
pc_score=0

window=tk.Tk()
window.geometry('800x500')
window.configure(bg='medium slate blue')
window.title('rock paper scissors')
window.iconbitmap('rock_39413.ico')

ston_image=Image.open('ston.png')
ston_image_resized=ston_image.resize((100,100))
ston_image_tk=ImageTk.PhotoImage(ston_image_resized)

ston_but=tk.Button(window,image=ston_image_tk,width=100,height=100,command=ston_show)
ston_but.place(x=650,y=100)



paper_image=Image.open('paper.jpg')
paper_image_resized=paper_image.resize((100,100))
paper_image_tk=ImageTk.PhotoImage(paper_image_resized)

paper_but=tk.Button(window,image=paper_image_tk,width=100,height=100,command=paper_show)
paper_but.place(x=650,y=220)


scisors_image=Image.open('scisorse.jpg')
scisors_image_resized=scisors_image.resize((100,100))
scisors_image_tk=ImageTk.PhotoImage(scisors_image_resized)

scisors_but=tk.Button(window,image=scisors_image_tk,width=100,height=100,command=scisors_show)
scisors_but.place(x=650,y=340)




############for pc choose
ston_label=tk.Label(window,image=ston_image_tk,width=100,height=100)
ston_label.place(x=50,y=100)


paper_label=tk.Label(window,image=paper_image_tk,width=100,height=100)
paper_label.place(x=50,y=220)


scisors_label=tk.Label(window,image=scisors_image_tk,width=100,height=100)
scisors_label.place(x=50,y=340)



my_score_label=tk.Label(window,bg='medium slate blue',font=('comic sans ms',20),fg='white',text='my score:'+str(my_score))
my_score_label.place(x=620,y=20)


pc_score_label=tk.Label(window,bg='medium slate blue',font=('comic sans ms',20),fg='white',text='pc score:'+str(pc_score))
pc_score_label.place(x=50,y=20)


my_choice_label=tk.Label(window)
my_choice_label.place(x=500,y=220,width=100,height=100)
   
pc_chice_label=tk.Label(window)
pc_chice_label.place(x=200,y=220,width=100,height=100)
window.mainloop()
