from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import time
import textwrap
from fpdf import FPDF
import os
import pymysql

def costofItem():
    global priceofdesserts, priceofFood, priceofDrinks

    if e_chapati.get()==" " or e_chips.get()==" " or e_biryani.get()==" " or e_pizza.get() == " " or e_ugali.get()==" " or e_shawarma.get()==" " or e_bhajia.get()==" " or\
            e_rice.get()==" " or e_chicken.get() == " " or e_water.get()==" " or e_coffee.get()==" " or e_tea.get()==" " or e_icedtea.get()==" " or\
            e_orangejuice.get()==" " or e_applejuice.get()==" " or e_cocktailjuice.get()==" " or e_soda.get()==" " or e_madafus.get()==" " or e_icecream.get()==" " or e_cheesecake.get() == " " or\
            e_chocolatecake.get()==" " or e_vanillacake.get()==" " or e_blackforestcake.get()==" " or e_brownie.get()==" " or e_bananabread.get()==" " or e_strawberrytart.get()==" " or e_applepie.get()==" " :
        #if the checkbox is selected but no figure has been given in the entry field, then this error will show.
        messagebox.showerror("Error", "No Quantity is selected.")

    else:

        if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or\
        var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or var11.get()!=0 or var12.get()!=0 or\
        var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or\
        var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or\
        var25.get()!=0 or var26.get()!=0 or var27.get()!=0 :

        #if the values entered are not zero then carry out the function.

            item1=int(e_chapati.get())
            item2=int(e_chips.get())
            item3 = int(e_biryani.get())
            item4 = int(e_pizza.get())
            item5 = int(e_ugali.get())
            item6 = int(e_shawarma.get())
            item7 = int(e_bhajia.get())
            item8 = int(e_rice.get())
            item9 = int(e_chicken.get())

            item10 = int(e_water.get())
            item11 = int(e_coffee.get())
            item12 = int(e_tea.get())
            item13 = int(e_icedtea.get())
            item14 = int(e_orangejuice.get())
            item15 = int(e_applejuice.get())
            item16 = int(e_cocktailjuice.get())
            item17 = int(e_soda.get())
            item18 = int(e_madafus.get())

            item19 = int(e_icecream.get())
            item20 = int(e_cheesecake.get())
            item21 = int(e_chocolatecake.get())
            item22 = int(e_vanillacake.get())
            item23 = int(e_blackforestcake.get())
            item24 = int(e_brownie.get())
            item25 = int(e_bananabread.get())
            item26 = int(e_strawberrytart.get())
            item27 = int(e_applepie.get())

            priceofFood=(item1*10)+(item2*100)+(item3*250)+(item4*500)+(item5*50)+(item6*150)+(item7*150)+(item8*100)+(item9*200)
            priceofDrinks=(item10*50)+(item11*150)+(item12*100)+(item13*150)+(item14*60)+(item15*60)+(item16*100)+(item17*70)+(item18*70)
            priceofdesserts=(item19*100)+(item20*300)+(item21*250)+(item22*200)+(item23*350)+(item24*150)+(item25*200)+(item26*300)+(item27*300)

            costoffoodvar.set(priceofFood)
            costofdrinksvar.set(priceofDrinks)
            costofdessertsvar.set(priceofdesserts)

            subtotalofitems=priceofFood+priceofDrinks+priceofdesserts
            subtotal.set(str(subtotalofitems))

            servicecharge.set("100")

            tc=subtotalofitems+100
            totalcost.set(str(tc))

        else:
            messagebox.showerror("Error", "No item is selected")



def chapati():
    if var1.get()==1:
        textchapati.config(state=NORMAL)
        textchapati.focus() #cursor starts blinking
        textchapati.delete(0, END)
    elif var1.get()==0:
        textchapati.config(state=DISABLED)
        e_chapati.set("0")

def chips():
    if var2.get()==1:
        textchips.config(state=NORMAL)
        textchips.focus() #cursor starts blinking
        textchips.delete(0, END)
    elif var2.get()==0:
        textchips.config(state=DISABLED)
        e_chips.set("0")

def biryani():
    if var3.get()==1:
        textbiryani.config(state=NORMAL)
        textbiryani.focus() #cursor starts blinking
        textbiryani.delete(0, END)
    elif var3.get()==0:
        textbiryani.config(state=DISABLED)
        e_biryani.set("0")

def pizza():
    if var4.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.focus() #cursor starts blinking
        textpizza.delete(0, END)
    elif var4.get()==0:
        textpizza.config(state=DISABLED)
        e_pizza.set("0")

def ugali():
    if var5.get()==1:
        textugali.config(state=NORMAL)
        textugali.focus() #cursor starts blinking
        textugali.delete(0, END)
    elif var5.get()==0:
        textugali.config(state=DISABLED)
        e_ugali.set("0")

def shawarma():
    if var6.get()==1:
        textshawarma.config(state=NORMAL)
        textshawarma.focus() #cursor starts blinking
        textshawarma.delete(0, END)
    elif var6.get()==0:
        textshawarma.config(state=DISABLED)
        e_shawarma.set("0")

def bhajia():
    if var7.get()==1:
        textbhajia.config(state=NORMAL)
        textbhajia.focus() #cursor starts blinking
        textbhajia.delete(0, END)
    elif var7.get()==0:
        textbhajia.config(state=DISABLED)
        e_bhajia.set("0")

def rice():
    if var8.get()==1:
        textrice.config(state=NORMAL)
        textrice.focus() #cursor starts blinking
        textrice.delete(0, END)
    elif var8.get()==0:
        textrice.config(state=DISABLED)
        e_rice.set("0")

def chicken():
    if var9.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.focus() #cursor starts blinking
        textchicken.delete(0, END)
    elif var9.get()==0:
        textchicken.config(state=DISABLED)
        e_chicken.set("0")

def water():
    if var10.get()==1:
        textwater.config(state=NORMAL)
        textwater.focus() #cursor starts blinking
        textwater.delete(0, END)
    elif var10.get()==0:
        textwater.config(state=DISABLED)
        e_water.set("0")


def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()  # cursor starts blinking
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set("0")


def tea():
    if var12.get()==1:
        texttea.config(state=NORMAL)
        texttea.focus()  # cursor starts blinking
        texttea.delete(0, END)
    elif var12.get() == 0:
        texttea.config(state=DISABLED)
        e_tea.set("0")

def icedtea():
    if var13.get()==1:
        texticedtea.config(state=NORMAL)
        texticedtea.focus()  # cursor starts blinking
        texticedtea.delete(0, END)
    elif var13.get() == 0:
        texticedtea.config(state=DISABLED)
        e_icedtea.set("0")

def orangejuice():
    if var14.get()==1:
        textorangejuice.config(state=NORMAL)
        textorangejuice.focus()  # cursor starts blinking
        textorangejuice.delete(0, END)
    elif var14.get() == 0:
        textorangejuice.config(state=DISABLED)
        e_orangejuice.set("0")

def applejuice():
    if var15.get()==1:
        textapplejuice.config(state=NORMAL)
        textapplejuice.focus()  # cursor starts blinking
        textapplejuice.delete(0, END)
    elif var15.get() == 0:
        textapplejuice.config(state=DISABLED)
        e_applejuice.set("0")

def cocktailjuice():
    if var16.get()==1:
        textcocktailjuice.config(state=NORMAL)
        textcocktailjuice.focus()  # cursor starts blinking
        textcocktailjuice.delete(0, END)
    elif var16.get() == 0:
        textcocktailjuice.config(state=DISABLED)
        e_cocktailjuice.set("0")


def soda():
    if var17.get() == 1:
        textsoda.config(state=NORMAL)
        textsoda.focus()  # cursor starts blinking
        textsoda.delete(0, END)
    elif var17.get() == 0:
        textsoda.config(state=DISABLED)
        e_soda.set("0")


def madafus():
    if var18.get() == 1:
        textmadafus.config(state=NORMAL)
        textmadafus.focus()  # cursor starts blinking
        textmadafus.delete(0, END)
    elif var18.get() == 0:
        textmadafus.config(state=DISABLED)
        e_madafus.set("0")


def icecream():
    if var19.get() == 1:
        texticecream.config(state=NORMAL)
        texticecream.focus()  # cursor starts blinking
        texticecream.delete(0, END)
    elif var19.get() == 0:
        texticecream.config(state=DISABLED)
        e_icecream.set("0")


def cheesecake():
    if var20.get() == 1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.focus()  # cursor starts blinking
        textcheesecake.delete(0, END)
    elif var20.get() == 0:
        textcheesecake.config(state=DISABLED)
        e_cheesecake.set("0")


def chocolatecake():
    if var21.get() == 1:
        textchocolatecake.config(state=NORMAL)
        textchocolatecake.focus()  # cursor starts blinking
        textchocolatecake.delete(0, END)
    elif var21.get() == 0:
        textchocolatecake.config(state=DISABLED)
        e_chocolatecake.set("0")


def vanillacake():
    if var22.get() == 1:
        textvanillacake.config(state=NORMAL)
        textvanillacake.focus()  # cursor starts blinking
        textvanillacake.delete(0, END)
    elif var22.get() == 0:
        textvanillacake.config(state=DISABLED)
        e_vanillacake.set("0")


def blackforestcake():
    if var23.get() == 1:
        textblackforestcake.config(state=NORMAL)
        textblackforestcake.focus()  # cursor starts blinking
        textblackforestcake.delete(0, END)
    elif var23.get() == 0:
        textblackforestcake.config(state=DISABLED)
        e_blackforestcake.set("0")

def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()  # cursor starts blinking
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set("0")

def bananabread():
    if var25.get() == 1:
        textbananabread.config(state=NORMAL)
        textbananabread.focus()  # cursor starts blinking
        textbananabread.delete(0, END)
    elif var25.get() == 0:
        textbananabread.config(state=DISABLED)
        e_bananabread.set("0")

def strawberrytart():
    if var26.get() == 1:
        textstrawberrytart.config(state=NORMAL)
        textstrawberrytart.focus()  # cursor starts blinking
        textstrawberrytart.delete(0, END)
    elif var26.get() == 0:
        textstrawberrytart.config(state=DISABLED)
        e_strawberrytart.set("0")

def applepie():
    if var27.get() == 1:
        textapplepie.config(state=NORMAL)
        textapplepie.focus()  # cursor starts blinking
        textapplepie.delete(0, END)
    elif var27.get() == 0:
        textapplepie.config(state=DISABLED)
        e_applepie.set("0")



def receipt():
    global date, x
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or \
            var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
            var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or \
            var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
            var25.get() != 0 or var26.get() != 0 or var27.get() != 0:

        if costoffoodvar.get()!="" or costofdrinksvar.get()!="" or costofdessertsvar.get()!="":

            textReceipt.delete(1.0,END)
            x=random.randint(0,100)
            x="BILL"+str(x)
            date=time.strftime("%d/%m/%Y")

            textReceipt.insert(END, "Receipt  Ref:\t\t"+ x + "\t\t" + date + "\n")
            textReceipt.insert(END, "*********************************************************************\n")
            textReceipt.insert(END, "Items: \t\t"+"Cost of Items:\n")
            textReceipt.insert(END, "*********************************************************************\n")

            if e_chapati.get()!="0":
                textReceipt.insert(END, f"Chapati:\t\t{int(e_chapati.get())*10}\n\n")

            if e_chips.get()!="0":
                textReceipt.insert(END, f"Chips:\t\t{int(e_chips.get())*100}\n\n")

            if e_biryani.get()!="0":
                textReceipt.insert(END, f"Biryani:\t\t{int(e_biryani.get())*250}\n\n")

            if e_pizza.get()!="0":
                textReceipt.insert(END, f"Pizza:\t\t{int(e_pizza.get())*500}\n\n")

            if e_ugali.get()!="0":
                textReceipt.insert(END, f"Ugali:\t\t{int(e_ugali.get())*50}\n\n")

            if e_shawarma.get()!="0":
                textReceipt.insert(END, f"Shawarma:\t\t{int(e_shawarma.get())*150}\n\n")

            if e_bhajia.get()!="0":
                textReceipt.insert(END, f"Bhajia:\t\t{int(e_bhajia.get())*150}\n\n")

            if e_rice.get()!="0":
                textReceipt.insert(END, f"rice:\t\t{int(e_rice.get())*100}\n\n")

            if e_chicken.get()!="0":
                textReceipt.insert(END, f"Chicken:\t\t{int(e_chicken.get())*200}\n\n")

            if e_water.get()!="0":
                textReceipt.insert(END, f"Water:\t\t{int(e_water.get())*50}\n\n")

            if e_coffee.get()!="0":
                textReceipt.insert(END, f"Coffee:\t\t{int(e_coffee.get())*150}\n\n")

            if e_tea.get()!="0":
                textReceipt.insert(END, f"Tea:\t\t{int(e_tea.get())*100}\n\n")

            if e_icedtea.get()!="0":
                textReceipt.insert(END, f"Iced tea:\t\t{int(e_icedtea.get())*150}\n\n")

            if e_orangejuice.get()!="0":
                textReceipt.insert(END, f"Orange juice:\t\t{int(e_orangejuice.get())*60}\n\n")

            if e_applejuice.get()!="0":
                textReceipt.insert(END, f"Apple juice:\t\t{int(e_applejuice.get())*60}\n\n")

            if e_cocktailjuice.get()!="0":
                textReceipt.insert(END, f"Cocktail juice:\t\t{int(e_cocktailjuice.get())*100}\n\n")

            if e_soda.get()!="0":
                textReceipt.insert(END, f"Soda:\t\t{int(e_soda.get())*70}\n\n")

            if e_madafus.get()!="0":
                textReceipt.insert(END, f"Madafu:\t\t{int(e_madafus.get())*70}\n\n")

            if e_icecream.get()!="0":
                textReceipt.insert(END, f"Ice cream:\t\t{int(e_icecream.get())*100}\n\n")

            if e_cheesecake.get()!="0":
                textReceipt.insert(END, f"Cheesecake:\t\t{int(e_cheesecake.get())*300}\n\n")

            if e_chocolatecake.get()!="0":
                textReceipt.insert(END, f"Chocolate cake:\t\t{int(e_chocolatecake.get())*250}\n\n")

            if e_vanillacake.get()!="0":
                textReceipt.insert(END, f"Vanilla cake:\t\t{int(e_vanillacake.get())*200}\n\n")

            if e_blackforestcake.get()!="0":
                textReceipt.insert(END, f"Blackforest cake:\t\t{int(e_blackforestcake.get())*350}\n\n")

            if e_brownie.get()!="0":
                textReceipt.insert(END, f"Brownie:\t\t{int(e_brownie.get())*150}\n\n")

            if e_bananabread.get()!="0":
                textReceipt.insert(END, f"banana bread:\t\t{int(e_bananabread.get())*200}\n\n")

            if e_strawberrytart.get()!="0":
                textReceipt.insert(END, f"strawberry tart:\t\t{int(e_strawberrytart.get())*300}\n\n")

            if e_applepie.get()!="0":
                textReceipt.insert(END, f"apple pie:\t\t{int(e_applepie.get())*300}\n\n")

            textReceipt.insert(END, "*********************************************************************\n")

            if costoffoodvar.get()!="0":
                textReceipt.insert(END, f"Cost of Food: \t\t{priceofFood}\n\n")
            if costofdrinksvar.get() != "0":
                textReceipt.insert(END, f"Cost of Drinks: \t\t{priceofDrinks}\n\n")
            if costofdessertsvar.get() != "0":
                textReceipt.insert(END, f"Cost of Desserts: \t\t{priceofdesserts}\n\n")

            textReceipt.insert(END, "*********************************************************************\n")

            textReceipt.insert(END, f"Sub Total:\t\t{priceofFood+priceofDrinks+priceofdesserts}\n\n")
            textReceipt.insert(END, f"Service Charge:\t\t{100}\n\n")

            textReceipt.insert(END, "*********************************************************************\n")

            textReceipt.insert(END, f"Total:\t\t{priceofFood + priceofDrinks + priceofdesserts+100}\n\n")

            textReceipt.insert(END, "*********************************************************************\n")

    else:
        messagebox.showerror("Error", "No Item selected")

def print():
    if textReceipt.get(1.0, END)!="\n":

        url=filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", ".txt"),("All Files", "*.*")))
        if url == None:
            return
        bill_data=textReceipt.get(1.0, END)
        url.write(bill_data)
        url.close()
        os.startfile(url)

        messagebox.showinfo("Information", "Your Bill is saved successfully")

    else:
        messagebox.showerror("Error", "Enter Order")

def save():
    global date, x
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or \
            var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
            var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or \
            var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
            var25.get() != 0 or var26.get() != 0 or var27.get() != 0:


        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="restaurant")
            cur = con.cursor()
            cur.execute("insert into orders values (%s,%s,%s,%s,%s,%s)",
                        (x,
                         date,
                         priceofFood + priceofDrinks + priceofdesserts + 100,
                         priceofFood,
                         priceofDrinks,
                         priceofdesserts,
                         ))
            con.commit()
            messagebox.showinfo("Success", "Successfully saved order in database")
            if costoffoodvar.get() != 0:
                cur.execute("insert into foodorders values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (x,
                             date,
                             priceofFood,
                             e_chapati.get(),
                             e_chips.get(),
                             e_biryani.get(),
                             e_pizza.get(),
                             e_ugali.get(),
                             e_shawarma.get(),
                             e_bhajia.get(),
                             e_rice.get(),
                             e_chicken.get()
                             ))
                con.commit()


            if costofdrinksvar.get() != 0:
                cur.execute("insert into drinkorders values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (x,
                             date,
                             priceofDrinks,
                             e_water.get(),
                             e_coffee.get(),
                             e_tea.get(),
                             e_icedtea.get(),
                             e_orangejuice.get(),
                             e_applejuice.get(),
                             e_cocktailjuice.get(),
                             e_soda.get(),
                             e_madafus.get()
                             ))
                con.commit()


            if costofdessertsvar.get() != 0:
                cur.execute("insert into dessertorders values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (x,
                             date,
                             priceofdesserts,
                             e_icecream.get(),
                             e_cheesecake.get(),
                             e_chocolatecake.get(),
                             e_vanillacake.get(),
                             e_blackforestcake.get(),
                             e_brownie.get(),
                             e_bananabread.get(),
                             e_strawberrytart.get(),
                             e_applepie.get()
                             ))
                con.commit()
                con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)} ", parent=root)

    else:
        messagebox.showerror("Error", "Enter Order")


def reset():
    e_chapati.set("0")
    e_chips.set("0")
    e_pizza.set("0")
    e_biryani.set("0")
    e_ugali.set("0")
    e_shawarma.set("0")
    e_bhajia.set("0")
    e_chicken.set("0")
    e_rice.set("0")

    e_water.set("0")
    e_coffee.set("0")
    e_tea.set("0")
    e_applejuice.set("0")
    e_icedtea.set("0")
    e_orangejuice.set("0")
    e_cocktailjuice.set("0")
    e_soda.set("0")
    e_madafus.set("0")

    e_icecream.set("0")
    e_cheesecake.set("0")
    e_chocolatecake.set("0")
    e_vanillacake.set("0")
    e_blackforestcake.set("0")
    e_brownie.set("0")
    e_bananabread.set("0")
    e_strawberrytart.set("0")
    e_applepie.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    textchapati.config(state=DISABLED)
    textchips.config(state=DISABLED)
    textbiryani.config(state=DISABLED)
    textpizza.config(state=DISABLED)
    textugali.config(state=DISABLED)
    textshawarma.config(state=DISABLED)
    textbhajia.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textchicken.config(state=DISABLED)

    textwater.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    texttea.config(state=DISABLED)
    texticedtea.config(state=DISABLED)
    textorangejuice.config(state=DISABLED)
    textapplejuice.config(state=DISABLED)
    textcocktailjuice.config(state=DISABLED)
    textsoda.config(state=DISABLED)
    textmadafus.config(state=DISABLED)

    texticecream.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    textchocolatecake.config(state=DISABLED)
    textvanillacake.config(state=DISABLED)
    textblackforestcake.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textbananabread.config(state=DISABLED)
    textstrawberrytart.config(state=DISABLED)
    textapplepie.config(state=DISABLED)

    costoffoodvar.set("")
    costofdrinksvar.set("")
    costofdessertsvar.set("")
    subtotal.set("")
    servicecharge.set("")
    totalcost.set("")

    textReceipt.delete(1.0, END)


root = Tk()
root.geometry("1350x700+0+0")
root.resizable(0, 0)
root.title("Restaurant order management system by Khudeija Kassam")
root.config(bg="#34bf49")

#NAV BAR
def donothing():
    x = 0

def quit():
    answer = messagebox.askyesno('confirmation','Are you sure that you want to logout?')
    if answer:
        root.destroy()

def about():
    root.destroy()
    import about


def help():
    root.destroy()
    import help

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Print", command=print)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", command=about)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", command=help)


topFrame = Frame(root, bg="#34bf49", bd=10)
topFrame.pack(side=TOP)

labeltitle = Label(topFrame, text="Restaurant Order Management System", bd=9, font=("Arial", 30, "bold"), width=54,bg="#34bf49" )
labeltitle.grid(row=0, column=0)

#FRAMES

receiptcal_frame = Frame(root, bd=15, relief=RAISED, bg="#34bf49")
receiptcal_frame.place(x=870, y=75)

buttonFrame = Frame(receiptcal_frame, bd=3, relief=RAISED, bg="#34bf49")
buttonFrame.pack(side=BOTTOM)

calcFrame = Frame(receiptcal_frame, bd=1, relief=RAISED, bg="#34bf49")
calcFrame.pack(side=TOP)

receiptFrame = Frame(receiptcal_frame, bd=4, relief=RAISED, bg="#34bf49")
receiptFrame.pack(side=BOTTOM)

menuFrame = Frame(root, bd=10, relief=RAISED, bg="#34bf49")
menuFrame.place(x=30, y=75)

costFrame = Frame(menuFrame, bd=4, bg="#34bf49")
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text="Food", font=("arial", 19, "bold"), fg="brown", bg="white", bd=10, relief=RAISED)
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text="Drinks", font=("arial", 19, "bold"), fg="brown", bg="white", bd=10,
                         relief=RAISED)
drinksFrame.pack(side=LEFT)

dessertsFrame = LabelFrame(menuFrame, text="Desserts", font=("arial", 19, "bold"), fg="brown", bg="white", bd=10, relief=RAISED)
dessertsFrame.pack(side=LEFT)

#VARIABLES

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_chips=StringVar()
e_chapati=StringVar()
e_pizza=StringVar()
e_shawarma=StringVar()
e_biryani=StringVar()
e_bhajia=StringVar()
e_ugali=StringVar()
e_chicken=StringVar()
e_rice=StringVar()

e_water=StringVar()
e_coffee=StringVar()
e_tea=StringVar()
e_icedtea=StringVar()
e_applejuice=StringVar()
e_orangejuice=StringVar()
e_cocktailjuice=StringVar()
e_soda=StringVar()
e_madafus=StringVar()

e_icecream=StringVar()
e_cheesecake=StringVar()
e_chocolatecake=StringVar()
e_vanillacake=StringVar()
e_blackforestcake=StringVar()
e_brownie=StringVar()
e_bananabread=StringVar()
e_strawberrytart=StringVar()
e_applepie=StringVar()

dateofOrder = StringVar()
receipt_ref = StringVar()

costoffoodvar = StringVar()
subtotal = StringVar()
totalcost = StringVar()
costofdessertsvar = StringVar()
costofdrinksvar = StringVar()
servicecharge = StringVar()

e_chips .set("0")
e_chapati .set("0")
e_pizza .set("0")
e_biryani .set("0")
e_ugali .set("0")
e_shawarma .set("0")
e_bhajia .set("0")
e_chicken .set("0")
e_rice .set("0")

e_water .set("0")
e_coffee .set("0")
e_tea .set("0")
e_applejuice .set("0")
e_icedtea .set("0")
e_orangejuice .set("0")
e_cocktailjuice .set("0")
e_soda .set("0")
e_madafus .set("0")

e_icecream .set("0")
e_cheesecake .set("0")
e_chocolatecake .set("0")
e_vanillacake .set("0")
e_blackforestcake .set("0")
e_brownie .set("0")
e_bananabread .set("0")
e_strawberrytart .set("0")
e_applepie .set("0")







##FOOD

chapati = Checkbutton(foodFrame, text="Chapati", onvalue=1, variable=var1, offvalue=0, font=("arial", 15, "bold"), bg="white", command=chapati ).grid(row=0,
                                                                                                               column=0, #var1 will store the checkbutton value which will be either 1 when checked or 0 when not.
                                                                                                               sticky=W)  # sticky=W ensures everything sticks to the west side
chips = Checkbutton(foodFrame, text="Chips", onvalue=1, variable=var2, offvalue=0, font=("arial", 15, "bold"), bg="white", command=chips ).grid(row=1,
                                                                                                               column=0,
                                                                                                               sticky=W)
biryani = Checkbutton(foodFrame, text="Biryani", onvalue=1, variable=var3,offvalue=0, font=("arial", 15, "bold"), bg="white", command=biryani ).grid(row=2,
                                                                                                               column=0,
                                                                                                               sticky=W)
pizza = Checkbutton(foodFrame, text="Pizza", onvalue=1,variable=var4, offvalue=0, font=("arial", 15, "bold"), bg="white", command= pizza ).grid(row=3,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
ugali = Checkbutton(foodFrame, text="Ugali", onvalue=1,variable=var5, offvalue=0, font=("arial", 15, "bold"), bg="white", command=ugali ).grid(row=4,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
shawarma = Checkbutton(foodFrame, text="Shawarma", onvalue=1,variable=var6, offvalue=0, font=("arial", 15, "bold"), bg="white", command=shawarma ).grid(
    row=5, column=0, sticky=W)
bhajia = Checkbutton(foodFrame, text="Bhajia", onvalue=1,variable=var7, offvalue=0, font=("arial", 15, "bold"), bg="white", command=bhajia ).grid(
    row=6, column=0, sticky=W)
rice = Checkbutton(foodFrame, text="Rice", onvalue=1,variable=var8, offvalue=0, font=("arial", 15, "bold"), bg="white", command=rice ).grid(
    row=7, column=0, sticky=W)
chicken = Checkbutton(foodFrame, text="Chicken", onvalue=1,variable=var9, offvalue=0, font=("arial", 15, "bold"), bg="white", command=chicken ).grid(
    row=8, column=0, sticky=W)

# Food entry

textchapati = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6, textvariable=e_chapati, state=DISABLED)
textchapati.grid(row=0, column=1)

textchips = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6, textvariable=e_chips ,state=DISABLED)
textchips.grid(row=1, column=1)

textbiryani = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_biryani ,state=DISABLED)
textbiryani.grid(row=2, column=1)

textpizza = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_pizza ,state=DISABLED)
textpizza.grid(row=3, column=1)

textugali = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_ugali ,state=DISABLED)
textugali.grid(row=4, column=1)

textshawarma = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_shawarma ,state=DISABLED)
textshawarma.grid(row=5, column=1)

textbhajia = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_bhajia , state=DISABLED)
textbhajia.grid(row=6, column=1)

textrice = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_rice , state=DISABLED)
textrice.grid(row=7, column=1)

textchicken = Entry(foodFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_chicken , state=DISABLED)
textchicken.grid(row=8, column=1)

# DRINKS
water = Checkbutton(drinksFrame, text="Water", onvalue=1, variable=var10,offvalue=0, font=("arial", 15, "bold"), bg="white", command=water ).grid(
    row=0, column=0, sticky=W)
coffee = Checkbutton(drinksFrame, text="Coffee", onvalue=1,variable=var11, offvalue=0, font=("arial", 15, "bold"), bg="white", command=coffee ).grid(
    row=1, column=0, sticky=W)
tea = Checkbutton(drinksFrame, text="Tea", onvalue=1,variable=var12, offvalue=0, font=("arial", 15, "bold"), bg="white", command=tea ).grid(
    row=2, column=0, sticky=W)
icedtea = Checkbutton(drinksFrame, text="Iced tea", onvalue=1,variable=var13, offvalue=0, font=("arial", 15, "bold"),
                       bg="white", command=icedtea ).grid(row=3, column=0, sticky=W)
orangejuice = Checkbutton(drinksFrame, text="Orange juice", onvalue=1,variable=var14, offvalue=0, font=("arial", 15, "bold"),
                       bg="white", command=orangejuice ).grid(row=4, column=0, sticky=W)
applejuice = Checkbutton(drinksFrame, text="Apple juice", onvalue=1,variable=var15, offvalue=0, font=("arial", 15, "bold"),
                       bg="white", command=applejuice ).grid(row=5, column=0, sticky=W)
cocktailjuice = Checkbutton(drinksFrame, text="Cocktail juice", onvalue=1,variable=var16, offvalue=0, font=("arial", 15, "bold"),
                        bg="white", command=cocktailjuice ).grid(row=6, column=0, sticky=W)
soda = Checkbutton(drinksFrame, text="Soda", onvalue=1,variable=var17, offvalue=0, font=("arial", 15, "bold"),
                        bg="white", command=soda ).grid(row=7, column=0, sticky=W)
madafu = Checkbutton(drinksFrame, text="Madafu", onvalue=1,variable=var18, offvalue=0, font=("arial", 15, "bold"),
                        bg="white", command=madafus ).grid(row=8, column=0, sticky=W)

# DRINKS ENTRY
textwater = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6, textvariable=e_water , state=DISABLED)
textwater.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_coffee  ,state=DISABLED)
textcoffee.grid(row=1, column=1)

texttea = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_tea  ,state=DISABLED)
texttea.grid(row=2, column=1)

texticedtea = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_icedtea  ,state=DISABLED)
texticedtea.grid(row=3, column=1)

textorangejuice = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_orangejuice  ,state=DISABLED)
textorangejuice.grid(row=4, column=1)

textapplejuice = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_applejuice  ,state=DISABLED)
textapplejuice.grid(row=5, column=1)

textcocktailjuice = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_cocktailjuice  ,state=DISABLED)
textcocktailjuice.grid(row=6, column=1)

textsoda = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_soda  ,state=DISABLED)
textsoda.grid(row=7, column=1)

textmadafus = Entry(drinksFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_madafus , state=DISABLED)
textmadafus.grid(row=8, column=1)

# desserts
icecream = Checkbutton(dessertsFrame, text="Ice cream", onvalue=1,variable=var19, offvalue=0, font=("arial", 15, "bold"), bg="white", command=icecream ).grid(
    row=0, column=0, sticky=W)
cheesecake = Checkbutton(dessertsFrame, text="Cheesecake", onvalue=1,variable=var20, offvalue=0, font=("arial", 15, "bold"), bg="white", command=cheesecake ).grid(
    row=1, column=0, sticky=W)
chocolatecake = Checkbutton(dessertsFrame, text="Chocolate cake", onvalue=1,variable=var21, offvalue=0, font=("arial", 15, "bold"), bg="white", command=chocolatecake ).grid(
    row=2, column=0, sticky=W)
vanillacake = Checkbutton(dessertsFrame, text="Vanilla cake", onvalue=1,variable=var22, offvalue=0, font=("arial", 15, "bold"),
                          bg="white", command=vanillacake ).grid(row=3, column=0, sticky=W)
blackforestcake = Checkbutton(dessertsFrame, text="Blackforest", onvalue=1,variable=var23, offvalue=0, font=("arial", 15, "bold"), bg="white", command=blackforestcake ).grid(
    row=4, column=0, sticky=W)
browniecake = Checkbutton(dessertsFrame, text="Brownie", onvalue=1,variable=var24, offvalue=0, font=("arial", 15, "bold"),
                          bg="white", command=brownie ).grid(row=5, column=0, sticky=W)
bananabread = Checkbutton(dessertsFrame, text="Banana bread", onvalue=1, variable=var25,offvalue=0, font=("arial", 15, "bold"),
                            bg="white", command=bananabread ).grid(row=6, column=0, sticky=W)
strawberrytart = Checkbutton(dessertsFrame, text="Strawberry tart", onvalue=1,variable=var26, offvalue=0, font=("arial", 15, "bold"),
                            bg="white", command=strawberrytart ).grid(row=7, column=0, sticky=W)
applepie = Checkbutton(dessertsFrame, text="Apple pie", onvalue=1,variable=var27, offvalue=0, font=("arial", 15, "bold"),
                              bg="white", command=applepie ).grid(row=8, column=0, sticky=W)

# desserts ENTRY

texticecream = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_icecream  ,state=DISABLED)
texticecream.grid(row=0, column=1)

textcheesecake = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_cheesecake  ,state=DISABLED)
textcheesecake.grid(row=1, column=1)

textchocolatecake = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_chocolatecake  ,state=DISABLED)
textchocolatecake.grid(row=2, column=1)


textvanillacake = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_vanillacake  ,state=DISABLED)
textvanillacake.grid(row=3, column=1)

textblackforestcake = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_blackforestcake  ,state=DISABLED)
textblackforestcake.grid(row=4, column=1)

textbrownie = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_brownie  ,state=DISABLED)
textbrownie.grid(row=5, column=1)

textbananabread = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_bananabread  ,state=DISABLED)
textbananabread.grid(row=6, column=1)

textstrawberrytart = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_strawberrytart  ,state=DISABLED)
textstrawberrytart.grid(row=7, column=1)

textapplepie = Entry(dessertsFrame, font=("arial", 15, "bold"), bd=10, width=6,textvariable=e_applepie  ,state=DISABLED)
textapplepie.grid(row=8, column=1)

# COST LABELS

labelCostfood = Label(costFrame, font=("arial", 16, "bold"), text="Cost of Food\t", bg="#34bf49", fg="white",
                      justify=CENTER)  # \t puts in space between the label and entry
labelCostfood.grid(row=0, column=0, sticky=W)

textcostfood = Entry(costFrame, font=("arial", 16, "bold"), textvariable=costoffoodvar, bd=7, bg="white", width=14, justify=RIGHT, state="readonly")
textcostfood.grid(row=0, column=1)  # delete and insert can be possible with readonly but changes wont be made

labelCostdrinks = Label(costFrame, font=("arial", 16, "bold"), text="Cost of Drinks\t", bg="#34bf49", fg="white",
                        justify=CENTER)
labelCostdrinks.grid(row=1, column=0, sticky=W)

textcostdrinks = Entry(costFrame, font=("arial", 16, "bold"), textvariable=costofdrinksvar, bd=7, bg="white", width=14, justify=RIGHT,
                       state="readonly")
textcostdrinks.grid(row=1, column=1)

labelCostdesserts = Label(costFrame, font=("arial", 16, "bold"), text="Cost of Desserts\t", bg="#34bf49", fg="white",
                       justify=CENTER)
labelCostdesserts.grid(row=2, column=0, sticky=W)

textcostdesserts = Entry(costFrame, font=("arial", 16, "bold"), textvariable=costofdessertsvar, bd=7, bg="white", width=14, justify=RIGHT,
                      state="readonly")
textcostdesserts.grid(row=2, column=1)

labelSubtotal = Label(costFrame, font=("arial", 16, "bold"), text="   Sub Total\t", bg="#34bf49", fg="white",
                      justify=CENTER)
labelSubtotal.grid(row=0, column=2, sticky=W)

textsubtotal = Entry(costFrame, font=("arial", 16, "bold"), textvariable=subtotal, bd=7, bg="white", width=14, justify=RIGHT, state="readonly")
textsubtotal.grid(row=0, column=3)

labelServicecharge = Label(costFrame, font=("arial", 16, "bold"), text="   Service Charge\t", bg="#34bf49", fg="white",
                           justify=CENTER)
labelServicecharge.grid(row=1, column=2, sticky=W)

textservicecharge = Entry(costFrame, font=("arial", 16, "bold"), textvariable=servicecharge, bd=7, bg="white", width=14, justify=RIGHT,
                          state="readonly")
textservicecharge.grid(row=1, column=3)

labelTotalcost = Label(costFrame, font=("arial", 16, "bold"), text="   Total Cost\t", bg="#34bf49", fg="white",
                       justify=CENTER)
labelTotalcost.grid(row=2, column=2, sticky=W)

texttotalcost = Entry(costFrame, font=("arial", 16, "bold"), textvariable=totalcost, bd=7, bg="white", width=14, justify=RIGHT,
                      state="readonly")
texttotalcost.grid(row=2, column=3)

buttonTotal = Button(buttonFrame, text="Total", font=("arial", 14, "bold"),  fg="white", bg="#34bf49", padx=16, pady=1,
                     bd=4, width=4, command=costofItem)
buttonTotal.grid(row=0, column=0)

buttonreceipt = Button(buttonFrame, text="Receipt", font=("arial", 14, "bold"), fg="white", bg="#34bf49", padx=16,
                       pady=1, bd=4, width=4, command=receipt)
buttonreceipt.grid(row=0, column=1)

buttonsave = Button(buttonFrame, text="Save", font=("arial", 14, "bold"), fg="white", bg="#34bf49", padx=16, pady=1,
                    bd=4, width=4, command=save)
buttonsave.grid(row=0, column=2)

buttonprint = Button(buttonFrame, text="Print", font=("arial", 14, "bold"), fg="white", bg="#34bf49", padx=16, pady=1,
                    bd=4, width=4, command=print)
buttonprint.grid(row=0, column=3)

buttonreset = Button(buttonFrame, text="Reset", font=("arial", 14, "bold"), fg="white", bg="#34bf49", padx=16, pady=1,
                     bd=4, width=4, command=reset)
buttonreset.grid(row=0, column=4)

# TEXT AREA FOR RECEIPT

textReceipt = Text(receiptFrame, font=("arial", 12, "bold"), bd=4, width=46, height=14)
textReceipt.grid(row=0, column=0)

# CALC  GUI
operator = ""


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    textDisplay.delete(0, END)
    textDisplay.insert(END, operator)


def btnClear():
    global operator
    operator = ""
    textDisplay.delete(0, END)


def btnAns():
    global operator
    if operator==" ":
        pass
    else:
        sum = str(eval(operator))  # eval is short for evaluate.
        textDisplay.delete(0, END)  # to delete the previous input
        textDisplay.insert(0, sum)
        operator = ""  # to delete the previous input


textDisplay = Entry(calcFrame, width=35, bg="white", bd=4, font=("arial", 16, "bold"), justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan=4, pady=1)
textDisplay.insert(0, "0")

button7 = Button(calcFrame, text="7", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(7))
button7.grid(row=1, column=0)

button8 = Button(calcFrame, text="8", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(8))
button8.grid(row=1, column=1)

button9 = Button(calcFrame, text="9", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(9))
button9.grid(row=1, column=2)

buttonadd = Button(calcFrame, text="+", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                   width=4,
                   command=lambda: btnClick("+"))
buttonadd.grid(row=1, column=3)

button4 = Button(calcFrame, text="4", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(4))
button4.grid(row=2, column=0)

button5 = Button(calcFrame, text="5", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(5))
button5.grid(row=2, column=1)

button6 = Button(calcFrame, text="6", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(6))
button6.grid(row=2, column=2)

buttonsub = Button(calcFrame, text="-", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                   width=4,
                   command=lambda: btnClick("-"))
buttonsub.grid(row=2, column=3)

button1 = Button(calcFrame, text="1", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(1))
button1.grid(row=3, column=0)

button2 = Button(calcFrame, text="2", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(2))
button2.grid(row=3, column=1)

button3 = Button(calcFrame, text="3", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(3))
button3.grid(row=3, column=2)

buttonmult = Button(calcFrame, text="*", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                    width=4,
                    command=lambda: btnClick("*"))
buttonmult.grid(row=3, column=3)

buttonans = Button(calcFrame, text="Ans", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                   width=4,
                   command=btnAns)
buttonans.grid(row=4, column=0)

buttonclear = Button(calcFrame, text="Clear", fg="black", bg="#34bf49", bd=7, padx=16, pady=1,
                     font=("arial", 16, "bold"), width=4
                     , command=btnClear)
buttonclear.grid(row=4, column=1)

button0 = Button(calcFrame, text="0", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                 width=4,
                 command=lambda: btnClick(0))
button0.grid(row=4, column=2)

buttondiv = Button(calcFrame, text="/", fg="black", bg="#34bf49", bd=7, padx=16, pady=1, font=("arial", 16, "bold"),
                   width=4,
                   command=lambda: btnClick("/"))
buttondiv.grid(row=4, column=3)

root.config(menu=menubar)
menubar = Menu(root)
root.mainloop()
