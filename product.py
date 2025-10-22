from tkinter import*
from PIL import Image,ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x480+230+150")
        self.root.title("Product Dashboard      ||| developed by Mohit Ydv")
        self.root.config(bg="#C2B0B0")
        self.root.focus_force()
        
        #================================
        # All variables=======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pid=StringVar()
        self.var_category=StringVar()
        self.var_status=StringVar()
        self.var_supplier=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        
        
    #======= title ======
        title=Label(self.root,text="Product Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=10,y=5,width=1230)

    #======Product Frame=====
        productframe=LabelFrame(self.root,text="Search Product",font=("goudy old style",12),bd=2,relief=RIDGE, bg="white")
        productframe.place(x=10,y=50,width=500,height=400)
        title2=Label(productframe,text="Product Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X ,padx=5)
               
        lbl_category=Label(productframe,text="Category",font=("goudy old style",15),bg="white").place(x=20,y=50)
        lbl_supplier=Label(productframe,text="Supplier",font=("goudy old style",15),bg="white").place(x=20,y=90)
        lbl_name=Label(productframe,text="Name",font=("goudy old style",15),bg="white").place(x=20,y=130)
        lbl_price=Label(productframe,text="Price",font=("goudy old style",15),bg="white").place(x=20,y=170)
        lbl_qty=Label(productframe,text="Quantity",font=("goudy old style",15),bg="white").place(x=20,y=210)
        lbl_status=Label(productframe,text="Status",font=("goudy old style",15),bg="white").place(x=20,y=250)
        
        
        #=== text area and combo boxes
        
        #txt_category=Entry(productframe,textvariable=self.var_category,font=("goudy old style",15),bg="lightyellow").place(x=130,y=50,width=180)
        cmb_category=ttk.Combobox(productframe,textvariable=self.var_category, values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_category.place(x=130,y=50,width=180)
        cmb_category.current(0)
        #txt_supplier=Entry(productframe,textvariable=self.var_supplier,font=("goudy old style",15),bg="lightyellow").place(x=130,y=90,width=180)
        cmb_supplier=ttk.Combobox(productframe,textvariable=self.var_supplier, values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_supplier.place(x=130,y=90,width=180)
        cmb_supplier.current(0)
        txt_name=Entry(productframe,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=130,y=130,width=180)
        txt_price=Entry(productframe,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=130,y=170,width=180)
        txt_qty=Entry(productframe,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=130,y=210,width=180)
        cmb_status=ttk.Combobox(productframe,textvariable=self.var_status, values=("Select","approved","Unapproved","Delivered","In transit"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_status.place(x=130,y=250,width=150)
        cmb_status.current(0)
    
    #====== Buttons ======
        btn_add=Button(productframe,text="Save",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=20,y=310,width=100,height=30)
        btn_update=Button(productframe,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.update).place(x=130,y=310,width=100,height=30)
        btn_delete=Button(productframe,text="Delete",font=("goudy old style",15),bg="#CF275F",fg="white",cursor="hand2",command=self.delete).place(x=240,y=310,width=100,height=30)
        btn_clear=Button(productframe,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=350,y=310,width=100,height=30)
    
    
    #==    Search frames
        Searchframe=LabelFrame(self.root,text="Search Product",font=("goudy old style",12),bd=2,relief=RIDGE, bg="white")
        Searchframe.place(x=530,y=50,width=710,height=70)

        #=== options====
        cmb_category=ttk.Combobox(Searchframe,textvariable=self.var_searchby, values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_category.place(x=10,y=10,width=180)
        cmb_category.current(0)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt ,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(Searchframe,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=self.search).place(x=450,y=10,width=150,height=30)
  
       
    #======= Employee Details   ===================
        
        prdct_frame_table=Frame(self.root,bd=3,relief=RIDGE)
        prdct_frame_table.place(x=530,y=130,width=710,height=320)

        scrolly=Scrollbar(prdct_frame_table,orient=VERTICAL)
        scrollx=Scrollbar(prdct_frame_table,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(
            prdct_frame_table,
            columns=("pid","category","supplier","name","price","qty","status"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)



        self.productTable.heading("pid",text="Product Id")
        self.productTable.heading("category",text="Category")
        self.productTable.heading("supplier",text="Supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"

        self.productTable.column("pid",width=50)
        self.productTable.column("category",width=50)
        self.productTable.column("supplier",width=90)
        self.productTable.column("name",width=90)
        self.productTable.column("price",width=90)
        self.productTable.column("qty",width=50)
        self.productTable.column("status",width=70)
       
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)

        
        self.show()
        self.fetch_cat_sup()

### function to add category and supplier

    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("select")
                for i in cat:
                    self.cat_list.append(i[0])
            

            cur.execute("select name from supplier ")
            sup=cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("select")
                for i in sup:
                    self.sup_list.append(i[0])
            
            
            sup_list=[]
            for i in cat:
                sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#=================================================================================================================

    def add(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.var_category.get()=="":
                messagebox.showerror("Error","Category  must be required",parent=self.root)
            else:
                cur.execute("select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product already assigned, try diffrent",parent=self.root)
                else:
                    cur.execute(
                        "Insert into product (category,supplier,name,price,qty,status)"
                         "values(?,?,?,?,?,?)",
                                (      self.var_category.get(),
                                       self.var_supplier.get(),
                                       self.var_name.get(),
                                       self.var_price.get(),
                                       self.var_qty.get(),
                                       self.var_status.get(),
                                       
                                )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Product added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#====== show function =======
    def show(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        #=== if used for indexing error to avoid crash
        if row:
            self.var_pid.set(row[0]),
            self.var_category.set(row[1]),
            self.var_supplier.set(row[2]),
            self.var_name.set(row[3]),
            self.var_price.set(row[4]),
            self.var_qty.set(row[5]),
            self.var_status.set(row[6]),
            
                                
#=========== Update ============================
    def update(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Category must be required",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID",parent=self.root)
                else:
                    cur.execute(
                        "update product set category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?",
                                (      
                                       self.var_category.get(),
                                       self.var_supplier.get(),
                                       self.var_name.get(),
                                       self.var_price.get(),
                                       self.var_qty.get(),
                                       self.var_status.get(),
                                       self.var_pid.get(),
                                )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Product updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)




#=========== Delete ============================
    def delete(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Product Category must be required",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid =?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","product Deleted Succesfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#=========== Clear ==============================
    def clear(self):
        self.var_pid.set("")
        self.var_category.set("Select")
        self.var_supplier.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("")
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
                    
                    "Category": "category",
                    "Supplier": "supplier",
                    "Name": "name",
                    
                }
               col = search_col.get(self.var_searchby.get())


            if col is None:
                messagebox.showerror("Error","Invalid search field selected",parent=self.root)
                return
            

            cur.execute(f"SELECT * FROM product WHERE {col} LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
               # cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=cur.fetchall()

            if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                     self.productTable.insert('',END,values=row)
            else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#====== Main part======================= not to be disturbed
if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop() 