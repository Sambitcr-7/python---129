from tkinter import *
import tkinter.messagebox

root = Tk()

blank_sqace=""
root.title(30 * blank_sqace + "Multiplication Table")
root.geometry("373x642+440+0")
# root.iconbitmap('capt.ico')

text_Input = StringVar()

bgFrame = Frame(root, bd=14, bg='#5F9EA0',relief=RIDGE )
bgFrame.grid()

MainFrame = Frame(bgFrame, bd=7,width=350, height=640,  relief=RIDGE)
MainFrame.grid()


def iExit():
    iExit=tkinter.messagebox.askyesno("Multiplication Table", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()

    else:
        txtDisplay.delete(1.0, END)
        text_Input.set("")

def TimeTable():
    txtDisplay.delete(1.0, END)
    m = int(text_Input.get())
    text_Input.set("")
    for x in range(1,13):
        txtDisplay.insert(END, (x), '\t', "x", '\t', (m), '\t', "=", '\t', (x * m))
        txtDisplay.insert(END, '\n\n')


Titlelabel = Label(MainFrame, text="Multiplication Table", font=('arial', 20, 'bold')).grid(row=0, column=0)

txtInput = Entry(MainFrame, font= ('arail',20, 'bold'), textvariable=text_Input, bd=10, justify='center').grid(row = 1, column = 0)


txtDisplay = Text(MainFrame, font=('arail', 10, 'bold'), bd=10 , width=30, height=23)
txtDisplay.grid(row=2,column=0)

btnTimeTable = Button(MainFrame, font= ('arial', 20, 'bold'), bd=2, padx=2, pady=2, text="Multplication", width= 16, command= TimeTable).grid(row= 3, column=0)


btnExit = Button(MainFrame, font=('arial', 20, 'bold'), bd=2, padx=2, pady=2, text="Exit", width=16,command=iExit).grid(row=4, column=0)

root.mainloop()
