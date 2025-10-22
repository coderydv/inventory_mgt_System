from tkinter import*
from PIL import Image,ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x750+230+150")
        self.root.title("Employee Dashboard      ||| developed by Mohit Ydv")
        self.root.config(bg="#C2B0B0")
        self.root.focus_force()
        #================================
        # All variables=======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        

    #======Search Frame=====
        Searchframe=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12),bd=2,relief=RIDGE, bg="white")
        Searchframe.place(x=250,y=20,width=800,height=70)

        #=== options====
        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_searchby, values=("Select","Emp ID","Name","Contact","Email"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt ,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(Searchframe,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.search).place(x=450,y=10,width=150,height=30)

        #======= title ======
        title=Label(self.root,text="employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1100)

        #==========content==========
        #====== Row 1 ===========

        lbl_empid=Label(self.root,text="employee ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=400,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=200,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender, values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_gender.place(x=550,y=150,width=150)
        cmb_gender.current(0)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=950,y=150,width=180)

    #====== Row 2 =========

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="Date of Birth",font=("goudy old style",15),bg="white").place(x=400,y=190)
        lbl_doj=Label(self.root,text="Date of Joining",font=("goudy old style",15),bg="white").place(x=750,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=200,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=550,y=190,width=150)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=950,y=190,width=180)

    #=====   Row 3 ========

        lbl_email=Label(self.root,text="E-mail",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_passr=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=400,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=200,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=550,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype, values=("Admin","Employee","Manager"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_utype.place(x=950,y=230,width=150)
        cmb_utype.current(0)
        
        #======= Row 4 ================

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=550,y=270)
                
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=200,y=270, width=300, height=70)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=650,y=270,width=180)

    #====== Buttons ======
        btn_add=Button(self.root,text="Save",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=550,y=310,width=130,height=30)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.update).place(x=700,y=310,width=130,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="#CF275F",fg="white",cursor="hand2",command=self.delete).place(x=850,y=310,width=130,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=1000,y=310,width=130,height=30)

    #======= Employee Details   ===================
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=300)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(
            emp_frame,
            columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)



        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="E-mail")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="Date of Birth")
        self.EmployeeTable.heading("doj",text="Date of Joining")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=50)
        self.EmployeeTable.column("name",width=90)
        self.EmployeeTable.column("email",width=90)
        self.EmployeeTable.column("gender",width=50)
        self.EmployeeTable.column("contact",width=70)
        self.EmployeeTable.column("dob",width=50)
        self.EmployeeTable.column("doj",width=50)
        self.EmployeeTable.column("pass",width=50)
        self.EmployeeTable.column("utype",width=90)
        self.EmployeeTable.column("address",width=200)
        self.EmployeeTable.column("salary",width=50)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        
        self.show()
#=================================================================================================================

    def add(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This employee ID already assigned, try diffrent",parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)"
                         "values(?,?,?,?,?,?,?,?,?,?,?)",
                                (      self.var_emp_id.get(),
                                       self.var_name.get(),
                                       self.var_email.get(),
                                       self.var_gender.get(),
                                       self.var_contact.get(),
                                       self.var_dob.get(),
                                       self.var_doj.get(),
                                       self.var_pass.get(),
                                       self.var_utype.get(),
                                       self.txt_address.get('1.0','end'),
                                       self.var_salary.get(),
                                )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#====== show function =======
    def show(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #=== if used for indexing error to avoid crash
        if row:
            self.var_emp_id.set(row[0]),
            self.var_name.set(row[1]),
            self.var_email.set(row[2]),
            self.var_gender.set(row[3]),
            self.var_contact.set(row[4]),
            self.var_dob.set(row[5]),
            self.var_doj.set(row[6]),
            self.var_pass.set(row[7]),
            self.var_utype.set(row[8]),
            self.txt_address.delete('1.0',END)
            self.txt_address.insert(END,row[9])
            self.var_salary.set(row[10]),
                                
#=========== Update ============================
    def update(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID",parent=self.root)
                else:
                    cur.execute(
                        "update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",
                                (      
                                       self.var_name.get(),
                                       self.var_email.get(),
                                       self.var_gender.get(),
                                       self.var_contact.get(),
                                       self.var_dob.get(),
                                       self.var_doj.get(),
                                       self.var_pass.get(),
                                       self.var_utype.get(),
                                       self.txt_address.get('1.0','end'),
                                       self.var_salary.get(),
                                       self.var_emp_id.get(),
                                )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Employee updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)




#=========== Delete ============================
    def delete(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid =?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Succesfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#=========== Clear ==============================
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
#========== Search ================
    def search(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        col = None  # To ensure it is always defined
        try:
            if self.var_searchby.get()=="Select":
               messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
               search_col = {
                    "Emp ID": "eid",
                    "Name": "name",
                    "Contact": "contact",
                    "Email": "email"
                }
               col = search_col.get(self.var_searchby.get())


            if col is None:
                messagebox.showerror("Error","Invalid search field selected",parent=self.root)
                return
            

            cur.execute(f"SELECT * FROM employee WHERE {col} LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
               # cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=cur.fetchall()

            if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                     self.EmployeeTable.insert('',END,values=row)
            else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#====== Main part======================= not to be disturbed
if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop() 