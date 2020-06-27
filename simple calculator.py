from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root , width = 40 , borderwidth = 5)
e.grid(row = 0 ,  column = 0 , columnspan = 3, padx = 10 , pady = 10 )

#commmands the buttons would do
def button_click(number):
    current =  e.get()
    e.delete(0 , END)
    e.insert(0 , str(current) + str(number))

def button_clear():
     e.delete(0 , END)

def button_add():
    global math
    global a
    a = e.get()
    e.delete(0 , END)
    math = 'addition'
    
def button_sub():
    global a
    global math
    a = e.get()
    e.delete(0 , END)
    math = 'substract'
    
def button_mul():
    global a
    global math
    a = e.get()
    e.delete(0 , END)
    math = 'multiply'

def button_div():
    global a
    global math
    a = e.get()
    e.delete(0 , END)
    math = 'divide'
    

def button_result():
    num = e.get()
    e.delete(0 , END)
    if(math == 'addition'):
        e.insert(0 , int(a)+int(num))
    elif(math == 'substract'):
        e.insert(0 , int(a)-int(num))
    elif(math == 'multiply'):
        e.insert(0 , int(a)*int(num))
    elif(math=='divide'):
        e.insert(0 , int(a)/int(num)) 
    

    
#creating the buttons
mybutton_1 = Button(root , text= '1' , padx =40 , pady  = 20 ,command =lambda:button_click(1))  
mybutton_2 = Button(root , text= '2' , padx =40 , pady  = 20 ,command =lambda:button_click(2))
mybutton_3 = Button(root , text= '3' , padx =40 , pady  = 20 ,command =lambda:button_click(3))
mybutton_4 = Button(root , text= '4' , padx =40 , pady  = 20 ,command =lambda:button_click(4))
mybutton_5 = Button(root , text= '5' , padx =40 , pady  = 20 ,command =lambda:button_click(5))
mybutton_6 = Button(root , text= '6' , padx =40 , pady  = 20 ,command =lambda:button_click(6))
mybutton_7 = Button(root , text= '7' , padx =40 , pady  = 20 ,command =lambda:button_click(7))
mybutton_8 = Button(root , text= '8' , padx =40 , pady  = 20 ,command =lambda:button_click(8))
mybutton_9 = Button(root , text= '9' , padx =40 , pady  = 20 ,command =lambda:button_click(9))
mybutton_0 = Button(root , text= '0' , padx =40 , pady  = 20 ,command =lambda:button_click(0))
mybutton_eq = Button(root , text= '=' , padx =91 , pady  = 20 , command =button_result)
mybutton_clr = Button(root , text= 'Clear' , padx =79 , pady  = 20 , command = button_clear)
mybutton_plus = Button(root , text= '+' , padx =39 , pady  = 20 , command = button_add)
mybutton_sub = Button(root , text= '-' , padx =39 , pady  = 20 , command = button_sub)
mybutton_mul = Button(root , text= 'x' , padx =39 , pady  = 20 , command = button_mul)
mybutton_div = Button(root , text= '/' , padx =39 , pady  = 20 , command = button_div)
#adding them
mybutton_1.grid(row = 3, column = 0)
mybutton_2.grid(row = 3, column = 1) 
mybutton_3.grid(row = 3, column = 2) 
mybutton_4.grid(row = 2, column = 0) 
mybutton_5.grid(row = 2, column = 1) 
mybutton_6.grid(row = 2, column = 2) 
mybutton_7.grid(row = 1, column = 0) 
mybutton_8.grid(row = 1, column = 1) 
mybutton_9.grid(row = 1, column = 2) 
mybutton_0.grid(row = 4, column = 0)
mybutton_eq.grid(row = 5, column = 1, columnspan = 2 ) 
mybutton_clr.grid(row = 4, column = 1 , columnspan = 2)
mybutton_plus.grid(row = 5, column = 0) 
mybutton_sub.grid(row = 6, column = 0) 
mybutton_mul.grid(row = 6, column = 1) 
mybutton_div.grid(row = 6, column = 2) 

root.mainloop()