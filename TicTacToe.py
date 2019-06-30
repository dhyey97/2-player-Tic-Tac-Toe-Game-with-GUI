from tkinter import *
from tkinter import ttk
from tkinter import messagebox

c = True
player = 1
root =Tk()
button1 = Button()
button2 = Button()
button3 = Button()
button4 = Button()
button5 = Button()
button6 = Button()
button7 = Button()
button8 = Button()
button9 = Button()

def closeClick():
    quit()

def clearGrid():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global player
    button1["text"] = ' '
    button2["text"] = ' '
    button3["text"] = ' '
    button4["text"] = ' '
    button5["text"] = ' '
    button6["text"] = ' '
    button7["text"] = ' '
    button8["text"] = ' '
    button9["text"] = ' '
    player = 1

def undoGame(event, button):
    global player
    global button1
    if (c is True):
        if player is 1:
            player = 2
        else: player = 1
        button["text"]=" "
    else : messagebox._show(message="Undo has been disabled")

def undoGameMessage():
    messagebox._show(message="Right Click on the respective button in the grid to undo action")

def updateResults():
    pass

def undoDisable():
    global c
    if c is True:
        c = False
    else: c = True

def checkWinner(player):
    global c
    if((button1["text"] == button2["text"] and button2["text"] == button3["text"] and button1["text"] !=" ") or #Horizontal Case
       (button4["text"] == button5["text"] and button5["text"] == button6["text"] and button4["text"] !=" ") or
       (button7["text"] == button8["text"] and button8["text"] == button9["text"] and button7["text"] != " ") or
       (button1["text"] == button4["text"] and button4["text"] == button7["text"] and button1["text"] != " ") or #Vertical Case
       (button2["text"] == button5["text"] and button5["text"] == button8["text"] and button2["text"] != " ") or
       (button3["text"] == button6["text"] and button6["text"] == button9["text"] and button3["text"] != " ") or
       (button1["text"] == button5["text"] and button5["text"] == button9["text"] and button1["text"] != " ") or #Diagonal Case
       (button3["text"] == button5["text"] and button5["text"] == button7["text"] and button3["text"] != " ")):
            if player == 1:
                messagebox._show(message="Player 2 has won the game")
                clearGrid()
                c=True
            else:
                messagebox._show(message="Player 1 has won the game")
                clearGrid()
                c = True
    elif (button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and
          button4["text"]!=" " and button5["text"]!=" " and button6["text"]!=" " and
          button7["text"]!=" " and button8["text"]!=" " and button9["text"] != " " ):
            messagebox._show(message="Game is Drawn")
            clearGrid()
            c = True


def buttonPressed(button):
    global player
    if button["text"]==" " and player == 1 :
        button["text"]="X"
        player=2
    elif button["text"]==" " and player == 2 :
        button["text"]="O"
        player = 1
    else :
        messagebox._show(message="Choose another place on the grid")

    checkWinner(player)

def main():

    global root, c
    root.title("Tic Tac Toe Game")
    root.geometry('5000x5000')
    root.config(bg = 'black')
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
  #------------------------------Menu Section----------------------------------------------------
    menu1 = Menu(root)
    root.config(menu=menu1)
    subMenu = Menu(menu1, tearoff=0)
    menu1.add_cascade(label = 'File', menu = subMenu)
    subMenu.add_command(label = 'Quit', command = closeClick)
    subMenu.add_separator()
    subMenu.add_command(label='Clear', command = clearGrid)
    subMenu.add_separator()
    subMenu.add_command(label='Undo Enable/Disable', command = undoDisable)
    subMenu.add_separator()
    subMenu.add_command(label = 'Results', command = updateResults)
    subMenu.add_separator()
#-----------------------------------------------------------------------------------------------------
#-------------------------------Text to be displayed and input taken-------------------------------------
    topframe = Frame(root, width =50, height= 10)
    topframe.grid(row=0, column=0)
    label = Label(topframe, text="This is a tic tac toe game")
    label.grid(row=0, column=0, columnspan=3, sticky=W)
    #choice = Entry(root)
   # button10 = Button(root, text = "Undo Enable/Disable", command=undoDisable)
    #button10.grid(row =2, column = 5)
#-------------------------------------------------------------------------------------------------------
#------------------------------Buttons-------------------------------------------------------------------
    button1=Button(root, text=' ', command= lambda : buttonPressed(button1))
    button1.grid(row=50, column=1, ipadx=50, ipady=50)
    button1.bind("<Button-2>", lambda event : undoGame(event, button1))

    button2=Button(root, text=' ', command= lambda : buttonPressed(button2))
    button2.grid(row=50, column=2, ipadx=50, ipady=50)
    button2.bind("<Button-2>", lambda event: undoGame(event, button2))

    button3=Button(root, text=' ', command= lambda : buttonPressed(button3))
    button3.grid(row=50, column=3, ipadx=50, ipady=50)
    button3.bind("<Button-2>", lambda event: undoGame(event, button3))


    button4=Button(root, text=' ', command= lambda : buttonPressed(button4))
    button4.grid(row=51, column=1, ipadx=50, ipady=50)
    button4.bind("<Button-2>", lambda event: undoGame(event, button4))

    button5=Button(root, text=' ', command= lambda : buttonPressed(button5))
    button5.grid(row=51, column=2, ipadx=50, ipady=50)
    button5.bind("<Button-2>", lambda event: undoGame(event, button5))

    button6=Button(root, text=' ', command= lambda : buttonPressed(button6))
    button6.grid(row=51, column=3, ipadx=50, ipady=50)
    button6.bind("<Button-2>", lambda event: undoGame(event, button6))

    button7=Button(root, text=' ', command= lambda : buttonPressed(button7))
    button7.grid(row=52, column=1, ipadx=50, ipady=50)
    button7.bind("<Button-2>", lambda event: undoGame(event, button7))

    button8=Button(root, text=' ', command= lambda : buttonPressed(button8))
    button8.grid(row=52, column=2, ipadx=50, ipady=50)
    button8.bind("<Button-2>", lambda event: undoGame(event, button8))

    button9=Button(root, text=' ', command= lambda : buttonPressed(button9))
    button9.grid(row=52, column=3, ipadx=50, ipady=50)
    button9.bind("<Button-2>", lambda event: undoGame(event, button9))
#----------------------------------------------------------------------------------------------------------------

    root.mainloop()

if __name__ == '__main__':
    main()




