from tkinter import *

def write(x):
    s = len(entry.get())
    entry.insert(s,str(x))
    #print(x)

calculation = 5
s1 = 0 

def operations(x):
    global calculation
    calculation = x
    global s1
    s1 = float(entry.get())
    #print(calculation)
    #print(s1)
    entry.delete(0,'end')

s2 = 0
def calculate():
    global s2
    s2 = float(entry.get())
    print(s2)
    global calculation
    result = 0
    if(calculation==0) :
        result= s1 + s2
    elif(calculation==1):
        result = s1 - s2
    elif(calculation == 2):
        result = s1 * s2
    elif(calculation==3):
        result = s1 / s2
    entry.delete(0,'end')
    entry.insert(0,result)

window = Tk()
window.geometry("250x300")

entry = Entry(font="Verdana 14 bold", width=15, justify=RIGHT)
entry.place(x=20, y=20)

b= []

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:write(x)))

counter = 0

for i in range(0,3):
    for j in range(0,3):
        b[counter].place(x=20+j*50,y=50+i*50)
        counter += 1

operation =  []

for i in range(0,4):
    operation.append(Button(fg = "GREEN",font="Verdana 14 bold",width=2,command=lambda x=i:operations(x)))

operation[0]['text'] = "+"
operation[1]['text'] = "-"
operation[2]['text'] = "*"
operation[3]['text'] = "/"


for i in range(0,4):
    operation[i].place(x=170,y=50+50*i)
    
zeroButton = Button(text="0",font="Verdana 14 bold",command=lambda x=0:write(x))
zeroButton.place(x=20,y=200)
    
dotButton = Button(text="." , fg = "RED" ,font="Verdana 14 bold",width=2,command=lambda x=".":write(x))
dotButton.place(x=70, y=200)

equalButton = Button(text="=", fg = "RED",font = "Verdana 14 bold",command=calculate)
equalButton.place(x=120,y=200)

window.mainloop()
