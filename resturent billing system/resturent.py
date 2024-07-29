from tkinter import*
from tkinter import messagebox
import random
import os,tempfile
if not os.path.exists('bills'):
    os.mkdir('bills')
def clear():
    bathsoap_entry.delete(0,END)
    facecreme_entry.delete(0,END)
    facewash_entry.delete(0,END)
    hairspray_entry.delete(0,END)
    hairgel_entry.delete(0,END)
    bodyloson_entry.delete(0,END)
    rice_entry.delete(0,END)
    oil_entry.delete(0,END)
    daal_entry.delete(0,END)
    wheat_entry.delete(0,END)
    sugar_entry.delete(0,END)
    tea_entry.delete(0,END)
    maaza_entry.delete(0,END)
    pepsi_entry.delete(0,END)
    sprite_entry.delete(0,END)
    dew_entry.delete(0,END)
    fruti_entry.delete(0,END)
    coca_cola_entry.delete(0,END)
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    bill_entry.delete(0,END)
    cosmeticprice_entry.delete(0,END)
    groceryprice_entry.delete(0,END)
    drinkprice_entry.delete(0,END)
    textarea.delete(1.0,END)
    cosmetictax_entry.delete(0,END)
    grocerytax_entry.delete(0,END)
    drinktax_entry.delete(0,END)

    bathsoap_entry.insert(0,0)
    facecreme_entry.insert(0,0)
    facewash_entry.insert(0,0)
    hairspray_entry.insert(0,0)
    hairgel_entry.insert(0,0)
    bodyloson_entry.insert(0,0)
    rice_entry.insert(0,0)
    oil_entry.insert(0,0)
    daal_entry.insert(0,0)
    wheat_entry.insert(0,0)
    sugar_entry.insert(0,0)
    tea_entry.insert(0,0)
    maaza_entry.insert(0,0)
    pepsi_entry.insert(0,0)
    sprite_entry.insert(0,0)
    dew_entry.insert(0,0)
    fruti_entry.insert(0,0)
    coca_cola_entry.insert(0,0)
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
def search_bill():
    for i in os.listdir('bills/'):
        print(bill_entry.get())
        if i.split('.')[0]== ' '+bill_entry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
        else:
            messagebox.showerror('error','invalid bill number')
            break

def is_save():
    global billnumber
    result=messagebox.askyesno('message','Do you want to save the bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'{billnumber} is saved successfully')
        billnumber=random.randint(500,1000)
billnumber=random.randint(500,1000)
def billrecept():
    if name_entry.get()=='' or phone_entry.get()=='':
        messagebox.showerror('Error','customer details are required')
    elif cosmeticprice_entry.get()=='' and groceryprice_entry.get()=='' and drinkprice_entry.get()=='':
        messagebox.showerror('Error','No product is selected')
    elif cosmeticprice_entry.get()=='0 Rs' and groceryprice_entry.get()=='0 Rs' and drinkprice_entry.get()=='0 Rs':
        messagebox.showerror('Error','No product is selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t **Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {name_entry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number: {phone_entry.get()}\n')
        textarea.insert(END,'\n============================================================\n')
        textarea.insert(END,'Product \t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n============================================================\n')
        if bathsoap_entry.get()!='0':
            textarea.insert(END,f'Bath Soap\t\t\t  {bathsoap_entry.get()}\t\t\t  {bathsoap1}\n')
        if facecreme_entry.get()!='0':
            textarea.insert(END,f'Facecreme\t\t\t  {facecreme_entry.get()}\t\t\t  {facecreme1}\n')
        if facewash_entry.get()!='0':
            textarea.insert(END,f'Facewash\t\t\t  {facewash_entry.get()}\t\t\t  {fashwash1}\n')
        if hairspray_entry.get()!='0':
            textarea.insert(END,f'Hair Spray\t\t\t  {hairspray_entry.get()}\t\t\t  {hairspray1}\n')
        if hairgel_entry.get()!='0':
            textarea.insert(END,f'Hair Gel\t\t\t  {hairgel_entry.get()}\t\t\t  {hairgel1}\n')
        if bodyloson_entry.get()!='0':
            textarea.insert(END,f'Body Loson\t\t\t  {bodyloson_entry.get()}\t\t\t  {bodyloson1}\n')
        if rice_entry.get()!='0':
            textarea.insert(END,f'Rice\t\t\t  {rice_entry.get()}\t\t\t  {rice1}\n')
        if oil_entry.get()!='0':
            textarea.insert(END,f'Oil\t\t\t  {oil_entry.get()}\t\t\t  {oil1}\n')
        if daal_entry.get()!='0':
            textarea.insert(END,f'Daal\t\t\t  {daal_entry.get()}\t\t\t  {daal1}\n')
        if wheat_entry.get()!='0':
            textarea.insert(END,f'Wheat\t\t\t  {wheat_entry.get()}\t\t\t  {wheat1}\n')
        if sugar_entry.get()!='0':
            textarea.insert(END,f'Suger\t\t\t  {sugar_entry.get()}\t\t\t  {suger1}\n')
        if tea_entry.get()!='0':
            textarea.insert(END,f'Tea\t\t\t  {tea_entry.get()}\t\t\t  {tea1}\n')
        if maaza_entry.get()!='0':
            textarea.insert(END,f'Maaza\t\t\t  {maaza_entry.get()}\t\t\t  {maaza1}\n')
        if pepsi_entry.get()!='0':
            textarea.insert(END,f'Pepsi\t\t\t  {pepsi_entry.get()}\t\t\t  {pepsi1}\n')
        if sprite_entry.get()!='0':
            textarea.insert(END,f'Sprite\t\t\t  {sprite_entry.get()}\t\t\t  {sprite1}\n')
        if dew_entry.get()!='0':
            textarea.insert(END,f'Dew\t\t\t  {dew_entry.get()}\t\t\t  {dew1}\n')
        if coca_cola_entry.get()!='0':
            textarea.insert(END,f'Coca Cola\t\t\t  {coca_cola_entry.get()}\t\t\t  {coca_cola1}\n')
        if fruti_entry.get()!='0':
            textarea.insert(END,f'Fruti\t\t\t  {fruti_entry.get()}\t\t\t  {fruti1}\n')
        textarea.insert(END,'------------------------------------------------------------')
        if cosmeticprice_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmatic Tax\t\t{cosmetictax_entry.get()}')
        if groceryprice_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Grocery Tax\t\t{grocerytax_entry.get()}')
        if drinkprice_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cold Drinks Tax\t\t{drinktax_entry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')    
        textarea.insert(END,'\n------------------------------------------------------------')
        is_save()

def total():
    global bathsoap1,facecreme1,fashwash1,hairspray1,hairgel1,bodyloson1
    global rice1,oil1,daal1,wheat1,suger1,tea1
    global maaza1,pepsi1,sprite1,dew1,coca_cola1,fruti1
    global totalbill
    bathsoap1=int(bathsoap_entry.get())*75
    facecreme1=int(facecreme_entry.get())*100
    fashwash1=int(facecreme_entry.get())*95
    hairspray1=int(hairspray_entry.get())*85
    hairgel1=int(hairgel_entry.get())*20
    bodyloson1=int(bodyloson_entry.get())*50
    totalcosprice=bathsoap1+facecreme1+fashwash1+hairspray1+hairgel1+bodyloson1
    cosmeticprice_entry.delete(0,END)
    cosmeticprice_entry.insert(0,f'{totalcosprice} Rs')
    cosmatictax=totalcosprice*0.25
    cosmetictax_entry.delete(0,END)
    cosmetictax_entry.insert(0,f'{cosmatictax} Rs')

    rice1=int(rice_entry.get())*55
    oil1=int(oil_entry.get())*100
    daal1=int(daal_entry.get())*67
    wheat1=int(wheat_entry.get())*75
    suger1=int(sugar_entry.get())*50
    tea1=int(tea_entry.get())*75
    totalgroprice=rice1+oil1+daal1+wheat1+suger1+tea1
    groceryprice_entry.delete(0,END)
    groceryprice_entry.insert(0,f'{totalgroprice} Rs')
    groserytax=totalgroprice*0.05
    grocerytax_entry.delete(0,END)
    grocerytax_entry.insert(0,f'{groserytax} Rs')


    maaza1=int(maaza_entry.get())*75
    pepsi1=int(pepsi_entry.get())*55
    sprite1=int(sprite_entry.get())*75
    dew1=int(dew_entry.get())*45
    coca_cola1=int(coca_cola_entry.get())*57
    fruti1=int(fruti_entry.get())*55
    totaldrinkprice=maaza1+pepsi1+sprite1+dew1+coca_cola1+fruti1
    drinkprice_entry.delete(0,END)
    drinkprice_entry.insert(0,f'{totaldrinkprice} Rs')
    drink=totaldrinkprice*0.15
    drinktax_entry.delete(0,END)
    drinktax_entry.insert(0,f'{drink} Rs')
    totalbill =totalcosprice+totaldrinkprice+totalgroprice+cosmatictax+groserytax+drink


root=Tk()
root.title("Retail billing system")
root.geometry('1270x600')
root.iconbitmap('data.ico')
heading=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
heading.pack(fill=X)
customer_details=LabelFrame(root,text='customer info',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
customer_details.pack(fill=X,pady=2)
name=Label(customer_details,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
name.grid(row=0,column=0,padx=20)
name_entry=Entry(customer_details,font=('arial',15),bd=7,width=18)
name_entry.grid(row=0,column=1)
phone=Label(customer_details,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phone.grid(row=0,column=2,padx=20)
phone_entry=Entry(customer_details,font=('arial',15),bd=7,width=18)
phone_entry.grid(row=0,column=3)
bill=Label(customer_details,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bill.grid(row=0,column=4,padx=20)
bill_entry=Entry(customer_details,font=('arial',15),bd=7,width=18)
bill_entry.grid(row=0,column=5)
search=Button(customer_details,text='Search',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
search.grid(row=0,column=6,padx=20,pady=8)
product_frame=Frame(root)
product_frame.pack(pady=5)
cosmatic=LabelFrame(product_frame,text='Cosmatics',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
cosmatic.grid(row=0,column=0,padx=10)
bathsoap=Label(cosmatic,text='Bathsoap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoap.grid(row=0,column=0,pady=9,padx=10,sticky='w');
bathsoap_entry=Entry(cosmatic,font=('times new roman',15,'bold'),bd=5,width=10)
bathsoap_entry.grid(row=0,column=1,pady=9,padx=10)
bathsoap_entry.insert(0,0)

facecreme=Label(cosmatic,text='Facecreme',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreme.grid(row=1,column=0,pady=9,padx=10,sticky='w');
facecreme_entry=Entry(cosmatic,font=('times new roman',15,'bold'),bd=5,width=10)
facecreme_entry.grid(row=1,column=1,pady=9,padx=10)
facecreme_entry.insert(0,0)

facewash=Label(cosmatic,text='Facewash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewash.grid(row=2,column=0,pady=9,padx=10,sticky='w');
facewash_entry=Entry(cosmatic,font=('times new roman',15,'bold'),bd=5,width=10)
facewash_entry.grid(row=2,column=1,pady=9,padx=10)
facewash_entry.insert(0,0)

hairspray=Label(cosmatic,text='Hairspray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairspray.grid(row=3,column=0,pady=9,padx=10,sticky='w');
hairspray_entry=Entry(cosmatic,font=('times new roman',15,'bold'),bd=5,width=10)
hairspray_entry.grid(row=3,column=1,pady=9,padx=10)
hairspray_entry.insert(0,0)

hairgel=Label(cosmatic,text='Hairgel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgel.grid(row=4,column=0,pady=9,padx=10,sticky='w');
hairgel_entry=Entry(cosmatic,font=('times new roman',15,'bold'),bd=5,width=10)
hairgel_entry.grid(row=4,column=1,pady=9,padx=10)
hairgel_entry.insert(0,0)

bodyloson=Label(cosmatic,text='Bodyloson',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodyloson.grid(row=5,column=0,pady=9,padx=10,sticky='w');
bodyloson_entry=Entry(cosmatic,font=('times new roman',15,'bold'),bd=5,width=10)
bodyloson_entry.grid(row=5,column=1,pady=9,padx=10)
bodyloson_entry.insert(0,0)

grocery=LabelFrame(product_frame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
grocery.grid(row=0,column=1,padx=10)

rice=Label(grocery,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
rice.grid(row=0,column=0,pady=9,padx=10,sticky='w');
rice_entry=Entry(grocery,font=('times new roman',15,'bold'),bd=5,width=10)
rice_entry.grid(row=0,column=1,pady=9,padx=10)
rice_entry.insert(0,0)

oil=Label(grocery,text='oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oil.grid(row=1,column=0,pady=9,padx=10,sticky='w');
oil_entry=Entry(grocery,font=('times new roman',15,'bold'),bd=5,width=10)
oil_entry.grid(row=1,column=1,pady=9,padx=10)
oil_entry.insert(0,0)

daal=Label(grocery,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daal.grid(row=2,column=0,pady=9,padx=10,sticky='w');
daal_entry=Entry(grocery,font=('times new roman',15,'bold'),bd=5,width=10)
daal_entry.grid(row=2,column=1,pady=9,padx=10)
daal_entry.insert(0,0)

wheat=Label(grocery,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheat.grid(row=3,column=0,pady=9,padx=10,sticky='w');
wheat_entry=Entry(grocery,font=('times new roman',15,'bold'),bd=5,width=10)
wheat_entry.grid(row=3,column=1,pady=9,padx=10)
wheat_entry.insert(0,0)

sugar=Label(grocery,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugar.grid(row=4,column=0,pady=9,padx=10,sticky='w');
sugar_entry=Entry(grocery,font=('times new roman',15,'bold'),bd=5,width=10)
sugar_entry.grid(row=4,column=1,pady=9,padx=10)
sugar_entry.insert(0,0)

tea=Label(grocery,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
tea.grid(row=5,column=0,pady=9,padx=10,sticky='w');
tea_entry=Entry(grocery,font=('times new roman',15,'bold'),bd=5,width=10)
tea_entry.grid(row=5,column=1,pady=9,padx=10)
tea_entry.insert(0,0)

colddrinks=LabelFrame(product_frame,text='Cold drinks',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
colddrinks.grid(row=0,column=3,padx=10)

maaza=Label(colddrinks,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maaza.grid(row=0,column=0,pady=9,padx=10,sticky='w');
maaza_entry=Entry(colddrinks,font=('times new roman',15,'bold'),bd=5,width=10)
maaza_entry.grid(row=0,column=1,pady=9,padx=10)
maaza_entry.insert(0,0)

pepsi=Label(colddrinks,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsi.grid(row=1,column=0,pady=9,padx=10,sticky='w');
pepsi_entry=Entry(colddrinks,font=('times new roman',15,'bold'),bd=5,width=10)
pepsi_entry.grid(row=1,column=1,pady=9,padx=10)
pepsi_entry.insert(0,0)

sprite=Label(colddrinks,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sprite.grid(row=2,column=0,pady=9,padx=10,sticky='w');
sprite_entry=Entry(colddrinks,font=('times new roman',15,'bold'),bd=5,width=10)
sprite_entry.grid(row=2,column=1,pady=9,padx=10)
sprite_entry.insert(0,0)

dew=Label(colddrinks,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dew.grid(row=3,column=0,pady=9,padx=10,sticky='w');
dew_entry=Entry(colddrinks,font=('times new roman',15,'bold'),bd=5,width=10)
dew_entry.grid(row=3,column=1,pady=9,padx=10)
dew_entry.insert(0,0)

fruti=Label(colddrinks,text='Fruti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
fruti.grid(row=4,column=0,pady=9,padx=10,sticky='w');
fruti_entry=Entry(colddrinks,font=('times new roman',15,'bold'),bd=5,width=10)
fruti_entry.grid(row=4,column=1,pady=9,padx=10)
fruti_entry.insert(0,0)

coca_cola=Label(colddrinks,text='Coca Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
coca_cola.grid(row=5,column=0,pady=9,padx=10,sticky='w');
coca_cola_entry=Entry(colddrinks,font=('times new roman',15,'bold'),bd=5,width=10)
coca_cola_entry.grid(row=5,column=1,pady=9,padx=10)
coca_cola_entry.insert(0,0)

bill_frame=Frame(product_frame,bd=8,relief=GROOVE)
bill_frame.grid(row=0,column=4)

billarea=Label(bill_frame,text='Bill area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billarea.pack(fill=X)

scrollbare=Scrollbar(bill_frame,orient=VERTICAL)
scrollbare.pack(side=RIGHT,fill=Y)

textarea=Text(bill_frame,height=18,width=60,yscrollcommand=Scrollbar.set)
textarea.pack(padx=10)
scrollbare.config(command=textarea.yview)

bill_menu=LabelFrame(root,text='Bill Menu',font=('times new roman',12,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
bill_menu.pack(fill=X,)

cosmeticprice=Label(bill_menu,text='Cosmetic Price',font=('times new roman',12,'bold'),bg='gray20',fg='white')
cosmeticprice.grid(row=0,column=0,pady=9,padx=10,sticky='w');
cosmeticprice_entry=Entry(bill_menu,font=('times new roman',12,'bold'),bd=5,width=20)
cosmeticprice_entry.grid(row=0,column=1,pady=9,padx=10)

groceryprice=Label(bill_menu,text='Grocery Price',font=('times new roman',12,'bold'),bg='gray20',fg='white')
groceryprice.grid(row=1,column=0,pady=9,padx=10,sticky='w');
groceryprice_entry=Entry(bill_menu,font=('times new roman',12,'bold'),bd=5,width=20)
groceryprice_entry.grid(row=1,column=1,pady=9,padx=10)

drinkprice=Label(bill_menu,text='Cold Drink Price',font=('times new roman',12,'bold'),bg='gray20',fg='white')
drinkprice.grid(row=2,column=0,pady=9,padx=10,sticky='w');
drinkprice_entry=Entry(bill_menu,font=('times new roman',12,'bold'),bd=5,width=20)
drinkprice_entry.grid(row=2,column=1,pady=9,padx=10)

cosmetictax=Label(bill_menu,text='Cosmetic Tax',font=('times new roman',12,'bold'),bg='gray20',fg='white')
cosmetictax.grid(row=0,column=2,pady=9,padx=10,sticky='w');
cosmetictax_entry=Entry(bill_menu,font=('times new roman',12,'bold'),bd=5,width=20)
cosmetictax_entry.grid(row=0,column=3,pady=9,padx=10)

grocerytax=Label(bill_menu,text='Grocery Tax',font=('times new roman',12,'bold'),bg='gray20',fg='white')
grocerytax.grid(row=1,column=2,pady=9,padx=10,sticky='w');
grocerytax_entry=Entry(bill_menu,font=('times new roman',12,'bold'),bd=5,width=20)
grocerytax_entry.grid(row=1,column=3,pady=9,padx=10)

drinktax=Label(bill_menu,text='Cold Drink Tax',font=('times new roman',12,'bold'),bg='gray20',fg='white')
drinktax.grid(row=2,column=2,pady=9,padx=10,sticky='w');
drinktax_entry=Entry(bill_menu,font=('times new roman',12,'bold'),bd=5,width=20)
drinktax_entry.grid(row=2,column=3,pady=9,padx=10)

buttonframe=Frame(bill_menu,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3,padx=10)

totalbutton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,pady=10,width=9,command=total)
totalbutton.grid(row=0,column=0,padx=16,pady=20)

billbutton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,pady=10,width=9,command=billrecept)
billbutton.grid(row=0,column=1,padx=16,pady=20)

clearbutton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,pady=10,width=9,command=clear)
clearbutton.grid(row=0,column=2,padx=16,pady=20)

printbutton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,pady=10,width=9,command=print_bill)
printbutton.grid(row=0,column=3,padx=16,pady=20)
root.mainloop()