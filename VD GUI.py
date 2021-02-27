from Tkinter import *
win = Tk()
win.title('VirtualDoctor')
win.geometry('1440x1440')
lab1 = Label(win, text = 'Welcome to VirtualDoctor, please enter your name below', width = 100, fg = 'black')
lab1.pack()
txt = Entry(win)
txt.pack()
def onclick():
    message =  'Hello ' + txt.get() + '!' + '\n Choose your symptoms in the next step.'
    lab2 = Label(win, text = message)
    lab2.pack()
    message1 = '\n 1. Cold\
          \n 2. Cough\
          \n 3. Fever\
          \n 4. Weakness\
          \n 5. Weight Loss\
          \n 6. Loss of taste and smell\
          \n 7. Continuous sneezing\
          \n 8. Itchy or running nose\
          \n 9. Breathlessness\
          \n 10.Sweating\
          \n 11.Chest pain\
          \n 12.Frequent hunger\
          \n 13.Eye pain\
          \n 14.Sweating\
          \n 15.Frequent urination\
          \n 16.Rapid breathing\
          \n 17.Vomiting\
          \n 18.Diarrhoea\
          '
        
    lab3 = Label(win, text = message1)
    lab3.pack()
    txt.delete(0, END)

bt1 = Button(win, text = 'Click Here', bg = 'white', fg = 'black', command = onclick,)
bt1.pack()
txt1 = Entry(win, width = 100)
txt1.pack()
txt1.insert(0,'Enter the numbers assigned to your symptoms: ')
win.mainloop()


