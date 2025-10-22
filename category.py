from tkinter import*
from PIL import Image,ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x480+230+150")
        self.root.title("Employee Dashboard      ||| developed by Mohit Ydv")
        self.root.config(bg="#C2B0B0")
        self.root.focus_force()
#====== Variables ==================
        self.Var_cat_id=StringVar()
        self.Var_name=StringVar()
#========== Title ===================
        lbl_title=Label(self.root, text="Manage Product Category",fg="white",font=("goudy old style", 30, "bold"),bd=3,relief=RIDGE,bg="#7556A5").pack(side=TOP,fill=X,padx=10,pady=5)

        lbl_name=Label(self.root, text="Enter Category Name",fg="white",font=("goudy old style", 20),bg="#4D4760").place(x=10,y=70,width=400)
        txt_name=Entry(self.root, textvariable=self.Var_name,fg="black",font=("goudy old style", 15),bg="lightyellow").place(x=10,y=130,width=300,height=30)
        self.root.bind('<Return>',lambda event: self.add()) ## for binding enter key
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white", cursor="hand2").place(x=320,y=130,height=30 ,width=100)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white", cursor="hand2").place(x=430,y=130, height=30,width=100)

#======= Category Details   ===================
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=550,y=70,width=550,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(
            cat_frame,
            columns=("cid","name"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)



        self.category_table.heading("cid",text="Category ID")
        self.category_table.heading("name",text=" Category Name")
        
        self.category_table["show"]="headings"

        self.category_table.column("cid",width=80)
        self.category_table.column("name",width=300)
        
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        #======images with resizing ===========
        #img1
        # Load and resize image 1
        self.im1 = Image.open("images/cat.jpg")
        self.im1 = self.im1.resize((500, 250), Image.Resampling.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)
        self.lbl_im1 = Label(self.root, image=self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=20, y=220)

# Load and resize image 2
        self.im2 = Image.open("images/category.jpg")
        self.im2 = self.im2.resize((500, 250), Image.Resampling.LANCZOS)
        self.im2 = ImageTk.PhotoImage(self.im2)
        self.lbl_im2 = Label(self.root, image=self.im2, bd=2, relief=RAISED)
        self.lbl_im2.place(x=570, y=220)

# Show table on startup
        self.show()
        
#===== FUNCTIONS ==============        
#=          Add Function       ====
    def add(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            if self.Var_name.get() == "":
                messagebox.showerror("Error","Category name must be required",parent=self.root)
            else:
                cur.execute("select * from category where name=?",(self.Var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This category already assigned, try diffrent",parent=self.root)
                else:
                    cur.execute(
                        "Insert into category (name)"
                         "values(?)",
                                
                                ( self.Var_name.get(), )
                    ) 
                    con.commit()
                    messagebox.showinfo("Success","Category added successfully",parent=self.root)
                    self.show()
                    self.Var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
#=          Show Function       ====
    def show(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()

        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#            Get Function         ====
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        #=== if is used for indexing error to avoid crash
        if row:
            self.Var_cat_id.set(row[0]),
            self.Var_name.set(row[1]),

#=========== Delete ============================
    def delete(self):
        con=sqlite3.connect(database=r'bca.db')
        cur=con.cursor()
        try:
            if self.Var_cat_id.get()=="":
                messagebox.showerror("Error","Please selct category from list",parent=self.root)
            else:
                cur.execute("select * from category where cid=?",(self.Var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error Please try again.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.Var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","category Deleted Succesfully",parent=self.root)
                        
                        self.show()
                        self.Var_cat_id.set("")
                        self.Var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



#====== Main part======================= not to be disturbed
if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop() 