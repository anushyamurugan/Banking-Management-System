from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from time import gmtime,strftime
from tkinter import PhotoImage

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return
    

def write(master,name,pin,oc):
    if((is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0) or name==" "):
        messagebox.showinfo("Error","Invalid Credentials \nPlease try again.")
        master.destroy()
        return

    f1=open("Accnt_Record.txt",'r')
    accnt_no=int(f1.readline())
    accnt_no+=1
    f1.close()

    f1=open("Accnt_Record.txt",'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no)+".txt","w")
    fdet.write(pin+"\n")
    fdet.write(oc+"\n")
    fdet.write(str(accnt_no)+"\n")
    fdet.write(name+"\n")
    fdet.close()

    frec=open(str(accnt_no)+"-rec.txt",'w')
    frec.write("Date                             Credit               Debit            Balance\n")
    frec.write(str(strftime("[%Y-%m-%D][%H-%M-%S]",gmtime()))+"     "+oc+"                                  "+oc+"\n")
    frec.close()
    messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
    master.destroy()
    return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"        "+str(amti)+"                                   "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"               "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return
	
#main window 
x = Tk()
x.title('My Project')
x.geometry("1800x1000")
x.configure(background="#FEFEFE") 
lb = Label(x, text="Welcome to my page", bg="white", fg="black", font=("Times New Roman", 20))
lb.pack()
i1 = Image.open('bank.jpg')
i2 = i1.resize((500, 500))
i3 = ImageTk.PhotoImage(i2)
f = Frame(x, height=500, width=500)
f.pack()
lb2 = Label(f, image=i3)
lb2.place(x=0, y=0)
#login image
l1=Image.open('loginbutton.png')
l2=l1.resize((100,75))
l3=ImageTk.PhotoImage(l2)
#create account image
c1=Image.open('createaccount.png')
c2=c1.resize((100,75))
c3=ImageTk.PhotoImage(c2)
img6=Image.open('quitbutton.png')
img7=img6.resize((100,75))
img8=ImageTk.PhotoImage(img7)
b6=Button(image=img8,command=x.destroy)
b6.image=img8
b6.place(x=790,y=530)

def Cr_Amt(accnt,name):
	creditwn=Tk()
	creditwn.geometry("1800x1000")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="#DCBEBC")
	fr1=Frame(creditwn,bg="blue")
	l_title=Message(creditwn,text="Credit Details",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
	e1=Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))

def De_Amt(accnt,name):
	debitwn=Tk()
	debitwn.geometry("1800x1000")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="#DCBEBC")
	fr1=Frame(debitwn,bg="blue")
	l_title=Message(debitwn,text="Debit details",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=Label(debitwn,relief="raised",text="Enter Amount to be debited: ")
	e1=Entry(debitwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=Button(debitwn,text="Debit",relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))

def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

def disp_tr_hist(accnt):
	disp_wn=Tk()
	disp_wn.geometry("1800x1000")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="#DCBEBC")
	fr1=Frame(disp_wn,bg="blue")
	l_title=Message(disp_wn,text="Transaction History",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=Frame(disp_wn)
	fr1.pack(side="top")
	l1=Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="#7B4F47",fg="black",relief="raised")
	l1.pack(side="top")
	fr2=Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()

#login menu
def login_menu(accnt,name):
    g=Toplevel()
    g.title('submit details')
    g.geometry("1800x1000")
    g.configure(background="#E5E2E2")
    g1= Label(g, text="Login Menu", bg="white", fg="black", font=("Times New Roman", 20))
    g1.place(x=550,y=10)
    i1=PhotoImage(file='credit.gif')
    i2=i1.subsample(2,2)
    button = Button(g, image=i2,command=lambda: Cr_Amt(accnt,name))
    button.image = i2  
    button.place(x=350, y=100)
    i3=PhotoImage(file='debit.gif')
    i4=i3.subsample(2,2)
    button = Button(g, image=i4,command=lambda: De_Amt(accnt,name))
    button.image = i4
    button.place(x=750, y=100)
    i5=PhotoImage(file='checkbalance.gif')
    i6=i5.subsample(2,2)
    button = Button(g, image=i6,command=lambda: disp_bal(accnt))
    button.image = i6
    button.place(x=350, y=400)
    i7=PhotoImage(file='history.gif')
    i8=i7.subsample(2,2)
    button = Button(g, image=i8,command=lambda: disp_tr_hist(accnt))
    button.image = i8
    button.place(x=750, y=400)
    border_size = 10
    border_color = 'black'
    img6=PhotoImage(file="logout.gif")
    myimg6=img6.subsample(2,2)
    b6=Button(g,image=myimg6,command=lambda: logout(g))
    b6.image=myimg6
    b6.place(x=570,y=550)

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
	else:
		master.destroy()
		login_menu(acc_num,name)




    
#login function		
def login():
    y=Tk()
    y.title('Login details')
    y.geometry("1800x1000")
    y.configure(background="#E5E2E2")
    l1= Label(y, text="User Details", bg="white", fg="black", font=("Times New Roman", 20))
    l1.place(x=550,y=100)
    l2=Label(y,text="Enter Username",font=('Times New Roman',20),fg="black")
    l2.place(x=300,y=175)
    l3=Label(y,text="Enter Account Number",font=('Times New Roman',20),fg="black")
    l3.place(x=300,y=275)
    l4=Label(y,text="Enter Pin Number",font=('Times New Roman',20),fg="black")
    l4.place(x=300,y=375)

    
    e1=Entry(y,font=("Times New Roman",20),fg="black",bg="#F3EFEF")
    e1.place(x=650,y=175)
    e2=Entry(y,font=("Times New Roman",20),fg="black",bg="#F3EFEF")
    e2.place(x=650,y=275)
    e3=Entry(y,font=("Times New Roman",20),fg="black",bg="#F3EFEF",show="*")
    e3.place(x=650,y=375)
    b2=Button(y,text="Submit",height=3,width=7,command=lambda: check_log_in(y,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b2.place(x=550,y=500)
    y.bind("<Return>",lambda x:check_log_in(y,e1.get().strip(),e2.get().strip(),e3.get().strip()))


    
b=Button(x,image=l3,command=login)
b.place(x=390,y=530)


def create_account():
    z=Tk()
    z.title('Create Account')
    z.geometry("1800x1000")
    z.configure(background="#E5E2E2")
    k1= Label(z, text="User Details", bg="white", fg="black", font=("Times New Roman", 20))
    k1.place(x=550,y=100)
    k2=Label(z,text="Enter Name",font=('Times New Roman',20),fg="black")
    k2.place(x=300,y=175)
    k3=Label(z,text="Provide Pin",font=('Times New Roman',20),fg="black")
    k3.place(x=300,y=275)
    k4=Label(z,text="Opening Credit",font=('Times New Roman',20),fg="black")
    k4.place(x=300,y=375)

    
    f1=Entry(z,font=("Times New Roman",20),fg="black",bg="#F3EFEF")
    f1.place(x=650,y=175)
    f2=Entry(z,font=("Times New Roman",20),fg="black",bg="#F3EFEF",show="*")
    f2.place(x=650,y=275)
    f3=Entry(z,font=("Times New Roman",20),fg="black",bg="#F3EFEF")
    f3.place(x=650,y=375)
    
    bu=Button(z,text="Submit",font=('Times New Roman',25),command= lambda : write(z,f1.get().strip(),f2.get().strip(),f3.get().strip()))
    bu.place(x=550,y=500)
    z.bind("<Return>",lambda x: write(z,f1.get().strip(),f2.get().strip(),f3.get().strip()))
    return
    
    
b1=Button(x,image=c3,command=create_account)
b1.place(x=590,y=530)












