import tkinter
from tkinter import *

root=Tk()
root.geometry("700x400")
root.title("tassu kadai")
root.resizable(False,False)
root.configure(bg="olive")

def reset():
    entry_manchurian.delete(0, END)
    entry_redchilly.delete(0, END)
    entry_chukka.delete(0, END)
    entry_greenchilly.delete(0, END)
    entry_wings.delete(0, END)
    entry_legpiece.delete(0, END)
    entry_biriyani.delete(0, END)
    entry_gravy.delete(0, END)
    entry_grill.delete(0, END)

def total():
    try:a1=int(manchurian.get())
    except:a1=0
    try:a2=int(redchilly.get())
    except:a2=0
    try:a3=int(chukka.get())
    except:a3=0
    try:a4=int(greenchilly.get())
    except:a4=0
    try:a5=int(wings.get())
    except:a5=0
    try:a6=int(legpiece.get())
    except:a6=0
    try:a7=int(biriyani.get())
    except:a7=0
    try:a8=int(gravy.get())
    except:a8=0
    try:a9=int(grill.get())
    except:a9=0

    c1=100*a1
    c2=50*a2
    c3=120*a3
    c4=60*a4
    c5=150*a5
    c6=70*a6
    c7=100*a7
    c8=30*a8
    c9=600*a9

    lbl_total=Label(f3,text="TOTAL",font=("Javanese Text",20,"bold"),bg="black",fg="goldenrod",width=12)
    lbl_total.place(x=0,y=60)
    entry_total=Entry(f3,bg="black",textvariable=Total_bill,fg="white",width=60,bd=5)
    entry_total.place(x=0,y=150)
    cost_total = c1+c2+c3+c4+c5+c6+c7+c8+c9
    string_total = "Rs.", str(cost_total)
    Total_bill.set(string_total)

Label(root,text="BILL MANAGEMENT",font=("Segoe UI Black",20,"bold"),bg="darkkhaki",fg="black",width=700,height=2).pack()

#menucard
f1=Frame(root,width=230,height=300,bg="yellow",highlightbackground="black",highlightthickness=2)
f1.place(x=10,y=90)

Label(f1,text="Yenna Sapdalam...?",font=("Ink Free",17,"bold"),bg="yellow",fg="black").place(x=10,y=10)
Label(f1,text="COCKKU READY:",font=("Javanese Text",12,"bold"),bg="yellow",fg="black").place(x=10,y=40)

Label(f1,text="1.manchurian...Rs.100/plate",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=70)
Label(f1,text="2.red chilly...Rs.50/plate",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=90)
Label(f1,text="3.chukka...Rs.120/plate",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=110)
Label(f1,text="4.green chilly...Rs.60/plate",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=130)
Label(f1,text="5.wings...Rs.150/ 3 piece",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=150)
Label(f1,text="6.leg piece...Rs.70/piece",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=170)
Label(f1,text="7.biriyani...Rs.100/plate",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=190)
Label(f1,text="8.gravy...Rs.30/packet",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=210)
Label(f1,text="9.grill...Rs.600-full",font=("Ink Free",12,"bold"),bg="yellow",fg="black").place(x=10,y=230)

f2=Frame(root,width=230,height=300,bg="gold",highlightbackground="black",highlightthickness=2)
f2.place(x=250,y=90)

manchurian=StringVar()
redchilly=StringVar()
chukka=StringVar()
greenchilly=StringVar()
wings=StringVar()
legpiece=StringVar()
biriyani=StringVar()
gravy=StringVar()
grill=StringVar()
Total_bill=StringVar()

label_manchurian=Label(f2,text="manchurian",font=("Segoe Script",12,"bold"),bg="gold",fg="black",width=12)
label_redchilly=Label(f2,text="red chilly",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_chukka=Label(f2,text="chukka",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_greenchilly=Label(f2,text="green chilly",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_wings=Label(f2,text="wings",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_legpiece=Label(f2,text="legpiece",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_biriyani=Label(f2,text="biriyani",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_gravy=Label(f2,text="gravy",font=("Segoe Script",12,"bold"),bg="gold",fg="black")
label_grill=Label(f2,text="grill",font=("Segoe Script",12,"bold"),bg="gold",fg="black")

label_manchurian.place(x=2,y=2)
label_redchilly.place(x=15,y=28)
label_chukka.place(x=15,y=53)
label_greenchilly.place(x=15,y=78)
label_wings.place(x=15,y=103)
label_legpiece.place(x=15,y=128)
label_biriyani.place(x=15,y=153)
label_gravy.place(x=15,y=178)
label_grill.place(x=15,y=203)

entry_manchurian=Entry(f2,textvariable=manchurian,bg="white",fg="black",width=10,bd=3)
entry_redchilly=Entry(f2,textvariable=redchilly,bg="white",fg="black",width=10,bd=3)
entry_chukka=Entry(f2,textvariable=chukka,bg="white",fg="black",width=10,bd=3)
entry_greenchilly=Entry(f2,textvariable=greenchilly,bg="white",fg="black",width=10,bd=3)
entry_wings=Entry(f2,textvariable=wings,bg="white",fg="black",width=10,bd=3)
entry_legpiece=Entry(f2,textvariable=legpiece,bg="white",fg="black",width=10,bd=3)
entry_biriyani=Entry(f2,textvariable=biriyani,bg="white",fg="black",width=10,bd=3)
entry_gravy=Entry(f2,textvariable=gravy,bg="white",fg="black",width=10,bd=3)
entry_grill=Entry(f2,textvariable=grill,bg="white",fg="black",width=10,bd=3)

entry_manchurian.place(x=150,y=5)
entry_redchilly.place(x=150,y=30)
entry_chukka.place(x=150,y=55)
entry_greenchilly.place(x=150,y=80)
entry_wings.place(x=150,y=105)
entry_legpiece.place(x=150,y=130)
entry_biriyani.place(x=150,y=155)
entry_gravy.place(x=150,y=180)
entry_grill.place(x=150,y=205)

button_reset=Button(f2,text="Reset",font=("Segoe Script",12,"bold"),bg="red",fg="black",width=6,height=1,command=reset)
button_reset.place(x=15,y=240)

button_total=Button(f2,text="Total",font=("Segoe Script",12,"bold"),bg="blue",fg="black",width=6,height=1,command=total)
button_total.place(x=140,y=240)

f3=Frame(root,width=200,height=300,bg="goldenrod",highlightbackground="black",highlightthickness=2)
f3.place(x=490,y=90)

bill_label=Label(f3,text="BILL",font=("Javanese Text",20,"bold"),fg="black",bg="goldenrod")
bill_label.place(x=60,y=5)

root.mainloop()