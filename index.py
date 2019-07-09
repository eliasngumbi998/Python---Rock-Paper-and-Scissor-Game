from tkinter import *
import random

#================IMAGES================
blank img=PhotoImage(file="image/blank.png")
player_rock+PhotoImage(file="images/player_rock.png")
sm_player_rock=player_rock.subsample(3, 3)
player_paper_PhotoImage(file="image/player_paper.png")
sm_player_paper=player_paper.subsample(3, 3)
player_scissor=PhotoImage(file="images/player_scissor.png")
sm_player_scissor=player_scissor.subsample(3, 3)
com_paper=PhotoImage(file="image/com_rock.png")
com_paper=PhotoImage(file="image/com_paper.png")
com_scissor=PhotoImage(file="image/com_scissor.png")

#================LABLE WIDGET ===============
player_img= Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)
lbl_player = Label(root, text="PLAYER")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="#99ff99")
lbl_computer = Label(root, text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="99ff99")
lbl_status = Label(root, text="", font-'arial', 8))
lbl_status.config(bg="#99ff99")
player_img.grid(row=2,column=1,padx=30,pady=20)
comp_img.grid(row=2, column=3, pady=20)
lbl_status.grid(row=3, column=2)


#===============BUTTON WIDGET==============
rock=Button(root, image=sm_player_rock, command=Rock)
paper=Button(root, image=sm_player_paper, command=paper)
scissor=Button(root, image=sm_player_scissor, command=scissor)
btn_quit =Button(root, text="Quit", command=ExitApp)
rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2, pady=30)
scissor.grid(row=4, column=3, pady=30)
btn_quit.grid(row=5, column=2)


#============METHODS======================
def Rock();
    global player_choice
    player_choice =1
    player_img.configure(image=player_rock)
    Matchprocess()


def Paper();
    global player_choice
    player_choice =2
    player_img.configure(image=player_paper)
    Matchprocess()


def Scissor();
    global player_choice
    player_choice =3
    player_img.configure(image=player_scissor)
    Matchprocess()


def Matchprocess();
    com_choice= random.randint(1, 3)
    if com_choice==1:
       com_img.configure(image=com_rock)
       ComputerRock()
    elif  com_choice==2:
       com_img.configure(image=com_paper)
       ComputerPaper()
