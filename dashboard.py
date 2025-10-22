from tkinter import*
from PIL import Image,ImageTk  # pip install pillow 
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1750x1000+0+0")
        self.root.title("Inventory Management System ||| developed by Mohit Ydv")
        self.root.config(bg="white")

        #===title=====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("calibre",40,"bold"),bg = "#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====btn_logout====
        btn_logout = Button(
        self.root,
        text="Logout",
        font=("times new roman", 15, "bold"),
        bg="yellow",
        cursor="hand2"
            ).place(x=1580, y=10, height=50, width=150)

        #====clock====
        self.lbl_clock=Label(self.root,text="Welcome to inventory management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS ",
        font=("Arial",15,),
        bg="#4d636d",
        fg="white"
        ).place(x=0,y=70,relwidth=1, height=40)

        #=====Left Menu ====
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.Resampling.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=112,width=200,height=665)

        lbl_menuLogo=Label(leftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")

        lbl_menu=Label(leftMenu,text="Menu",font=("Arial",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(leftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(leftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(leftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_products=Button(leftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(leftMenu,text="Sales",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(leftMenu,text="Exit",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_contact_us=Button(leftMenu,text="contact Us",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Arial",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

    #====footer====
        lbl_footer=Label(self.root,text="IMS Inventory Management System | Developed by Mohit Ydv \n\n  For any technical issue Contact: 8711888858",
        font=("Arial",12,),
        bg="#4d636d",
        fg="white"
        ).pack(side=BOTTOM,fill=X)

    #=====content=====

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=400,y=120,height=150,width=300)

        self.lbl_suppliers=Label(self.root,text="Total Suppliers\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_suppliers.place(x=750,y=120,height=150,width=300)


        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1100,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=400,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=750,y=300,height=150,width=300)

        



#================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

#================================================================

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

#================================================================

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

#================================================================

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

#========================= Main part not to be disturbed========================

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop() 