import pandas as pd
from IPython.display import display, HTML, clear_output
from tkinter import *
import turtle
global gate_sel
import time

def make_truth_table(w1,w2,th):
     
    t = pd.DataFrame(index = None)
    
    t['Input 1']=[0,0,1,1]
    t['Input 2']=[0,1,0,1]
    t['Response']=[1 if 0*w1+0*w2>=th else 0,1 if 0*w1+1*w2>=th else 0,1 if 1*w1+0*w2>=th else 0,1 if 1*w1+1*w2>=th else 0]
        
    #display(HTML(t.to_html()))

def get_output(w1,w2,x1,x2,th):
    if w1*x1 + w2*x2 >= th:
        return 1
    else :
        return 0

def get_weights():

    root = Tk()
    root.title('Pick Weights')
    root.geometry("500x250") #You want the size of the app to be 500x500
    #root.resizable(1500, 1500)
    root.option_add("*Label.Font", "courier 24 bold")
    Label(root, text = "Enter Weight 1").grid(row = 0, sticky = W)
    Label(root, text = "Enter Weight 2").grid(row = 1, sticky = W)
    Label(root, text = "Enter Threshold").grid(row = 2, sticky = W)
    # Label(root, text = "Childs Year of Birth").grid(row = 2, sticky = W)
    # Label(root, text = "Childs Month of Birth").grid(row = 3, sticky = W)
    # Label(root, text = "Childs Day of Birth").grid(row = 4, sticky = W)

    wt1 = Entry(root)
    wt2 = Entry(root)
    thr = Entry(root)

    wt1.grid(row = 0, column = 1)
    wt2.grid(row = 1, column = 1)
    thr.grid(row = 2, column = 1)
    
    def getInput():

        a = wt1.get()
        b = wt2.get()
        c = thr.get()
        root.destroy()

        global weights
        weights = [a,b,c]


    Button(root, text = "Submit",
               command = getInput).grid(row = 5, sticky = W)
    mainloop()
        


def set_val(v):
    gate_sel=v

def draw_network(w1,w2,th,x1,x2,gate,close=False):

    output = get_output(w1,w2,x1,x2,th)

    trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
    screen=turtle.Screen()    #making a canvas for drawing
    screen.setup(520,420)    #choosing the screen size
    screen.bgcolor('white')    #making canvas black
    trtl.pencolor('black')    #making colour of the pen red

    trtl.pensize(4)    #choosing the size of pen nib
    trtl.speed(1)    #choosing the speed of drawing
    trtl.shape('turtle')   #choosing the shape of pen nib
    trtl.hideturtle()

    trtl.penup()
    trtl.goto(-100,150)
    trtl.pendown()
    trtl.write("{0} GATE".format(gate), font=("Arial", 24, "bold"))

    trtl.penup()
    trtl.goto(-150,90)
    trtl.pendown()
    trtl.forward(120)    #top line
    trtl.penup()


    trtl.goto(-130,110)
    trtl.pendown()
    trtl.write("w1 = {0}".format(w1), font=("Arial", 16, "normal"))
    trtl.penup()   #moving the pen up
     
    trtl.goto(-150,50)
    trtl.pendown()
    trtl.forward(120)    #top line
    trtl.penup()   #moving the pen down

    trtl.goto(-130,20)
    trtl.pendown()
    trtl.write("w2 = {0}".format(w2), font=("Arial", 16, "normal"))

    trtl.penup()
    trtl.goto(-220,80)
    trtl.pendown()
    trtl.write("x1 = {0}".format(x1), font=("Arial", 16, "normal"))
    trtl.penup()
    trtl.goto(-220,40)
    trtl.pendown()
    trtl.write("x2 = {0}".format(x2), font=("Arial", 16, "normal"))


    if output == 1:
        trtl.fillcolor("green")
    else:
        trtl.fillcolor("red")

    trtl.penup()
    trtl.goto(5,-20)
    trtl.pendown()
    trtl.write("\u03B8 = {0}".format(th), font=("Arial", 16, "normal"))
    trtl.penup()   #moving the pen up
    trtl.begin_fill()
    trtl.penup()   #moving the pen up
    trtl.goto(30,10)
    trtl.pendown()
    trtl.circle(60)   #drawing circle with radius 60 pixels 
    trtl.end_fill()
    
    
    trtl.penup()   #moving the pen down

    trtl.goto(90,70)
    trtl.pendown()
    trtl.forward(120) 

    trtl.penup()
    trtl.goto(110,90)
    trtl.pendown()
    trtl.write("output={0}".format(output), font=("Arial", 16, "normal"))

    time.sleep(3)

    screen.clear()
    #screen.mainloop()

    if(close):
        screen.bye()

        
onceMore = True
while(onceMore==True):
    #clear_output()
    
    master = Tk()
    var = IntVar()
    var.set(1)

    def quit_loop():
        #print("Selection:",var.get())
        global selection
        selection = var.get()
        master.destroy()
    
    def quit_loop_2():
        #print("Selection:",var.get())
        global selection2
        selection2 = var1.get()
        nextOne.destroy()
    
    master.title("CHOOSE AN OPTION")
    master.geometry("500x250")
    master.option_add("*Label.Font", "courier 24 bold")
    Label(master, text = "CHOOSE A GATE TO IMPLEMENT:").grid(row=0, sticky=W)
    Radiobutton(master, text = "AND", font="courier 24 bold",variable=var, value = 1).grid(row=1, sticky=W)
    Radiobutton(master, text = "OR", font="courier 24 bold",  variable=var, value = 2).grid(row=2, sticky=W)
    Radiobutton(master, text = "AND-NOT", font="courier 24 bold", variable=var, value = 3).grid(row=3, sticky=W)
    Radiobutton(master, text = "CUSTOM", font="courier 24 bold", variable=var, value = 4).grid(row=4, sticky=W)
    Button(master, text = "SUBMIT", font="courier 24 bold", command=quit_loop).grid(row=5, sticky=W)
    #Button(master, text = "OK", command=quit_loop).grid(row=5, sticky=W)
    #button = Button(master, text="Okay", command=master.destroy)
    #button.pack()
    master.mainloop()
    
    if selection == 1:
    #print ("My Value is equal to one.")
        gate_sel=1
        #print("AND Gate")

        draw_network(1,1,2,0,0,'AND')
        draw_network(1,1,2,0,1,'AND')
        draw_network(1,1,2,1,0,'AND')
        draw_network(1,1,2,1,1,'AND',close=True)
        #make_truth_table(1,1,2)
    elif selection == 2:
        gate_sel=2
        #print("OR Gate")
        draw_network(2,2,2,0,0,'OR')
        draw_network(2,2,2,0,1,'OR')
        draw_network(2,2,2,1,0,'OR')
        draw_network(2,2,2,1,1,'OR',close=True)
        #make_truth_table(2,2,2)
        #print ("My value is equal to two.")
    elif selection == 3:
        gate_sel=3
        #print("AND-NOT Gate")
        draw_network(2,-1,2,0,0,'AND-NOT')
        draw_network(2,-1,2,0,1,'AND-NOT')
        draw_network(2,-1,2,1,0,'AND-NOT')
        draw_network(2,-1,2,1,1,'AND-NOT',close=True)
        #make_truth_table(2,-1,2)
    elif selection == 4:
        gate_sel=4
        get_weights()
        weights=[int(x) for x in weights]
        #print("CUSTOM Gate")
        draw_network(weights[0],weights[1],weights[2],0,0,'CUSTOM')
        draw_network(weights[0],weights[1],weights[2],0,1,'CUSTOM')
        draw_network(weights[0],weights[1],weights[2],1,0,'CUSTOM')
        draw_network(weights[0],weights[1],weights[2],1,1,'CUSTOM',close=True)
        #make_truth_table(weights[0],weights[1],weights[2])
        
        
    
    nextOne = Tk()
    var1 = IntVar()
    var1.set(1)
    nextOne.title("Would you like to try again?")
    nextOne.geometry("500x250")
    nextOne.option_add("*Label.Font", "courier 24 bold")

    Radiobutton(nextOne, text = "YES", font="courier 24 bold", variable=var1, value = 1).grid(row=1, sticky=W)
    Radiobutton(nextOne, text = "NO", font="courier 24 bold", variable=var1, value = 2).grid(row=2, sticky=W)
    Button(nextOne, text = "SUBMIT", command=quit_loop_2).grid(row=3, sticky=W)
    nextOne.mainloop()
    
    if(selection2==1):
        print("\n\n\n")
        onceMore=True
    else:
        print("\nHope you liked this :)")
        onceMore=False
    