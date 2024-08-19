import customtkinter as ctk
from PIL import Image 
from tkinter import messagebox
import os

    
root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.resizable(False,False)
root.title("CIRCLY BANK")
root.iconbitmap("WS.ico")

root.geometry("1300x700")

def Registor():
    root.withdraw()
    A = ctk.CTkToplevel(root)
    A.geometry("1000x700")
    A.title("CIRCLY BANK: Registrasiýa")
    A.resizable(False,False)
    A.iconbitmap("WS.ico")
    #==================================================================
    temp_name       = ctk.StringVar()
    temp_surname    = ctk.StringVar()
    temp_age        = ctk.StringVar()
    temp_password   = ctk.StringVar()
    #==================================================================
    registor1 = ctk.CTkFrame(master=A)
    registor1.pack(expand=True, fill="both")

    arka_fon = Image.open("registor_page.jpg")
    arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(1000,700))

    label_arka_fon = ctk.CTkLabel(master=registor1,image=arka_fon,text="")
    label_arka_fon.place(relheight=1,relwidth=1)
    font1= ctk.CTkFont(family=("Century Gothic"),size=30,weight="bold")
    #==================================================================
    frame2 = ctk.CTkFrame(master=registor1,width=380,height=400,fg_color="white")
    frame2.pack(padx=130,side="left")
        
    label1 = ctk.CTkLabel(master=frame2,text="REGISTRASIYA",font=font1,text_color="black")
    label1.place(relx=0.25,rely=0.1)
    #==================================================================
    font2 = ctk.CTkFont(family=("timer"),size=15)
    font3 = ctk.CTkFont(family=("Century Gothic"),size=12,weight="bold")
    #==================================================================
    name = ctk.CTkLabel(master=frame2,text_color="#3DCDFF",font=font2,text="Ulanyjynyň ady")
    name.place(relx=0.05,rely=0.24)

    name_entry=ctk.CTkEntry(master=frame2,fg_color="white",corner_radius=100,
                                width=300,placeholder_text="Mekan",text_color="black",textvariable=temp_name)
    name_entry.place(relx=0.03,rely=0.3)
    #==================================================================
    surname = ctk.CTkLabel(master=frame2,text_color="#3DCDFF",font=font2,text="Ulanyjynyň Familýasy")
    surname.place(relx=0.05,rely=0.4)

    surname_entry=ctk.CTkEntry(master=frame2,fg_color="white",corner_radius=100,
                                    width=300,placeholder_text="Gurbandurdy",text_color="black",textvariable=temp_surname)
    surname_entry.place(relx=0.03,rely=0.47)
    #==================================================================
    age = ctk.CTkLabel(master=frame2,text_color="#3DCDFF",font=font2,text="Ulanyjynyň Ýaşy")
    age.place(relx=0.05,rely=0.57)

    age_entry=ctk.CTkEntry(master=frame2,fg_color="white",corner_radius=100,
                                width=300,placeholder_text="18",text_color="black",textvariable=temp_age)
    age_entry.place(relx=0.03,rely=0.65)


    pasword = ctk.CTkLabel(master=frame2,text_color="#3DCDFF",font=font2,text="Ulanyjynyň Kody")
    pasword.place(relx=0.03,rely=0.73)
    #==================================================================
    name = ""
    surname = ""
    age = ""
    password = ""
    font4 = ctk.CTkFont(family=("timer"),size=10)
    B = ctk.BooleanVar()
    def dana():
        #global B
        get_status = B.get() # B-nin icindaki bilgini al
        if(get_status==True):
            pasword_entry.configure(show="")
        elif(get_status==False):
            pasword_entry.configure(show="#")

    checkbox = ctk.CTkCheckBox(master=frame2,command=dana,text="Aç",
                                width=20,height=30,fg_color="orange",border_width=1,border_color="black",
                                text_color="black",hover_color="#3DCDFF",font=font4,variable=B)          
    checkbox.place(relx=0.85,rely=0.8)
    #==================================================================
    pasword_entry=ctk.CTkEntry(master=frame2,fg_color="white",corner_radius=100,
                                    width=300,placeholder_text="1234",show="#",text_color="black",textvariable=temp_password)
    pasword_entry.place(relx=0.03,rely=0.8)
    def finish_reg():
        name = temp_name.get()
        surname = temp_surname.get()
        age = temp_age.get()
        password = temp_password.get()
        all_accounts = os.listdir()

        if name == "" or surname == "" or age == "" or password == "":
            #notif.config(fg="red",text="All fields requried * ")
            print = ("mlds22")
            return

        for name_check in all_accounts:
            if name == name_check :
                #notif.config(fg="red",text="Account already exists")
                messagebox.showerror("YALNYSLYK BAR", "Sizin beren danylarynyza gora hasb doredilen oz hasabynyza girmeginizi maslahat beryaris.")
                print ("mlds")
                return
            else:
                new_file = open(name,"w")
                new_file.write('-------------------------'+"\n")
                new_file.write(name+'\n')
                new_file.write(surname+'\n')
                new_file.write(age+'\n')
                new_file.write(password+'\n')
                new_file.write('0'+"\n")
                #new_file.write('0'+"\n")
                new_file.write('-------------------------'+"\n")
                new_file.close()
        A.destroy()
        Login()
    #==================================================================
    def yza ():
        root.deiconify()
        A.destroy()
        
    #==================================================================
    font3 = ctk.CTkFont(family=("Century Gothic"),size=12,weight="bold")

    btn1 = ctk.CTkButton(master=frame2,text="Yza",font=font3,fg_color="#3DCDFF",text_color="black",command=yza)
    btn1.place(relx=0.1,rely=0.9)

    btn2 = ctk.CTkButton(master=frame2,text="Dowam et",font=font3,fg_color="#3DCDFF",text_color="black",command=finish_reg)
    btn2.place(relx=0.5,rely=0.9)

    #==================================================================================================
    def get_name(event):
        global name
        #---------------------------------
        name = name_entry.get()
        #---------------------------------
        if(not name):
            messagebox.showerror("YALNYSLYK BAR", "Adynyzy yazyn")
            return
        #---------------------------------
        surname_entry.focus()
    # ==================================================================================================
    name_entry.bind("<Return>", get_name)
    # ==================================================================================================
    def get_surname(event):
        global surname
        #---------------------------------
        surname = surname_entry.get()
        #---------------------------------
        if(not surname):
            messagebox.showerror("YALNYSLYK BAR", "Familyanyzy yazyn")
            return
        #---------------------------------
        age_entry.focus()
        #---------------------------------
    surname_entry.bind("<Return>", get_surname)
    # ==================================================================================================
    def get_age(event):
        global age
        #---------------------------------
        age = age_entry.get()
        #---------------------------------
        if(not age):
            messagebox.showerror("YALNYSLYK BAR", "Yasynyzy yazyn")
            return
        #---------------------------------
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("YALNYSLYK BAR", "Yasynyzy san bilen yazyn!")
            return
        #---------------------------------
        pasword_entry.focus()
    age_entry.bind("<Return>", get_age)
    # ==================================================================================================
    def get_password(event):
        global password
        #---------------------------------
        password = pasword_entry.get()
        #---------------------------------
        if(not password):
            messagebox.showerror("YALNYSLYK BAR", "Koynyzy bellan")
            return
        #---------------------------------
        btn2.focus()
    # ==================================================================================================
    pasword_entry.bind("<Return>", get_password)
#---------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

def Login():
    root.withdraw()
    B = ctk.CTkToplevel(root)
    B.geometry("1000x700")
    B.title("CIRCLY BANK: Login")
    B.resizable(False,False)
    B.iconbitmap("WS.ico")
    #==================================================================
    global temp_login_name
    global temp_login_password
    
    temp_login_name     = ctk.StringVar()
    temp_login_password = ctk.StringVar()
    
    def login_session():
        global login_name
        all_accounts = os.listdir()
        login_name = temp_login_name.get()
        login_password = temp_login_password.get()
#==================================================================
        for name in all_accounts:
            if name == login_name:
                file = open(name,"r")
                file_data = file.read()
                file_data = file_data.split('\n')
                password  = file_data[4]
                file_data = file.close()
                #Account Dashboard
                if login_password == password :
                    B.destroy()
                    print("mlds")
                    D = ctk.CTkToplevel(root)
                    #D._set_appearance_mode("light")
                    D.geometry("1300x700")
                    D.title("CIRCLY BANK:Pofil")
                    D.iconbitmap("WS.ico")
                    D.resizable(False,False)
                    #==================================================================
                    font4 = ctk.CTkFont(family=("timer"),size=10)
            
                    #checkbox.place(side="right")
                    arka_fon = Image.open("w.jpg")
                    arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(600,700))

                    label_arka_fon = ctk.CTkLabel(master=D,image=arka_fon,text="")
                    label_arka_fon.place(relx=0.55,rely=0)
                    
                    
                    frame22 = ctk.CTkFrame(D, width=720, height=700,border_color="red")
                    frame22.place(relx=0, rely=0)
                    
                    #==================================================================
                    font1= ctk.CTkFont(family=("Century Gothic"),size=30,weight="bold")
                    #==================================================================
                    one_frame = ctk.CTkFrame(master=frame22,width=720,height=200)
                    one_frame.place(relx=0)
                    
                    label_hedar = ctk.CTkLabel(master=one_frame,text="HOŞ GELDIŇIZ",font=font1)
                    label_hedar.place(relx=0.35,rely=0.1)
                    #==================================================================
                    font3 = ctk.CTkFont(family=("Century Gothic"),size=12,weight="bold")
                    
                    def user_date():
                        nonlocal font3
                        user_frame = ctk.CTkFrame(master=frame22,width=700,height=500)
                        user_frame.pack(pady=200)
                        
                        arka_fon = Image.open("profil.png")
                        arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(200,200))

                        label_arka_fon = ctk.CTkLabel(master=user_frame,image=arka_fon,text="")
                        label_arka_fon.place(relx=0.05,rely=0.2)

                        file = open(login_name, 'r')
                        file_data = file.read()
                        user_details = file_data.split('\n')
                        details_name = user_details[1]
                        details_surname = user_details[2]
                        details_age = user_details[3]
                        details_balance = user_details[5]
                        #details_usd_balance = user_details[6]

                        
                        font223 = ctk.CTkFont(family=("timer"),size=15,weight="bold")

                        user_label = ctk.CTkLabel(master=user_frame,text="Siziň adyňyz :"+details_name,font=font223)
                        user_label.place(relx=0.4,rely=0.25)

                        user_label1 = ctk.CTkLabel(master=user_frame,text="Siziň familyaňyz :"+details_surname,font=font223)
                        user_label1.place(relx=0.4,rely=0.3)

                        user_label2 = ctk.CTkLabel(master=user_frame,text="Siziň yaşyňyz :"+details_age,font=font223)
                        user_label2.place(relx=0.4,rely=0.35)

                        user_label3 = ctk.CTkLabel(master=user_frame,text="Siziň balansyňyz :"+details_balance,font=font223)
                        user_label3.place(relx=0.4,rely=0.5)

                        #user_label4 = ctk.CTkLabel(master=user_frame,text="Siziň USD balansyňyz :"+details_usd_balance,font=font223)
                        #user_label4.place(relx=0.4,rely=0.55)
                        
                        def exit1 ():
                            user_frame.destroy()
                            D
                        
                        user_btn = ctk.CTkButton(master=user_frame,text="YZA",
                                                 font=font3,fg_color="#3DCDFF",text_color="black",command=exit1)
                        user_btn.place(relx=0.5,rely=0.7)
                    #==================================================================
                    #==================================================================
                    btn = ctk.CTkButton(master= one_frame,text="Hasabyňyz",width=100,height=70,
                                        font=font3,fg_color="#3DCDFF",text_color="black",command=user_date)
                    btn.place(relx=0.05,rely=0.4)
                    #==================================================================
                    def finish_deposit():
                        if amount.get() == "":
                            deposit_notif.configure(text='Saljak puluňyzy ýazyň!',fg_color="red")
                            return
                        if float(amount.get()) <=0:
                            deposit_notif.configure(text='Saljak puluňyz 0 - dan yokary bolmaly', fg_color='red')
                            return

                        file = open(login_name, 'r+')
                        file_data = file.read()
                        details = file_data.split('\n')
                        current_balance = details[5]
                        updated_balance = current_balance
                        updated_balance = float(updated_balance) + float(amount.get())
                        file_data       = file_data.replace(current_balance, str(updated_balance))
                        file.seek(0)
                        #file.truncate(0)
                        file.write(file_data)
                        file.close()

                        label.configure(text="Current Balance : TMT"+str(updated_balance),fg_color="green")
                        deposit_notif.configure(text='Balansyňyza pull gosuldy', fg_color='green')    
                    
                    def user_pul_cekmek():
                        global user_frame2
                        global amount
                        global deposit_notif
                        global label
                        
                        user_frame2 = ctk.CTkFrame(master=frame22,width=700,height=500)
                        user_frame2.pack(pady=200)
                        
                        font11= ctk.CTkFont(family=("Century Gothic"),size=30,weight="bold")
                        
                        amount = ctk.StringVar()
                        file   = open(login_name, "r")
                        file_data = file.read()
                        user_details = file_data.split('\n')
                        details_balance = user_details[5]
                        #==================================================================
                        arka_fon = Image.open("bankamant.jpg")
                        arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(700,500))

                        label_arka_fon = ctk.CTkLabel(master=user_frame2,image=arka_fon,text="")
                        label_arka_fon.place(relheight=1,relwidth=1)
                        
                        label1 = ctk.CTkLabel(master=user_frame2, text='BALANS',font=font11,text_color="green",fg_color="transparent")
                        label1.place(relx=0.4,rely=0.4)
                        
                        label = ctk.CTkLabel(master=user_frame2, text='Sizin sumatky balansynyz : '+details_balance,font=font3,text_color="orange")
                        label.place(relx=0.25,rely=0.5)
                        
                        label2 = ctk.CTkLabel(master=user_frame2, text='Nace TMT gosmak isleyaniz  ',font=font3,text_color="orange")
                        label2.place(relx=0.25,rely=0.57)

                        Entry = ctk.CTkEntry(master=user_frame2, placeholder_text="1234",
                                             font=font3,fg_color="white",text_color="black",textvariable=amount)
                        Entry.place(relx=0.5,rely=0.57)
                        
                        deposit_notif = ctk.CTkLabel(master=user_frame2,text="",font=font3)
                        deposit_notif.place(relx=0.25,rely=0.62)
                        
                        btn_finsh = ctk.CTkButton(master=user_frame2,text="Sal",font=font3,height=70,
                                                  fg_color="#3DCDFF",text_color="black",command=finish_deposit)
                        btn_finsh.place(relx=0.7,rely=0.83)
                        
                        def exit1 ():
                            user_frame2.destroy()
                            D
                        user_btn = ctk.CTkButton(master=user_frame2,text="YZA",height=70,
                                                 font=font3,fg_color="#3DCDFF",text_color="black",command=exit1)
                        user_btn.place(relx=0.1,rely=0.83)
                    #==================================================================
                    def finish_withdraw():
                        if withdraw_amount.get() == "":
                            withdraw_deposit_notif.configure(text='Çekjek pulluňyzy yazyň!',fg_color="red")
                            return
                        if float(withdraw_amount.get()) <=0:
                            withdraw_deposit_notif.configure(text='Çekjek puluňyz 0 dan aşak bolup bilmeyä', fg_color='red')
                            return

                        file = open(login_name, 'r+')
                        file_data = file.read()
                        details = file_data.split('\n')
                        current_balance = details[5]

                        if float(withdraw_amount.get()) >float(current_balance):
                            withdraw_deposit_notif.configure(text='Sizin balansyňyzyň möçberi yeterlik däl!', fg_color='red')
                            return

                        updated_balance = current_balance
                        updated_balance = float(updated_balance) - float(withdraw_amount.get())
                        file_data       = file_data.replace(current_balance, str(updated_balance))
                        file.seek(0)
                        #file.truncate(0)
                        file.write(file_data)
                        file.close()

                        withdraw_label.configure(text="Current Balance : TMT"+str(updated_balance),fg_color="green")
                        withdraw_deposit_notif.configure(text='Balansyňyzdan pul çekildi', fg_color='green')
                    #==================================================================
                    def withdraw():
                        global withdraw_amount
                        global withdraw_deposit_notif
                        global withdraw_label
                        
                        withdraw_user_frame2 = ctk.CTkFrame(master=frame22,width=700,height=500)
                        withdraw_user_frame2.pack(pady=200)
                        
                        font11= ctk.CTkFont(family=("Century Gothic"),size=30,weight="bold")
                        
                        withdraw_amount = ctk.StringVar()
                        file   = open(login_name, "r")
                        file_data = file.read()
                        user_details = file_data.split('\n')
                        details_balance = user_details[5]
                        #==================================================================
                        arka_fon = Image.open("bankamant.jpg")
                        arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(700,500))

                        label_arka_fon = ctk.CTkLabel(master=withdraw_user_frame2,image=arka_fon,text="")
                        label_arka_fon.place(relheight=1,relwidth=1)
                        
                        withdraw_label1 = ctk.CTkLabel(master=withdraw_user_frame2, text='BALANS',font=font11,text_color="green",fg_color="transparent")
                        withdraw_label1.place(relx=0.4,rely=0.4)
                        
                        withdraw_label = ctk.CTkLabel(master=withdraw_user_frame2, text='Sizin sumatky balansynyz : '+details_balance,font=font3,text_color="orange")
                        withdraw_label.place(relx=0.25,rely=0.5)
                        
                        withdraw_label2 = ctk.CTkLabel(master=withdraw_user_frame2, text='Nace TMT çekmek isleyaniz  ',font=font3,text_color="orange")
                        withdraw_label2.place(relx=0.25,rely=0.57)

                        withdraw_Entry = ctk.CTkEntry(master=withdraw_user_frame2, placeholder_text="1234",
                                            font=font3,fg_color="white",text_color="black",textvariable=withdraw_amount)
                        withdraw_Entry.place(relx=0.5,rely=0.57)
                        
                        withdraw_deposit_notif = ctk.CTkLabel(master=withdraw_user_frame2,text="",font=font3)
                        withdraw_deposit_notif.place(relx=0.25,rely=0.62)
                        
                        withdraw_btn_finsh = ctk.CTkButton(master=withdraw_user_frame2,text="Çek",font=font3,height=70,
                                                fg_color="#3DCDFF",text_color="black",command=finish_withdraw)
                        withdraw_btn_finsh.place(relx=0.7,rely=0.83)

                        def exit1 ():
                            withdraw_user_frame2.destroy()
                            D
                        user_btn = ctk.CTkButton(master=withdraw_user_frame2,text="YZA",height=70,
                                                font=font3,fg_color="#3DCDFF",text_color="black",command=exit1)
                        user_btn.place(relx=0.1,rely=0.83)
         
                    def finish_usd():
                        print("2")
                        if usd_amount.get() == "":
                            usd_deposit_notif.configure(text='Obmen etjek pulluňyzy yazyň!',fg_color="red")
                            return
                        if float(usd_amount.get()) <=0:
                            usd_deposit_notif.configure(text='Obmen etjek puluňyz 0 dan aşak bolup bilmeyä', fg_color='red')
                            return

                        file = open(login_name, 'r+')
                        file_data = file.read()
                        details = file_data.split('\n')
                        current_balance = details[5]
                        #usd_balance = details[6]
                        print("3")
                        if float(usd_amount.get()) >float(current_balance):
                            usd_deposit_notif.configure(text='Sizin balansyňyzyň möçberi yeterlik däl!', fg_color='red')
                            print("4")
                            return
                        #elif float(usd_amount.get()) == float(current_balance):
                        updated_balance = current_balance
                        updated_balance = float(updated_balance) - float(usd_amount.get())
                        file_data       = file_data.replace(current_balance, str(updated_balance))
                        kop = float(usd_amount.get()) * 4
                        #usdbalance = float(usd_balance) + float(kop)
                        #file_data       = file_data.replace(usd_balance, str(usdbalance))
                        file.seek(0)
                        #file.truncate(0)
                        file.write(file_data)
                        file.close()
                        print("5")
                        usd_label.configure(text="Current Balance : TMT"+str(updated_balance),fg_color="green")
                        usd_deposit_notif.configure(text='USD + $'+str(kop), fg_color='green')
                        
                        
                    def finish_rub():
                        print("2")
                        if usd_amount.get() == "":
                            usd_deposit_notif.configure(text='Obmen etjek pulluňyzy yazyň!',fg_color="red")
                            return
                        if float(usd_amount.get()) <=0:
                            usd_deposit_notif.configure(text='Obmen etjek puluňyz 0 dan aşak bolup bilmeyä', fg_color='red')
                            return

                        file = open(login_name, 'r+')
                        file_data = file.read()
                        details = file_data.split('\n')
                        current_balance = details[5]
                        #usd_balance = details[6]
                        print("3")
                        if float(usd_amount.get()) >float(current_balance):
                            usd_deposit_notif.configure(text='Sizin balansyňyzyň möçberi yeterlik däl!', fg_color='red')
                            print("4")
                            return
                        #elif float(usd_amount.get()) == float(current_balance):
                        updated_balance = current_balance
                        updated_balance = float(updated_balance) - float(usd_amount.get())
                        file_data       = file_data.replace(current_balance, str(updated_balance))
                        kop = float(usd_amount.get()) * 2
                        #usdbalance = float(usd_balance) + float(kop)
                        #file_data       = file_data.replace(usd_balance, str(usdbalance))
                        file.seek(0)
                        #file.truncate(0)
                        file.write(file_data)
                        file.close()
                        print("5")
                        usd_label.configure(text="Current Balance : TMT"+str(updated_balance),fg_color="green")
                        usd_deposit_notif.configure(text='RUB +  ₽'+str(kop), fg_color='green') 
                        
                    def finish_eur():
                        print("2")
                        if usd_amount.get() == "":
                            usd_deposit_notif.configure(text='Obmen etjek pulluňyzy yazyň!',fg_color="red")
                            return
                        if float(usd_amount.get()) <=0:
                            usd_deposit_notif.configure(text='Obmen etjek puluňyz 0 dan aşak bolup bilmeyä', fg_color='red')
                            return

                        file = open(login_name, 'r+')
                        file_data = file.read()
                        details = file_data.split('\n')
                        current_balance = details[5]
                        #usd_balance = details[6]
                        print("3")
                        if float(usd_amount.get()) >float(current_balance):
                            usd_deposit_notif.configure(text='Sizin balansyňyzyň möçberi yeterlik däl!', fg_color='red')
                            print("4")
                            return
                        #elif float(usd_amount.get()) == float(current_balance):
                        updated_balance = current_balance
                        updated_balance = float(updated_balance) - float(usd_amount.get())
                        file_data       = file_data.replace(current_balance, str(updated_balance))
                        kop = float(usd_amount.get()) * 3
                        #usdbalance = float(usd_balance) + float(kop)
                        #file_data       = file_data.replace(usd_balance, str(usdbalance))
                        file.seek(0)
                        #file.truncate(0)
                        file.write(file_data)
                        file.close()
                        print("5")
                        usd_label.configure(text="Current Balance : TMT"+str(updated_balance),fg_color="green")
                        usd_deposit_notif.configure(text='EUR +  €'+str(kop), fg_color='green')
                      
                    def finish_gbp():
                        print("2")
                        if usd_amount.get() == "":
                            usd_deposit_notif.configure(text='Obmen etjek pulluňyzy yazyň!',fg_color="red")
                            return
                        if float(usd_amount.get()) <=0:
                            usd_deposit_notif.configure(text='Obmen etjek puluňyz 0 dan aşak bolup bilmeyä', fg_color='red')
                            return

                        file = open(login_name, 'r+')
                        file_data = file.read()
                        details = file_data.split('\n')
                        current_balance = details[5]
                        #usd_balance = details[6]
                        print("3")
                        if float(usd_amount.get()) >float(current_balance):
                            usd_deposit_notif.configure(text='Sizin balansyňyzyň möçberi yeterlik däl!', fg_color='red')
                            print("4")
                            return
                        #elif float(usd_amount.get()) == float(current_balance):
                        updated_balance = current_balance
                        updated_balance = float(updated_balance) - float(usd_amount.get())
                        file_data       = file_data.replace(current_balance, str(updated_balance))
                        kop = float(usd_amount.get()) * 5
                        #usdbalance = float(usd_balance) + float(kop)
                        #file_data       = file_data.replace(usd_balance, str(usdbalance))
                        file.seek(0)
                        #file.truncate(0)
                        file.write(file_data)
                        file.close()
                        print("5")
                        usd_label.configure(text="Current Balance : TMT"+str(updated_balance),fg_color="green")
                        usd_deposit_notif.configure(text='GBP +  £'+str(kop), fg_color='green')  
                        
                    
                    #==================================================================
                    def usd():
                        global usd_amount
                        global usd_deposit_notif
                        global usd_label
                        
                        usd_user_frame2 = ctk.CTkFrame(master=frame22,width=700,height=500)
                        usd_user_frame2.pack(pady=200)
                        
                        font11= ctk.CTkFont(family=("Century Gothic"),size=30,weight="bold")
                        
                        usd_amount = ctk.StringVar()
                        file   = open(login_name, "r")
                        file_data = file.read()
                        user_details = file_data.split('\n')
                        details_balance = user_details[5]
                        #==================================================================
                        arka_fon = Image.open("bankamant.jpg")
                        arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(700,500))

                        label_arka_fon = ctk.CTkLabel(master=usd_user_frame2,image=arka_fon,text="")
                        label_arka_fon.place(relheight=1,relwidth=1)
                        
                        usd_label1 = ctk.CTkLabel(master=usd_user_frame2, text=' TMT - USD',font=font11,text_color="green",fg_color="transparent")
                        usd_label1.place(relx=0.4,rely=0.4)
                        
                        usd_label = ctk.CTkLabel(master=usd_user_frame2, text='Sizin sumatky balansynyz : '+details_balance,font=font3,text_color="orange")
                        usd_label.place(relx=0.2,rely=0.5)
                        
                        usd_label2 = ctk.CTkLabel(master=usd_user_frame2, text='Nace TMT USD çalysmak isliyaňiz ',font=font3,text_color="orange")
                        usd_label2.place(relx=0.2,rely=0.57)

                        usd_Entry = ctk.CTkEntry(master=usd_user_frame2, placeholder_text="1234",
                                            font=font3,fg_color="white",text_color="black",textvariable=usd_amount)
                        usd_Entry.place(relx=0.5,rely=0.57)
                        
                        usd_deposit_notif = ctk.CTkLabel(master=usd_user_frame2,text="",font=font3)
                        usd_deposit_notif.place(relx=0.25,rely=0.62)
                        
                        usd_btn_finsh = ctk.CTkButton(master=usd_user_frame2,text="USD",font=font3,height=10,width=60,
                                                fg_color="#3DCDFF",text_color="black",command=finish_usd)
                        usd_btn_finsh.place(relx=0.7,rely=0.83)
                        
                        usd_btn_finsh2 = ctk.CTkButton(master=usd_user_frame2,text="EUR",font=font3,height=10,width=60,
                                                fg_color="#3DCDFF",text_color="black",command=finish_eur)
                        usd_btn_finsh2.place(relx=0.8,rely=0.83)
                        
                        usd_btn_finsh3 = ctk.CTkButton(master=usd_user_frame2,text="RUB",font=font3,height=10,width=60,
                                                fg_color="#3DCDFF",text_color="black",command=finish_rub)
                        usd_btn_finsh3.place(relx=0.7,rely=0.88)
                        
                        usd_btn_finsh4 = ctk.CTkButton(master=usd_user_frame2,text="GBP",font=font3,height=10,width=60,
                                                fg_color="#3DCDFF",text_color="black",command=finish_gbp)
                        usd_btn_finsh4.place(relx=0.8,rely=0.88)
                        print("1")
                        def exit1 ():
                            usd_user_frame2.destroy()
                            D
                        user_btn = ctk.CTkButton(master=usd_user_frame2,text="YZA",height=50,
                                                font=font3,fg_color="#3DCDFF",text_color="black",command=exit1)
                        user_btn.place(relx=0.1,rely=0.85)
                            
                            
                    #==================================================================
                    btn1 = ctk.CTkButton(master= one_frame,text="Pul Çek",width=100,height=70,
                                         font=font3,fg_color="#3DCDFF",text_color="black",command=withdraw)
                    btn1.place(relx=0.23,rely=0.4)
                    
                    btn2 = ctk.CTkButton(master= one_frame,text="Pul Sal",width=100,height=70,
                                         font=font3,fg_color="#3DCDFF",text_color="black",command=user_pul_cekmek)
                    btn2.place(relx=0.42,rely=0.4)

                    btn3 = ctk.CTkButton(master= one_frame,text="Walýuta Çalyşygy",width=100,height=70,
                                         font=font3,fg_color="#3DCDFF",text_color="black",command=usd)
                    btn3.place(relx=0.6,rely=0.4)
                    def yza ():
                        root.deiconify()
                        D.destroy()
                    
                    btn = ctk.CTkButton(master= one_frame,text="Çykyş",width=100,height=70,
                                        font=font3,fg_color="#3DCDFF",text_color="black",command=D.quit)
                    btn.place(relx=0.8,rely=0.4)
                    #==================================================================
                elif login_password != password:
                    messagebox.showerror("YALNYSLYK BAR", "Sizin parolynyz yalnys!")
                    return
    
    registor1 = ctk.CTkFrame(master=B)
    registor1.pack(expand=True, fill="both")

    arka_fon = Image.open("registor_page.jpg")
    arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(1000,700))

    label_arka_fon = ctk.CTkLabel(master=registor1,image=arka_fon,text="")
    label_arka_fon.place(relheight=1,relwidth=1)
    font1= ctk.CTkFont(family=("Century Gothic"),size=30,weight="bold")
    #==================================================================
    frame2 = ctk.CTkFrame(master=registor1,width=380,height=400,fg_color="white")
    frame2.pack(padx=130,side="left")
    #==================================================================
    label1 = ctk.CTkLabel(master=frame2,text="G I R I Ş",font=font1,text_color="black")
    label1.place(relx=0.35,rely=0.1)
    #==================================================================
    font2 = ctk.CTkFont(family=("timer"),size=15,weight="bold")
    #==================================================================
    login_name = ctk.CTkLabel(master=frame2,text="Ulanyjynyň ady",font=font2,text_color="#3DCDFF")
    login_name.place(relx=0.05,rely=0.3)
            
    login_name_entry = ctk.CTkEntry(master=frame2,fg_color="white", textvariable=temp_login_name,corner_radius=100,
                                   width=300,placeholder_text="Mekan",text_color="black")
    login_name_entry.place(relx=0.03,rely=0.4)
    
    #==================================================================
    login_password = ctk.CTkLabel(master=frame2,text="Ulanyjynyň kody",font=font2,text_color="#3DCDFF")
    login_password.place(relx=0.03,rely=0.5)

    login_password_entry = ctk.CTkEntry(master=frame2,fg_color="white", textvariable=temp_login_password,corner_radius=100,
                                       width=300,placeholder_text="1234",show="#",text_color="black")
    login_password_entry.place(relx=0.03,rely=0.6)
    font3 = ctk.CTkFont(family=("timer"),size=10)
    C = ctk.BooleanVar()  
    def dana():
        #global B
        get_status = C.get() # B-nin icindaki bilgini al
        if(get_status==True):
            login_password_entry.configure(show="")
        elif(get_status==False):
            login_password_entry.configure(show="#")
        
    checkbox = ctk.CTkCheckBox(master=frame2,command=dana,text="Aç",
                                 width=20,height=30,fg_color="orange",border_width=1,border_color="black",
                                 text_color="black",hover_color="#3DCDFF",font=font3,variable=C)          
    checkbox.place(relx=0.85,rely=0.6)

    #==================================================================
    font3 = ctk.CTkFont(family=("Century Gothic"),size=12,weight="bold")
    #==================================================================
    def yza ():
        root.deiconify()
        B.destroy()
    
    btn = ctk.CTkButton(master=frame2,text="Yza",font=font3,fg_color="#3DCDFF",corner_radius=100,text_color="black",command=yza)
    btn.place(relx=0.1,rely=0.72)
        
    btn4 = ctk.CTkButton(master=frame2,text="Dowam et",font=font3,fg_color="#3DCDFF",text_color="black",command=login_session)
    btn4.place(relx=0.5,rely=0.72)
    #==================================================================
    name = ""
    def get_name(event):
        nonlocal name
        #---------------------------------
        name = login_name_entry.get()
        #---------------------------------
        if(not name):
            messagebox.showerror("YALNYSLYK BAR", "Adynyzy yazyn")
            return
        #---------------------------------
        login_password_entry.focus()
    # ==================================================================================================
    login_name_entry.bind("<Return>", get_name)
    #login_name_entry.bind("<FocusOut>", get_name)
    # ==================================================================================================
    password =""
    def get_password(event):
        nonlocal password
        #---------------------------------
        password = login_password_entry.get()
        #---------------------------------
        if(not password):
            messagebox.showerror("YALNYSLYK BAR", "Koynyzy bellan")
            return
        #---------------------------------
        btn4.focus()
    # ==================================================================================================
    login_password_entry.bind("<Return>", get_password)
    #login_name_entry.bind("<FocusOut>", get_password)
    

#------------------------------------------------------------------------------------------------------------------------
arka_fon = Image.open("GIRIS_LOGO.jpg")
arka_fon = ctk.CTkImage(dark_image=arka_fon,size=(1300,700))

label_arka_fon = ctk.CTkLabel(master=root,image=arka_fon,text="")
label_arka_fon.place(relheight=1,relwidth=1)

font3 = ctk.CTkFont(family=("Century Gothic"),size=17,weight="bold")

btn = ctk.CTkButton(master= root, width=150,height=70,command=Registor,text="Hasap doretmek",font=font3,fg_color="#3DCDFF",text_color="black")
btn.place(relx=0.04,rely=0.6)
btn2 = ctk.CTkButton(master= root, width=150,height=70,command=Login,text="Hasaba girmek",font=font3,fg_color="#3DCDFF",text_color="black")
btn2.place(relx=0.2,rely=0.6)


#image=(ctk.CTkImage(dark_image=Image.open("transaction.png"),size=(150,70)))

root.mainloop()       