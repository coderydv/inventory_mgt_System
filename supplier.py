from tkinter import*
from PIL import Image,ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x480+230+150")
        self.root.title("Employee Dashboard      ||| developed by Mohit Ydv")
        self.root.config(bg="#C2B0B0")
        self.root.focus_force()
        #================================
        # All variables=======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        

    #======Search Frame=====
       
        #=== options====
        lbl_search=Label(self.root,text="Search by Invoice No.",bg="white", font=("goudy old style",15))
        lbl_search.place(x=620,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt ,font=("goudy old style",15),bg="lightyellow").place(x=830,y=80)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.search).place(x=1080,y=80,width=100,height=30)

        #======= title ======
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=10,y=10,width=1180,height=50)

        #==========content==========
        #====== Row 1 ===========

        lbl_supplier_invoice=Label(self.root,text=" Invoice No.",font=("goudy old style",15),bg="white").place(x=10,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=130,y=80,width=200)
        
    #====== Row 2 =========

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=10,y=130)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=130,y=130,width=200)
       
    #=====   Row 3 ========

        lbl_contact=Label(self.root,text="Contact ",font=("goudy old style",15),bg="white").place(x=10,y=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=130,y=180,width=180)
       
        #======= Row 4 ================

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=10,y=270)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=130,y=230, width=460, height=110)
                
        #====== Buttons ======
        btn_add=Button(self.root,text="Save",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=130,y=370,width=100,height=50)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.update).place(x=250,y=370,width=100,height=50)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="#CF275F",fg="white",cursor="hand2",command=self.delete).place(x=370,y=370,width=100,height=50)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=490,y=370,width=100,height=50)

    #======= Employee Details   ===================
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=615,y=140,width=570,height=280)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(
            emp_frame,
            columns=("invoice","name","contact","desc"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)



        self.supplierTable.heading("invoice",text="Invoice No")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=30)
        self.supplierTable.column("name",width=50)
        self.supplierTable.column("contact",width=50)
        self.supplierTable.column("desc",width=90)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
#=================================================================================================================
    #invoice
    def add(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice No. already assigned, try diffrent",parent=self.root)
                else:
                    cur.execute(
                        "Insert into supplier (invoice,name,contact,desc)"
                         "values(?,?,?,?)",
                                (      self.var_sup_invoice.get(),
                                       self.var_name.get(),
                                       self.var_contact.get(),
                                       self.txt_desc.get('1.0','end'),
                                       
                                )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Supplier added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#====== show function =======
    def show(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #=== if used for indexing error to avoid crash
        if row:
            self.var_sup_invoice.set(row[0]),
            self.var_name.set(row[1]),
            self.var_contact.set(row[2]),
            self.txt_desc.delete('1.0',END)
            self.txt_desc.insert(END,row[3])
                    
                                
#=========== Update ============================
    def update(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute(
                        "update supplier set name=?,contact=?,desc=? where invoice=?",
                                (      
                                       self.var_name.get(),
                                       self.var_contact.get(),
                                       self.txt_desc.get('1.0','end'),
                                       self.var_sup_invoice.get(),
                                )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Supplier updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)




#=========== Delete ============================
    def delete(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Succesfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#=========== Clear ==============================
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        
        self.show()

#========== Search ================
    def search(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()
        
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            else:
               cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
               row=cur.fetchone()

            if row!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
            else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#====== Main part======================= not to be disturbed
if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop() 