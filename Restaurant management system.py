from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("RESTAURENT MANAGEMET SYSTEM")

text_Input = StringVar()
operator = " "

Tops = Frame(root, width = 1600,height = 50,bg = "red",relief=SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800,height = 700,relief=SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300,height = 700,bg= "green",relief=SUNKEN)
f2.pack(side = RIGHT)
#==================================Time=============
localtime = time.asctime(time.localtime(time.time()))
#=========================Info======================
lblInfo = Label(Tops,font = ['arial',50,'bold'],text = "Restaurant Management System",fg = "Royal blue",bd = 10, anchor = 'w')
lblInfo.grid(row = 0,column = 0)
lblDateTime = Label(Tops,font = ['arial',20,'bold'],text = localtime,fg = "Royal blue",bd = 10, anchor = 'w')
lblDateTime.grid(row = 1,column = 0)
#================================Calculator=========
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator= " "
    text_Input.set(" ")
    
def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=" "

def Ref() :
    x = random.randint(10908,500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF =int(Fries.get())
    CoBurger =int(Burger.get())
    CoSamosa =int(Samosa.get())
    CoTea =int(Tea.get())
    CoCold_Drinks =int(Cold_Drinks.get())
    CoPizza=int(Pizza.get())
    CostofFries = CoF * 50
    CostofBurger = CoBurger * 50
    CostofSamosa = CoSamosa * 20
    CostofTea = CoTea * 25
    CostofCold_Drinks = CoCold_Drinks * 40
    CostofPizza = CoPizza * 100

    CostofMeal =  (CostofFries + CostofBurger +
                 CostofSamosa + CostofTea 
                    + CostofCold_Drinks + CostofPizza)

    GST1 = (CostofFries+ CostofBurger +
             CostofSamosa + CostofTea 
             + CostofCold_Drinks + CostofPizza) * (0.5)
    
    Total_Cost1 =(CostofFries + CostofBurger +
                CostofSamosa + CostofTea
                 + CostofCold_Drinks+ CostofPizza)

    Service_Charge1 = ((CostofFries + CostofBurger +
                    CostofSamosa + CostofTea 
                     + CostofCold_Drinks + CostofPizza)/100 * 10)

    OverAllCost1 = (Total_Cost1 + GST1 + Service_Charge1)

    
    Service_Charge.set(str(Service_Charge1))
    Cost_of_Meal.set(CostofMeal)
    GST.set(str(GST1))
    subTotal.set(str(Total_Cost1))
    Total_Cost.set(str(OverAllCost1))

    
def qExit():
    root.destroy()
    
def Reset():
    rand.set(" ")
    Fries.set(" ")
    Burger.set(" ")
    Samosa.set(" ")
    Tea.set(" ")
    Cold_Drinks.set(" ")
    Pizza.set(" ")
    Cost_of_Meal.set(" ")
    Service_Charge.set(" ")
    GST.set(" ")
    Total_Cost.set(" ")
    subTotal.set("  ")
#-----------------------------Calculator-------------------------------------    
txtDisplay = Entry(f2,font = ('arial',20,'bold'),textvariable =text_Input,
bd = 30,insertwidth = 4,bg = "powder blue",justify = 'right')
txtDisplay.grid(columnspan = 4)

#---------------------------------------------------------------------------------
btn7 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='7',bg= "powder blue",command= lambda: btnClick(7)).grid( row= 2,column=0)

btn8 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='8',bg= "powder blue",command= lambda: btnClick(8)).grid( row= 2,column=1)

btn9 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='9',bg= "powder blue",command= lambda: btnClick(9)).grid( row= 2,column=2)

Addition=Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='+',bg= "powder blue",command= lambda: btnClick("+")).grid( row= 2,column=3)
#----------------------------------------------------------------------------
btn6 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='6',bg= "powder blue",command= lambda: btnClick(6)).grid( row= 3,column=0)

btn5 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='5',bg= "powder blue",command= lambda: btnClick(5)).grid( row= 3,column=1)

btn4 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='4',bg= "powder blue",command= lambda: btnClick(9)).grid( row= 3,column=2)

Substraction=Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='-',bg= "powder blue",command= lambda: btnClick("-")).grid( row= 3,column=3)
#----------------------------------------------------------------------------
btn3 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='3',bg= "powder blue",command= lambda: btnClick(3)).grid( row= 4,column=0)

btn2 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='2',bg= "powder blue",command= lambda: btnClick(2)).grid( row= 4,column=1)

btn1 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='1',bg= "powder blue",command= lambda: btnClick(1)).grid( row= 4,column=2)

Multiply=Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='*',bg= "powder blue",command= lambda: btnClick("*")).grid( row= 4,column=3)
#-----------------------------------------------------------------------------
btn0 = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='0',bg= "powder blue",command= lambda: btnClick(0)).grid( row= 5,column=0)

btnClear = Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='C',bg= "powder blue",command=btnClearDisplay).grid( row= 5,column=1)

btnEquals= Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='=',bg= "powder blue",command=btnEqualsInput).grid( row= 5,column=2)

Division =Button(f2,padx = 16,pady = 16,bd = 8,fg= "black", font = ('arial',20,'bold'),
              text='/',bg= "powder blue",command= lambda: btnClick("/")).grid( row= 5,column=3)

#--------------------------------------Restaurent Info 1----------------------------------------
rand          = StringVar()
Fries         = StringVar()
Burger        = StringVar()
Samosa        = StringVar()
Tea           = StringVar()
Cold_Drinks   = StringVar()
Pizza         = StringVar()
Service_Charge= StringVar()
Cost_of_Meal  = StringVar()
GST           = StringVar()
Total_Cost    = StringVar()
subTotal      = StringVar()

lblReference = Label(f1,font =('arial',16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0,column=0)
txtReference = Entry(f1,font =('arial',16, 'bold'),textvariable=rand,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font =('arial',16, 'bold'),text="Large Fries",bd=16,anchor="w")
lblFries.grid(row=1,column=0)
txtFries = Entry(f1,font =('arial',16, 'bold'),textvariable=Fries,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtFries.grid(row=1,column=1)

lblBurger= Label(f1,font =('arial',16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=2,column=0)
txtBurger = Entry(f1,font =('arial',16, 'bold'),textvariable=Burger,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtBurger.grid(row=2,column=1)

lblSamosa = Label(f1,font =('arial',16, 'bold'),text="Samosa",bd=16,anchor="w")
lblSamosa.grid(row=3,column=0)
txtSamosa = Entry(f1,font =('arial',16, 'bold'),textvariable=Samosa,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtSamosa.grid(row=3,column=1)

lblTea = Label(f1,font =('arial',16, 'bold'),text="Tea",bd=16,anchor="w")
lblTea.grid(row=4,column=0)
txtTea = Entry(f1,font =('arial',16, 'bold'),textvariable=Tea,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtTea.grid(row=4,column=1)

lblCold_Drinks = Label(f1,font =('arial',16, 'bold'),text="Cold_Drinks",bd=16,anchor="w")
lblCold_Drinks.grid(row=5,column=0)
txtCold_Drinks = Entry(f1,font =('arial',16, 'bold'),textvariable=Cold_Drinks,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtCold_Drinks.grid(row=5,column=1)
#---------------------------------------------Restaurent Info 2--------------------------

lblPizza = Label(f1,font =('arial',16, 'bold'),text="Pizza",bd=16,anchor="w")
lblPizza.grid(row=0,column=2)
txtPizza = Entry(f1,font =('arial',16, 'bold'),textvariable=Pizza,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtPizza.grid(row=0,column=3)

lblCost_of_Meal = Label(f1,font =('arial',16, 'bold'),text="Cost_of_Meal",bd=16,anchor="w")
lblCost_of_Meal.grid(row=1,column=2)
txtCost_of_Meal = Entry(f1,font =('arial',16, 'bold'),textvariable=Cost_of_Meal,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtCost_of_Meal.grid(row=1,column=3)


lblsubTotal = Label(f1,font =('arial',16, 'bold'),text="subTotal",bd=16,anchor="w")
lblsubTotal.grid(row=2,column=2)
txtsubTotal = Entry(f1,font =('arial',16, 'bold'),textvariable=subTotal,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtsubTotal.grid(row=2,column=3)

lblService_Charge = Label(f1,font =('arial',16, 'bold'),text="Service_Charge",bd=16,anchor="w")
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font =('arial',16, 'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtService_Charge.grid(row=3,column=3)

lblGST = Label(f1,font =('arial',16, 'bold'),text="GST ",bd=16,anchor="w")
lblGST .grid(row=4,column=2)
txtGST  = Entry(f1,font =('arial',16, 'bold'),textvariable=GST,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtGST.grid(row=4,column=3)

lblTotal_Cost = Label(f1,font =('arial',16, 'bold'),text="Total_Cost",bd=16,anchor="w")
lblTotal_Cost.grid(row=5,column=2)
txtTotal_Cost = Entry(f1,font =('arial',16, 'bold'),textvariable=Total_Cost,bd=10,insertwidth=4,
                    bg="powder blue",justify = 'right')
txtTotal_Cost.grid(row=5,column=3)
#-----------------------------------Bottom----------------------------------
btnTotal = Button(f1,padx = 16,bd = 16 , fg = "black" ,font=('arial',16,'bold'),width = 10,
                  text = "Total", bg = "powder blue",command = Ref).grid(row = 7, column=1)

btnReset = Button(f1,padx = 16,bd = 16 , fg = "black" ,font=('arial',16,'bold'),width = 10,
                  text = "Reset", bg = "powder blue",command = Reset).grid(row = 7, column=2)

btnExit = Button(f1,padx = 16,bd = 16 , fg = "black" ,font=('arial',16,'bold'),width = 10,
                  text = "Exit", bg = "powder blue",command = qExit).grid(row = 7, column=3)
root.mainloop()
