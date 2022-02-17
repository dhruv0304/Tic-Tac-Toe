from tkinter import *
import tkinter.messagebox

root = Tk()

root.iconbitmap('tic tac toe.ico')

root.title("Dhruv's Tic Tac Toe")

root.resizable(False,False)

x_clicked = True

count = 0

but1 = StringVar()
but2 = StringVar()
but3 = StringVar()
but4 = StringVar()
but5 = StringVar()
but6 = StringVar()
but7 = StringVar()
but8 = StringVar()
but9 = StringVar()

xPic = PhotoImage(file='X.png')
oPic = PhotoImage(file='O.png')
transPic = PhotoImage(file='transparent.png')

def press(number, r, c):
    global x_clicked, count 
    
    if x_clicked == True:
        labelPic = Label(root,image = xPic)
        labelPic.grid(row = r, column = c)
        if number == 1:
            but1.set('X')
        if number == 2:
            but2.set('X')
        if number == 3:
            but3.set('X')
        if number == 4:
            but4.set('X')
        if number == 5:
            but5.set('X')
        if number == 6:
            but6.set('X')
        if number == 7:
            but7.set('X')
        if number == 8:
            but8.set('X')
        if number == 9:
            but9.set('X')
        
        count += 1
        x_clicked = False    
        checkWin()
    else:
        labelPic = Label(root, image = oPic)
        labelPic.grid(row = r, column = c)
            
        if number == 1:
            but1.set('O')
        if number == 2:
            but2.set('O')
        if number == 3:
            but3.set('O')
        if number == 4:
            but4.set('O')
        if number == 5:
            but5.set('O')
        if number == 6:
            but6.set('O')
        if number == 7:
            but7.set('O')
        if number == 8:
            but8.set('O')
        if number == 9:
            but9.set('O')        
        
        count += 1
        x_clicked = True   
        checkWin()


def playgame():
    
    button1 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#ff4500', textvariable= but1, command = lambda:press(1,0,0))
    button2 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#ff4500', textvariable= but2, command = lambda:press(2,0,1))
    button3 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#ff4500', textvariable= but3, command = lambda:press(3,0,2))
    button4 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#b84518', textvariable= but4, command = lambda:press(4,1,0))
    button5 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#b84518', textvariable= but5, command = lambda:press(5,1,1))
    button6 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#b84518', textvariable= but6, command = lambda:press(6,1,2))
    button7 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#828282', textvariable= but7, command = lambda:press(7,2,0))
    button8 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#828282', textvariable= but8, command = lambda:press(8,2,1))
    button9 = Button(root,image=transPic, bd = 5, relief = 'ridge', bg = '#828282', textvariable= but9, command = lambda:press(9,2,2))

    button1.grid(row = 0, column = 0)
    button2.grid(row = 0, column = 1)
    button3.grid(row = 0, column = 2)
    button4.grid(row = 1, column = 0)
    button5.grid(row = 1, column = 1)
    button6.grid(row = 1, column = 2)
    button7.grid(row = 2, column = 0)
    button8.grid(row = 2, column = 1)
    button9.grid(row = 2, column = 2)

def checkWin():
    global x_clicked, count
    
    if (but1.get() == 'X' and but2.get() == 'X' and but3.get() == 'X' or 
    but4.get() == 'X' and but5.get() == 'X' and but6.get() == 'X' or 
    but7.get() == 'X' and but8.get() == 'X' and but9.get() == 'X' or 
    but1.get() == 'X' and but4.get() == 'X' and but7.get() == 'X' or 
    but2.get() == 'X' and but5.get() == 'X' and but8.get() == 'X' or 
    but3.get() == 'X' and but6.get() == 'X' and but9.get() == 'X' or
    but1.get() == 'X' and but5.get() == 'X' and but9.get() == 'X' or 
    but3.get() == 'X' and but5.get() == 'X' and but7.get() == 'X'):
        tkinter.messagebox.showinfo('tic tac toe','X is the winner!!')
        x_clicked = True
        count = 0
        clear()
    
    
    if (but1.get() == 'O' and but2.get() == 'O' and but3.get() == 'O' or 
    but4.get() == 'O' and but5.get() == 'O' and but6.get() == 'O' or 
    but7.get() == 'O' and but8.get() == 'O' and but9.get() == 'O' or 
    but1.get() == 'O' and but4.get() == 'O' and but7.get() == 'O' or 
    but2.get() == 'O' and but5.get() == 'O' and but8.get() == 'O' or 
    but3.get() == 'O' and but6.get() == 'O' and but9.get() == 'O' or 
    but1.get() == 'O' and but5.get() == 'O' and but9.get() == 'O' or 
    but3.get() == 'O' and but5.get() == 'O' and but7.get() == 'O'):
        tkinter.messagebox.showinfo('tic tac toe','O is the winner!!')
        count = 0
        clear()
        
    elif count == 9:
        tkinter.messagebox.showinfo('Tie Game!!','No One Wins :(')
        x_clicked = True
        count = 0
        clear()

def clear():
    but1.set('')
    but2.set('')
    but3.set('')
    but4.set('')
    but5.set('')
    but6.set('')
    but7.set('')
    but8.set('')
    but9.set('')
    for ele in root.winfo_children():
        ele.destroy()
    playgame()

playgame()
root.mainloop()