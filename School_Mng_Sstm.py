# using mysql python connection
import ctypes
import tkinter as tkr
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from datetime import date
from matplotlib import pyplot as plt

ico='programm_CS_12th'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(ico)


import mysql.connector as MCS
mycon= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
Cur=mycon.cursor()

def Fee_mang():
    mycon2= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
    Cur=mycon2.cursor()
    mkt=tkr.Tk()
    mkt.title("Fee Management")
    mkt.geometry('900x700')
    mkt.configure(bg='#333333')
    img=PhotoImage(file=r'D:/Proj_logo.png')
    mkt.iconphoto(False,img)

    def close_FM():
        mkt.destroy()
        Home_pg()

    Cur.execute("Select * from stu_fee where sid=%s"%(var2.get()))
    try:
        for x in Cur:
            dat=list(x)
            abc='Name ---->'+dat[0]+'\n'+'Quat1 ---->'+dat[2]+'\n'+'Quat2 ---->'+dat[3]+'\n'+'Quat3 ---->'+dat[4]+'\n'+'Quat4 ---->'+dat[5]
        lab=tkr.Label(mkt,text=abc,font=('Britannica Bold',24),justify=tkr.CENTER,bg='#333333',fg='#FFFFFF')
        lab.pack()
    except:
        lab1=tkr.Label(mkt,text='Data not present!!!',font=('Britannica Bold',20),bg='#333333',fg='#FFFFFF')
        lab1.place(x='50',y='20')

    butn_FN_cl=tkr.Button(mkt,text='To return back',command=close_FM,bg='#3AD4D9',overrelief="raised",bd=3)
    butn_FN_cl.pack()

def imp_dates():

    data=''
    mycon4= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
    Curn=mycon4.cursor()
    win_imp_dat=tkr.Tk()
    win_imp_dat.title("Important Academic Dates")
    win_imp_dat.geometry('700x400')
    win_imp_dat.configure(bg='#333333')

    img=PhotoImage(file=r'D:/Proj_logo.png')
    win_imp_dat.iconphoto(False,img)
    def des_imp_dt():
        win_imp_dat.destroy()
        Home_pg()

    Curn.execute('Select * from imp_dat order by imp_dt')
    for x in Curn:
        a=list(x)
        data+=a[0]+'----->'+a[1]+'\n'
    lab_dt=tkr.Label(win_imp_dat,text=data,bg='#333333',fg='#FFFFFF')
    lab_dt.pack()

    butn_ret=tkr.Button(win_imp_dat,command=des_imp_dt,text='To exit back',bg='#3AD4D9',overrelief="raised",bd=3)
    butn_ret.pack()

def Lbd():
    
    mkt1=tkr.Tk()
    mkt1.title("LeaderBoard")
    mkt1.geometry('700x400')
    mkt1.configure(bg='#333333')
    img=PhotoImage(file=r'D:/Proj_logo.png')
    mkt1.iconphoto(False,img)
    
    def destroy_lbd():
        mkt1.destroy()
        Home_pg()

    global vari_sub,vari_tenm
    vari_sub=tkr.StringVar()
    vari_tenm=tkr.StringVar()
    lab_sub=tkr.Label(mkt1,text='Select subject',bg='#333333',fg='#FFFFFF')
    lab_sub.pack()

    com1=ttk.Combobox(mkt1,width=25,textvariable=vari_sub)
    com1['values']=('Eng','Maths','Phy','Chem')
    com1['state']='readonly'
    com1.current()
    com1.pack()
    
    lab_nm=tkr.Label(mkt1,text="Select Test name",bg='#333333',fg='#FFFFFF')
    lab_nm.pack()

    com2=ttk.Combobox(mkt1,width=25,textvariable=vari_tenm)
    com2['values']=('PT1','PT2','Hf','Annual')
    com2['state']='readonly'
    com2.current()
    com2.pack()

    def prd():
        mycon3= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
        Cur=mycon3.cursor()
        mkt2=tkr.Tk()
        mkt2.title("LeaderBoard")
        mkt2.geometry('700x400')
        mkt2.configure(bg='#333333')

        list_a=''
        count=0
        a=vari_tenm.get()
        b=vari_sub.get()
        if a=='' or b=='':
            messagebox.showwarning('WARNING','Please select the options!!')
            mkt2.destroy()

        else:
            try:
                Cur.execute("Select name,marks from stu_mark where sub like '%s' and testnm like '%s' order by marks Desc"%(str(b),str(a)))
            
                for x in Cur:
                    dat=list(x)
                    count+=1
                    a=str(count)+'--->'+' Name:'+dat[0].title()+' '+'Mark:'+str(dat[1])+'\n'
                    list_a=list_a+a
                    print(list_a)
                    

                lab1=tkr.Label(mkt2,text=list_a,font=('Britannica Bold',20),bg='#333333',fg='#FFFFFF')
                lab1.pack()
                if dat=='':
                    label_empt=tkr.Label(mkt2,text="No data present!!",bg='#333333',fg='#FFFFFF')
                    label_empt.pack()

            except:
                messagebox.showwarning("Warning",'Data not present!!')
                mkt2.destroy()
            
        mycon3.close()
    but_prd=tkr.Button(mkt1,text='SUBMIT',command=prd,bg='#3AD4D9',overrelief="raised",bd=3)
    but_prd.pack()
    
    but_lbd_clos=tkr.Button(mkt1,text='To close lbd',command=destroy_lbd,bg='#3AD4D9',overrelief="raised",bd=3)
    but_lbd_clos.pack()   

def Home_pg():
    win=tkr.Tk()
    win.title('Login done')
    win.geometry('500x500')
    win.configure(bg='#333333')
    img=PhotoImage(file=r'D:/Proj_logo.png')
    win.iconphoto(False,img)
    label=tkr.Label(win,text='|____Welcome To Student Management System____|',bg='#333333',fg='#FFFFFF')
    label.pack()
    label2=tkr.Label(win,text='Select an option',bg='#333333',fg='#FFFFFF')
    label2.pack()
    varib=tkr.StringVar()
    com=ttk.Combobox(win,width=25,textvariable=varib)
    com['values']=('Attendance','Marks','Fees Management','Leaderboard','Important dates','Return to main menu')
    com['state']='readonly'
    com.current()
    com.pack()
    def stud_main():
        nm=varib.get()
        data=''
        defl='Subject  testname  marks\n'
        
        def dest():
            win.destroy()

        if nm=='Marks':
            dest()
            Mark_win=tkr.Tk()
            Mark_win.title('Login Page')
            Mark_win.geometry('700x400')
            Mark_win.resizable(False,False)
            Mark_win.configure(bg='#333333')
            img=PhotoImage(file=r'D:/Proj_logo.png')
            Mark_win.iconphoto(False,img)

            Tab_Tree=ttk.Treeview(Mark_win,columns=('Test name','Subject','Marks'))
            Tab_Tree.column('#0',width=0,stretch=False)
            Tab_Tree.column('Test name',width=50)
            Tab_Tree.column('Subject',width=50)
            Tab_Tree.column('Marks',width=50)
            Tab_Tree.pack(fill='both',expand=True)

            Tab_Tree.heading('Test name',text='Test name')
            Tab_Tree.heading('Subject',text='Subject')
            Tab_Tree.heading('Marks',text='Marks')

            mycon1= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
            Cur=mycon1.cursor()
            Cur.execute("Select marks,sub,testnm from Stu_mark where sid=%s"%(var2.get()))
            try:
                for x in Cur:
                    a=list(x)
                    all=(a[1].title(),a[2].upper(),a[0])
                    Tab_Tree.insert(parent="",index=0,values=all)
                mycon1.close()

            except:
                Tab_Tree.insert(parent='',index=0,values=('Data','Not','Present'))

        elif nm=='Fees Management':
            dest()
            Fee_mang()
        
        elif nm=='Attendance':
            import mysql.connector as MCSA
            mycon2= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
            Cur1=mycon2.cursor()
            Cur1.execute('Select status from attendance where Stu_id=%s'%(var2.get()))
            present=0
            absnt=0
            onlv=0
            for x in Cur1:
                y=list(x)
                if y[0].lower()=='absent':
                    absnt+=1
                elif y[0].lower()=='present':
                    present+=1
                else:
                    onlv+=1
            vlu=[absnt,present,onlv]
            lbl=['Absent','Present','On Leave']
            plt.pie(vlu,labels=lbl)
            plt.legend(lbl)
            plt.show()
            mycon2.close()

        
        elif nm=="Leaderboard":
            dest()
            Lbd()

        elif nm=='Return to main menu':
            dest()
            login_pg_stud()

        elif nm=='Important dates':
            dest()
            imp_dates()
        
        else:
            messagebox.showwarning("Warning",'Please select an Option.')

    btn=tkr.Button(win,text='Submit',command=stud_main,bg='#3AD4D9',overrelief="raised",bd=3)
    btn.pack()

def login_pg_stud():
    
    window=tkr.Tk()
    window.title('Login Page')
    window.geometry('700x400')
    window.resizable(False,False)
    window.configure(bg='#333333')
    img=PhotoImage(file=r'D:/Proj_logo.png')
    window.iconphoto(False,img)

    image_path=PhotoImage(file='D:\Bg_pg.png')
    updated_logo=image_path.subsample(1,1)
    bg_image=tkr.Label(window,image=updated_logo)
    bg_image.pack()

    def close():
        window.destroy()

    label=tkr.Label(window,text="Please Login to proceed",cursor='Plus',bg='#333333',fg='#FFFFFF')
    label.pack()

    def func():
        mycon_lt= MCS.connect(host='localhost' ,user='root',password='rIsHu@123',database='abc')
        Cur_lt=mycon.cursor()
        if var1.get()=="":
            messagebox.showwarning("Warning",'Empty data')
        else:  
            a=var1.get()
            b=var2.get()
            Cur_lt.execute("SELECT name,id from Stud_dat")
            for x in Cur_lt:
                y=list(x)
                if y[0].lower()==a.lower() and y[1]==int(b):
                    window.destroy()
                    Home_pg()
            else:
                try:
                    window.destroy()
                    messagebox.showwarning("Warning",'Incorrect user name and id')
                except:
                    pass   
                
        Cur_lt.close()
        mycon_lt.close()

    var1=tkr.StringVar()
    global var2
    var2=tkr.IntVar()
    label2=tkr.Label(window,text="Enter name",bg='#333333',fg='#FFFFFF')
    label2.place(x='280',y='50')
    ent=tkr.Entry(window,textvariable=var1)
    ent.place(x='280',y='70')
    lable3=tkr.Label(window,text='Enter id',bg='#333333',fg='#FFFFFF')
    lable3.place(x='280',y='90')
    ent2=tkr.Entry(window,textvariable=var2)
    ent2.place(x='280',y='110')
    but2=tkr.Button(window,text='submit',command=func,bg='#3AD4D9',overrelief="raised",bd=3)
    but2.place(x='320',y='140')

    lable4=tkr.Label(window,text='To exit the student login page',bg='#333333',fg='#FFFFFF')
    lable4.place(x='260',y='330')

    but3=tkr.Button(window,text='Close',command=close,bg='#3AD4D9',overrelief="raised",bd=3)
    but3.place(x='320',y='350')
    window.mainloop()

def mng_stud():
    wind_mng_stud=tkr.Tk()
    wind_mng_stud.title('Manage Student')
    wind_mng_stud.geometry('600x400')
    wind_mng_stud.configure(bg='#333333')
    img=PhotoImage(file=r'D:/Proj_logo.png')
    wind_mng_stud.iconphoto(False,img)

    def end_mng_stud():
        wind_mng_stud.destroy()
        Home_pg_Tec()

    lab_mng_stud_1=tkr.Label(wind_mng_stud,text='Select an option to proceed!!',bg='#333333',fg='#FFFFFF')
    lab_mng_stud_1.pack()

    def proc_mnst():
        opt=com_mng_var.get()
        if opt=='Add Student':
            def cont():
                a=ent_mg_id.get()
                b=ent_mg_nm.get()
                c=ent_mg_cl.get()
                d=ent_mg_rno.get()
                try:
                    mcs_mngstd=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
                    mycur_mngst=mcs_mngstd.cursor()
                    mycur_mngst.execute("Insert into stud_dat values(%s,'%s','%s',%s)"%(a,b,c,d))
                    mcs_mngstd.commit()
                    messagebox.showinfo('Task Completed','Student Data is added!!')
                    
                    wind_add_std.destroy()
                    mcs_mngstd.close()
                
                except:
                    messagebox.showwarning('Warning','Something went wrong!!')
        
            wind_add_std=tkr.Tk()
            wind_add_std.title('Add student')
            wind_add_std.geometry('600x400')
            wind_add_std.configure(bg='#333333')
            
            lab_add_std_id=tkr.Label(wind_add_std,text='Enter Id of student',bg='#333333',fg='#FFFFFF')
            lab_add_std_id.pack()            
            var_mg_id=tkr.IntVar()
            ent_mg_id=tkr.Entry(wind_add_std,textvariable=var_mg_id)
            ent_mg_id.pack()

            lab_add_std_nm=tkr.Label(wind_add_std,text='Enter Name of student',bg='#333333',fg='#FFFFFF')
            lab_add_std_nm.pack()            
            var_mg_nm=tkr.StringVar()
            ent_mg_nm=tkr.Entry(wind_add_std,textvariable=var_mg_nm)
            ent_mg_nm.pack()

            lab_add_std_cl=tkr.Label(wind_add_std,text='Enter class of student',bg='#333333',fg='#FFFFFF')
            lab_add_std_cl.pack()            
            var_mg_cl=tkr.StringVar()
            ent_mg_cl=tkr.Entry(wind_add_std,textvariable=var_mg_cl)
            ent_mg_cl.pack()

            lab_add_std_rno=tkr.Label(wind_add_std,text='Enter roll no. of student',bg='#333333',fg='#FFFFFF')
            lab_add_std_rno.pack()            
            var_mg_rno=tkr.IntVar()
            ent_mg_rno=tkr.Entry(wind_add_std,textvariable=var_mg_rno)
            ent_mg_rno.pack()

            btn_proccd=tkr.Button(wind_add_std,text='Submit',command=cont,bg='#3AD4D9',overrelief="raised",bd=3)
            btn_proccd.pack()

            wind_add_std.mainloop()

        elif opt=='Remove Student':
            wind_rem_std=tkr.Tk()
            wind_rem_std.title('Add student')
            wind_rem_std.geometry('600x400')
            wind_rem_std.configure(bg='#333333')

            def delt_dta():
                
                def end_std_rem():
                    wind_rem_std.destroy()
                    Home_pg_Tec()

                a=ent_reg_id.get()
                try:
                    mcs_remstd=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
                    mycur_remst=mcs_remstd.cursor()
                    mycur_remst.execute("Delete from stud_dat where id=%s"%(a))
                    mcs_remstd.commit()
                    mycur_remst.execute("Delete from stud_dat where id=%s"%(a))
                    mcs_remstd.commit()
                    messagebox.showinfo('Task Completed','Student Data is removed!!')
                    end_std_rem()
                    mcs_remstd.close()
                
                except:
                    messagebox.showwarning('Warning','Data not present!!')


            lab_rem_std_id=tkr.Label(wind_rem_std,text='Enter Id of student to remove.',bg='#333333',fg='#FFFFFF')
            lab_rem_std_id.pack()            
            var_reg_id=tkr.IntVar()
            ent_reg_id=tkr.Entry(wind_rem_std,textvariable=var_reg_id)
            ent_reg_id.pack()

            btn_procd=tkr.Button(wind_rem_std,text='Submit',command=delt_dta,bg='#3AD4D9',overrelief="raised",bd=3)
            btn_procd.pack()

        elif opt=='Show students':

            def close_show():
                wind_sho_std.destroy()

            wind_sho_std=tkr.Tk()
            wind_sho_std.title('Show student')
            wind_sho_std.geometry('600x400')
            wind_sho_std.configure(bg='#333333')

            dta=''

            mcs_shostd=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
            mycur_shost=mcs_shostd.cursor()
            mycur_shost.execute("Select Name from stud_dat order by name")
            for x in mycur_shost:
                a=x
                dta+=str(a[0]).title()+'\n'
            label_sho=tkr.Label(wind_sho_std,text=dta,bg='#333333',fg='#FFFFFF')
            label_sho.pack()
            but_ret=tkr.Button(wind_sho_std,text='To return back',command=close_show,bg='#3AD4D9',overrelief="raised",bd=3)
            but_ret.pack()
            mcs_shostd.close()
            
    label_main_mng_dt=tkr.Label(wind_mng_stud,text='Select an option',bg='#333333',fg='#FFFFFF')
    label_main_mng_dt.pack()
    com_mng_var=tkr.StringVar()
    comb_mng_stud=ttk.Combobox(wind_mng_stud,width=25,textvariable=com_mng_var)
    comb_mng_stud['values']=('Add Student','Remove Student','Show students')
    comb_mng_stud['state']='readonly'
    comb_mng_stud.current()
    comb_mng_stud.pack()
    btn_mng_stud=tkr.Button(wind_mng_stud,text='Submit',command=proc_mnst,bg='#3AD4D9',overrelief="raised",bd=3)
    btn_mng_stud.pack()

    btn_end=tkr.Button(wind_mng_stud,text='To Return',command=end_mng_stud,bg='#3AD4D9',overrelief="raised",bd=3)
    btn_end.pack()

def imp_dat():
    def imp_close():
        imp_win.destroy()
        Home_pg_Tec()

    def imp_cont():
        vark=imp_comb.get()
        if vark=='show events':
            def cls_show_imp():
                try:
                    show_win.destroy()
                    imp_win.destroy()
                except:
                    pass

            imp_close()
            show_win=tkr.Tk()
            show_win.title('Important dates')
            show_win.geometry('600x400')
            show_win.configure(bg='#333333')
            dat=''
            imp_mcs=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
            imp_cur=imp_mcs.cursor()
            imp_cur.execute('Select * from imp_dat order by imp_dt')
            for x in imp_cur:
                a=list(x)
                dat+=a[0]+'----->'+a[1]+'\n'
            label_imp=tkr.Label(show_win,text=dat,bg='#333333',fg='#FFFFFF')
            label_imp.pack()
            imp_mcs.close()
            btn_cls=tkr.Button(show_win,text='Close',command=cls_show_imp,bg='#3AD4D9',overrelief="raised",bd=3)
            btn_cls.pack()
        
        elif vark=='Add new event':
            def continue1():
                name=ent_name.get()
                date=ent_date.get()
                print(name,date)
                print(var_name,var_dates)
                print(ent_date.get())
                if name!='':
                    imp_mcs=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
                    imp_cur=imp_mcs.cursor()
                    imp_cur.execute("Insert into imp_dat values('%s','%s')"%(name,date))
                    imp_mcs.commit()
                    messagebox.showinfo('Task Completed','Data added!!')
                    add_impdt.destroy()
                    imp_mcs.close()
                    imp_close()
            
                else:
                    messagebox.showwarning('Warning !!!','Something went wrong!!')

            imp_win.destroy()
            add_impdt=tkr.Tk()
            add_impdt.title('Adding new event')
            add_impdt.geometry('600x400')
            add_impdt.configure(bg='#333333')
            
            var_name=tkr.StringVar()
            var_dates=tkr.StringVar()
            label_name=tkr.Label(add_impdt,text='Enter Name of the event',bg='#333333',fg='#FFFFFF')
            label_date=tkr.Label(add_impdt,text='Enter Date of the event',bg='#333333',fg='#FFFFFF')
                
            ent_name=tkr.Entry(add_impdt,textvariable=var_name)
            ent_date=tkr.Entry(add_impdt,textvariable=var_dates)
            but_1=tkr.Button(add_impdt,text='Submit',command=continue1,bg='#3AD4D9',overrelief="raised",bd=3)
            label_name.pack()
            ent_name.pack()
            label_date.pack()
            ent_date.pack()
            but_1.pack()

            
            add_impdt.mainloop()
        elif vark=='Remove event':
            def rem_event():
                imp_win.destroy()
                a=ent_rem.get()
                rem_mcs=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
                rem_cur=rem_mcs.cursor()
                try:
                    rem_cur.execute("Delete from imp_dat where imp_dt='%s'"%(a.lower()))
                    rem_mcs.commit()
                    messagebox.showinfo('Done','Data successfully removed!')
                    rem_mcs.close()
                    rem_win.destroy()

                except:
                    messagebox.showwarning('Warning!','Data not present or try to enter similar data')

            rem_win=tkr.Tk()
            rem_win.title("Removing data")
            rem_win.geometry('600x400')
            rem_win.configure(bg='#333333')
            rem_var=tkr.StringVar()
            lab_rem=tkr.Label(rem_win,text="Enter name of the event to remove.",bg='#333333',fg='#FFFFFF')
            lab_rem.pack()
            ent_rem=tkr.Entry(rem_win,textvariable=rem_var)
            ent_rem.pack()
            btn_rem=tkr.Button(rem_win,text='Submit',command=rem_event,bg='#3AD4D9',overrelief="raised",bd=3)
            btn_rem.pack()
            
    imp_win=tkr.Tk()
    imp_win.title('Manage Important Dates')
    imp_win.geometry('600x400')
    imp_win.configure(bg='#333333')
    imp_comb_str=tkr.StringVar()

    imp_lab=tkr.Label(imp_win,text='Select an option!',bg='#333333',fg='#FFFFFF')
    imp_lab.pack()
    imp_comb=ttk.Combobox(imp_win,width=25,textvariable=imp_comb_str)
    imp_comb['values']=('Add new event','Remove event','show events')
    imp_comb['state']='readonly'
    imp_comb.current()
    imp_comb.pack()
    btn_imp_cont=tkr.Button(imp_win,text='Submit',command=imp_cont,bg='#3AD4D9',overrelief="raised",bd=3)
    btn_imp_cont.pack()

    lab_ext=tkr.Label(imp_win,text="To exit back",bg='#333333',fg='#FFFFFF')
    lab_ext.pack()
    btn_close_impdt=tkr.Button(imp_win,text='To return',command=imp_close,bg='#3AD4D9',overrelief="raised",bd=3)
    btn_close_impdt.pack()


def Home_pg_Tec():
    window_hom_t=tkr.Tk()
    window_hom_t.title('Home page')
    window_hom_t.configure(bg='#333333')
    window_hom_t.geometry('600x400')
    img=PhotoImage(file=r'D:/Proj_logo.png')
    window_hom_t.iconphoto(False,img)
    txt="|_________Welcome to Teacher's Management home page_________|"

    def end_home_pg():
        window_hom_t.destroy()

    def close_hpg():
        window_hom_t.destroy()
        loginpg_tech()

    def procc():
        opt=vari_tr.get()
        print(opt)
        if opt=='Manage Student':
            end_home_pg()
            mng_stud()

        elif opt=='Alter Important dates':
            end_home_pg()
            imp_dat()

        elif opt=='Generate Time Table':
            end_home_pg()
            mng_tt_win=tkr.Tk()
            mng_tt_win.title('Generating Time Table....')
            mng_tt_win.geometry('600x400')
            img=PhotoImage(file=r'D:/Proj_logo.png')
            mng_tt_win.iconphoto(False,img)
            mng_tt_win.configure(bg='#333333')
            
            def end_back():
                mng_tt_win.destroy()
                Home_pg_Tec()

            tdata=''            
            import random
            subj=['English','Maths','Hindi','Physics','Chemistry','Computer Science']
            Tim_slot=["9:00 - 10:00","10:00 - 11:00","11:00 - 12:00","12:30 - 1:30","1:30 - 2:30","2:30 - 3:30"]
            for x in Tim_slot:
                a=random.choice(subj)
                tdata+=a+'---->'+x+'\n'

            lab_gen_tt=tkr.Label(mng_tt_win,text=tdata,bg='#333333',fg='#FFFFFF')
            lab_gen_tt.pack()

            but_mng_res_back=tkr.Button(mng_tt_win,text='To return back',command=end_back,bg='#3AD4D9',overrelief="raised",bd=3)
            but_mng_res_back.pack()

            mng_tt_win.mainloop()

        elif opt=='Show Teachers':

            end_home_pg()
            sho_tech=tkr.Tk()
            sho_tech.title('Teachers')
            sho_tech.geometry('600x400')
            img=PhotoImage(file=r'D:/Proj_logo.png')
            sho_tech.iconphoto(False,img)
            sho_tech.configure(bg='#333333')
            
            sho_mcs=MCS.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
            sho_cur=sho_mcs.cursor()
            sho_cur.execute('SELECT NAME,SUBJECT,EID FROM TEC_DAT ORDER BY EID DESC')
            
            tbl=ttk.Treeview(sho_tech,columns=('C1','C2','C3'))
            
            tbl.column('#0',width=0,stretch=False)
            tbl.column('C1',width=50,anchor='c')
            tbl.column('C2',width=50,anchor='c')
            tbl.column('C3',width=50,anchor='c')
            
            tbl.heading('C1',text='Name')
            tbl.heading('C2',text='Subject')
            tbl.heading('C3',text='EID')
            tbl.pack(fill='both',expand=True)

            for x in sho_cur:
                dat=list(x)
                tbl.insert(parent='',index=0,values=(dat[0],dat[1],dat[2]))    
        
        elif opt=='Manage Attendance':
            
            def fun_Atten():
                wing_Atten.destroy()
                var_attn=atten_Var.get()
                if var_attn=='View attendance':
                    vw_atten=tkr.Tk()
                    vw_atten.title('View attendance')
                    vw_atten.configure(bg='#333333')
                    vw_atten.geometry('600x400')
                    img=PhotoImage(file=r'D:/Proj_logo.png')
                    vw_atten.iconphoto(False,img)
                    import mysql.connector as MKCT
                    mycon_t=MKCT.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
                    cursor_vw=mycon_t.cursor()
                    cursor_vw.execute('select * from attendance,stud_dat where attendance.Stu_Id=stud_dat.id')
                    a=cursor_vw.fetchall()

                    table=ttk.Treeview(vw_atten,columns=('Name','Id','Date','Status'))

                    table.column('#0',width=0,stretch=False)
                    table.column('Name',width=50,minwidth=40)
                    table.column('Id',width=50,minwidth=40)
                    table.column('Date',width=50,minwidth=40)
                    table.column('Status',width=50,minwidth=40)

                    table.heading('Name',text='Name')
                    table.heading('Id',text='Id')
                    table.heading('Date',text='Date')
                    table.heading('Status',text='Status')
                    table.pack(fill='both',expand=True)
                    for x in a:
                        b=list(x)
                        c=(b[4],b[0],b[1],b[2].title())
                        table.insert(parent='',index=0,values=c)
                    
                elif var_attn=='Perform Attendance':
                    def ret():
                        pr_atten.destroy()
                        Home_pg_Tec()

                    pr_atten=tkr.Tk()
                    pr_atten.title('View attendance')
                    pr_atten.configure(bg='#333333')
                    pr_atten.geometry('600x400')
                    img=PhotoImage(file=r'D:/Proj_logo.png')
                    pr_atten.iconphoto(False,img)

                    def fun_pr_atten():

                        student_id=var_atten_1.get()
                        status=var_atten_2.get()
                        print(student_id,status)
                        import mysql.connector as MKCT
                        mycon_t=MKCT.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
                        cursor=mycon_t.cursor()
                        try:
                            cursor.execute("INSERT INTO Attendance (Stu_ID, Date, Status) VALUES (%s, %s, %s)", (student_id, date.today(), status))
                            mycon_t.commit()
                            mycon_t.close()
                            messagebox.showinfo('Done!','Attendance Granted')
                        except:
                            messagebox.showerror('Duplicacy','Attendance already granted for the day!')
                            ret()

                    
                    var_atten_1=tkr.IntVar()
                    var_atten_2=tkr.StringVar()
                    lable1_atten=tkr.Label(pr_atten,text='Enter Student ID',bg='#333333',fg='#FFFFFF')
                    lable2_atten=tkr.Label(pr_atten,text='Enter the Status',bg='#333333',fg='#FFFFFF')
                    ent_atten_1=tkr.Entry(pr_atten,textvariable=var_atten_1)
                    ent_atten_2=tkr.Entry(pr_atten,textvariable=var_atten_2)
                    lable1_atten.pack()
                    ent_atten_1.pack()
                    lable2_atten.pack()
                    ent_atten_2.pack()

                    buttn_prd=tkr.Button(pr_atten,text='Enter',command=fun_pr_atten,bg='#3AD4D9',overrelief="raised",bd=3)
                    buttn_prd.pack()
                    but_ret=tkr.Button(pr_atten,text='To return',command=ret,bg='#3AD4D9',overrelief="raised",bd=3)
                    but_ret.pack()
                    

                else:
                    messagebox.showwarning('Warning !!','Select an option first')

            end_home_pg()
            wing_Atten=tkr.Tk()
            wing_Atten.title('Attendance Management')
            wing_Atten.configure(bg='#333333')
            wing_Atten.geometry('600x400')
            img=PhotoImage(file=r'D:/Proj_logo.png')
            wing_Atten.iconphoto(False,img)
            atten_Var=tkr.StringVar()
            cmb_atten=ttk.Combobox(wing_Atten,width=20,textvariable=atten_Var)
            cmb_atten['values']=('View attendance','Perform Attendance')
            cmb_atten['state']='readonly'
            cmb_atten.current()
            lab_attn=tkr.Label(wing_Atten,text='Select an option to proceed',bg='#333333',fg='#FFFFFF')
            lab_attn.pack()
            
            cmb_atten.pack()

            btn_atten=tkr.Button(wing_Atten,text='Click',command=fun_Atten,bg='#3AD4D9',overrelief="raised",bd=3)
            btn_atten.pack()


        else:
            messagebox.showwarning('WARNING !!!','Please select an option to proceed!!')
    
    label1_hm=tkr.Label(window_hom_t,text=txt,bg='#333333',fg='#FFFFFF')
    label1_hm.pack()

    label2=tkr.Label(window_hom_t,text='Select an option',bg='#333333',fg='#FFFFFF')
    label2.pack()
    vari_tr=tkr.StringVar()
    com_tr=ttk.Combobox(window_hom_t,width=25,textvariable=vari_tr)
    com_tr['values']=('Manage Student','Generate Time Table','Alter Important dates','Show Teachers','Manage Attendance')
    com_tr['state']='readonly'
    com_tr.current()
    com_tr.pack()

    btn_com_tr=tkr.Button(window_hom_t,text='Submit',command=procc,bg='#3AD4D9',overrelief="raised",bd=3)
    btn_com_tr.pack()

    label_ret=tkr.Label(window_hom_t,text='To return back',bg='#333333',fg='#FFFFFF')
    label_ret.pack()
    btn_hpg_t=tkr.Button(window_hom_t,text='To close',command=close_hpg,bg='#3AD4D9',overrelief="raised",bd=3)
    btn_hpg_t.pack()

def loginpg_tech():
    import mysql.connector as MKCT
    mycon_t=MKCT.connect(host='localhost',user='root',password='rIsHu@123',database='abc')
    cursor=mycon_t.cursor()

    def close_t():
        window_tr.destroy()

    window_tr=tkr.Tk()
    window_tr.title('Login Page')
    window_tr.geometry('700x400')
    window_tr.configure(bg='#333333')
    window_tr.resizable(False,False)
    image_path=PhotoImage(file='D:\Bg_pg.png')
    updated_logo=image_path.subsample(1,1)
    bg_image=tkr.Label(window_tr,image=updated_logo)
    bg_image.pack()

    img=PhotoImage(file=r'D:/Proj_logo.png')
    window_tr.iconphoto(False,img)

    label_t=tkr.Label(window_tr,text="Please Login to proceed",bg='#333333',fg='#FFFFFF')
    label_t.pack()

    def func_t():
        
        if str(var1_t.get()).isdigit() and var1_t.get()==0:
            messagebox.showwarning("Warning !!!",'Empty data')
        elif str(var1_t.get()).isdigit():  
            a=var1_t.get()
            b=var2_t.get()
            cursor.execute("SELECT eid,password from Tec_dat")
            for x in cursor:
                y=list(x)

                if y[0]==a and y[1]==b.upper():
                    close_t()
                    Home_pg_Tec()
                    break
                    
            else:
                window_tr.destroy()
                messagebox.showwarning("Warning !!!",'Incorrect user name and id')
        else:
            messagebox.showerror("ERROR!!!",'Enter valid ID number!') 
            mycon_t.close()   

    var1_t=tkr.IntVar()
    var2_t=tkr.StringVar()
    label2_t=tkr.Label(window_tr,text="Enter Teacher ID number.",bg='#333333',fg='#FFFFFF')
    label2_t.place(x='280',y='50')
    ent_t=tkr.Entry(window_tr,textvariable=var1_t)
    ent_t.place(x='280',y='70')
    lable3_t=tkr.Label(window_tr,text='Enter Password',bg='#333333',fg='#FFFFFF')
    lable3_t.place(x='280',y='90')
    ent2_t=tkr.Entry(window_tr,textvariable=var2_t,show="*")
    ent2_t.place(x='280',y='110')
    but2_t=tkr.Button(window_tr,text='submit',command=func_t,bg='#3AD4D9',overrelief="raised",bd=3)
    but2_t.place(x='320',y='140')

    lable4_t=tkr.Label(window_tr,text='To exit the Teacher login page',bg='#333333',fg='#FFFFFF')
    lable4_t.place(x='260',y='330')

    but3_t=tkr.Button(window_tr,text='Close',command=close_t,bg='#3AD4D9',overrelief="raised",bd=3)
    but3_t.place(x='320',y='350')

    window_tr.mainloop()

print("To start EMS please Call SMS .")
def SMS():
    ans_c='y'
    
    while ans_c in 'yY':
        print('Welcome to first page of Student Management System')
        print('For Teachers Select 1\nFor student select 2\nFor ending program select 3.')
        
        ans_p=int(input("Enter your choice."))
        if ans_p==1:
            loginpg_tech()

        elif ans_p==2:
            login_pg_stud()
        elif ans_p==3:
            print('Ending Programm!!')
            print('Thankyou For Coming!')
            break
        else:
            print("Enter a valid option please!")
        ans_c=input('Do you want to continue? {y/n}')
    
    else:
        print('Ending Program!!')
        print('Thankyou for coming!')

SMS()