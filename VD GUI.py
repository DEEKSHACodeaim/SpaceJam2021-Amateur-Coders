from Tkinter import *
win = Tk()
win.title('VirtualDoctor')
win.geometry('1080x1080')
lab1 = Label(win, text = 'Welcome to VirtualDoctor, please enter your name below', width = 100, fg = 'black')
lab1.pack()
txt = Entry(win)
txt.pack()
def onclick1():
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

bt1 = Button(win, text = 'Click Here(1)', bg = 'white', fg = 'black', command = onclick1,)
bt1.pack()
txt1 = Entry(win, width = 100)
txt1.pack()
txt1.insert(0,'Enter the numbers assigned to your symptoms: ')
def onclick2():
    def disease_check():
        flag = 0
        symp=[]
        s = txt1.get()
        symp=s.split(',')
    def corona():
        count=0
        for i in symp:
            if i=='1':
                count+=1
            if i=='2':
                count+=1
            if i=='3':
                temp=float(input('Enter the body temperature in Fahrenheit:  '))
                if temp>=99:
                    count+=1
            if i=='4':
                count+=1
            if i=='6':
                count+=1
            if i=='9':
                count+=1
            if i=='11':
                count+=1
            else:
                continue

        if count>=4:
            flag=1
            msg1 = 'Patient has been diagnosed with CORONA.'
            med1 = 'Medications:\n Hot water gargling\n Isolation\n Steam inhalation'
            exit()



    def pneumonia():
        count=0
        for i in symp:
            if i=='2':
                count+=1
            if i=='3':
                temp=float(input('Enter the body temperature in Fahrenheit:  '))
                if temp>=99:
                    count+=1
            if i=='4':
                count+=1
            if i=='9':
                count+=1
            if i=='10':
                count+=1
            else:
                continue

        if count>=3:
            flag=1
            msg1 = 'Patient has been diagnosed with PNEUMONIA.'
            med1 = 'Medications:\n Fluoroquinones\n Tetracyclines\n Antibiotics '
            exit()


    
    def typhoid():
            count = 0
            for i in symp:
                if i == '3':
                     temp = float(input('Enter your body temperature in Fahrenheit:  '))
                     if temp>=99:
                          count += 1
                if i == '4':
                     count += 1
                if i == '17':
                      count += 1
                if i == '18':
                      count += 1

            if count >= 3:
                   flag=1
                   msg1 = 'Patient has been diagnosed with TYPHOID.'
                   med1 = 'Medications :\n Maintain fluid diet\n Anti-Biotics\n Penicillin'
                   exit()


    def angina_pectoris():
        count=0
        for i in symp:
            if i=='4':
                count+=1
            if i=='10':
                count+=1
            if i=='11':
                count+=1
            if i=='16':
                count+=1
            else:
                continue

        if count>=3:
            flag=1
            msg1 = 'Patient has been diagnosed with ANGINA PECTORIS.'
            med1 = 'Medications:\n Anticoagulants\n Antianginal\n Regular physical exercise\n Quit smoking'
            exit()


    def conjunctivitis():
             count=0
             for i in symp:
                 if i=='7':
                      count+=1
                 if i=='8':
                       count+=1
                 if i=='13':
                       count+=1
                 else:
                      continue
             if count>=2:
                      flag=1
                      msg1 = "Patient has been diagnosed with CONJUNCTIVITIS."
                      med1 = "Medications:\n Lubricant eye drops \n Wash hands regularly \n Remove contact lenses"
                      exit()

    def diabetes():
        count=0
        for i in symp:
            if i=='4':
                count+=1
            if i=='5':
                count+=1
            if i=='12':
                count+=1
            if i=='15':
                count+=1
            else:
                continue
            
        if count>=3:
            s_level=float(input('Enter blood sugar level before meal: ')) 
            if s_level<80 or s_level>130: 
                   flag=1
                   msg1 = 'Patient has been diagnosed with DIABETES.'
                   med1 = 'Medications:\n Insulin\n Regular exercising\n Maintaining diet '
                   exit()



    def AllergicRhinitis():
             count=0
             for i in symp:
                  if i=='7':
                      count+=1
                  if i=='8':
                      count+=1
                  else:
                      continue
             if count>=1:
                        flag=1
                        msg1 = "Patient has been diagnosed with ALLERGIC RHINITIS."
                        med1 = "Medications:\n Antihistamines \n corticosteroid nasal spray:"
                        exit()
    

    corona()
    pneumonia()
    typhoid()
    angina_pectoris()
    conjunctivitis()
    AllergicRhinitis()
    

    if flag==0:
        print('The patient is HEALTHY!!')
          
           
          
          
    disease_check()
    label1 = Label(win, text = msg1\n msg2)
    label1.pack()
btn1 = Button(win, text = 'Click Here(2)', command = onclick2)
btn1.pack()
win.mainloop()


