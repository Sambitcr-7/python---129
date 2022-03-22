from tkinter import *
from tkinter import ttk
from typing import Coroutine
import mysql.connector

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Mangment System")
        self.root.geometry("1550x800+0+0")



        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktite_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finallprice_var=StringVar()


        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM ", bg="#B6D0E2", fg="green",bd = 20, relief=RIDGE, font=("time new romen", 50, "bold"), padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)


        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#B6D0E2")
        frame.place(x=0, y=130, width=1530, height=400)


        # *************************DataFrameLeft**************************

        DataFrameLeft=LabelFrame(frame, text= "Library Membership Information ", bg= "#B6D0E2", bd=12, relief= RIDGE, font=("time new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)


        lblMember = Label(DataFrameLeft, bg="#B6D0E2",text="Member Type", font=("time new roman", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)


        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var, font=("time new roman", 15, "bold"), width= 27, state="readonly")
        comMember["value"]=("Admin staf", "student", "Lecturer")
        comMember.grid(row=0,column=1)


        lblPRN_No = Label(DataFrameLeft, bg="#B6D0E2",text="PRN NO", font=("arial", 12, "bold"), padx=2)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1)



        lblTitle = Label(DataFrameLeft, bg="#B6D0E2",text="ID NO", font=("arial", 12, "bold"), padx=2, pady=4)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="#B6D0E2",text="FirstName", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="#B6D0E2",text="LastName", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)


        lblAddress1 = Label(DataFrameLeft, bg="#B6D0E2",text="Address1", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)


        lblAddress2 = Label(DataFrameLeft, bg="#B6D0E2",text="Address2", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.address2_var, width=29)
        txtAddress2.grid(row=6, column=1)


        lblPostCode = Label(DataFrameLeft, bg="#B6D0E2",text="PRN NO", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=7, column=1)


        lblMobile = Label(DataFrameLeft, bg="#B6D0E2",text="Mobile", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial", 13, "bold"),textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)


        lblBookId = Label(DataFrameLeft, bg="#B6D0E2",text="Book ID", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)


        lblBookTitle = Label(DataFrameLeft, bg="#B6D0E2",text="Book Title", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.booktite_var, width=29)
        txtBookTitle.grid(row=1, column=3)



        lblAuther = Label(DataFrameLeft, bg="#B6D0E2",text="Auther Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.auther_var, width=29)
        txtAuther.grid(row=2, column=3)


        lblDateBorrowered = Label(DataFrameLeft, bg="#B6D0E2",text="Date Borrowered", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateBorrowered.grid(row=3, column=2, sticky=W)
        txtDateBorrowered=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowered.grid(row=3, column=3)


        lblDateDue = Label(DataFrameLeft, bg="#B6D0E2",text="Date Due", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)


        lblDaysOnBook = Label(DataFrameLeft, bg="#B6D0E2",text="Date On Book", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.daysonbook_var, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="#B6D0E2",text="Late Return Fine", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial", 15, "bold"),textvariable=self.lateratefine_var, width=24)
        txtLateReturnFine.grid(row=6, column=3)


        lblDateOverdate = Label(DataFrameLeft, bg="#B6D0E2",text="Date Over Due", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.dateoverdue_var, width=29)
        txtDateOverdate.grid(row=7, column=3)


        lblActualPrice = Label(DataFrameLeft, bg="#B6D0E2",text="Actual Price", font=("arial", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial", 12, "bold"),textvariable=self.finallprice_var, width=29)
        txtActualPrice.grid(row=8, column=3)



# **************************DataFrameRight***************8

        DataFrameRight=LabelFrame(frame, text= "Book Details", bg= "#B6D0E2", bd=12, relief= RIDGE, font=("time new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox= Text(DataFrameRight, font=("arail", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First book', 'Learn Python The Hard Way', 'Python Programming', 'Secrete Rahshy', 'python cookBook', 'Inton Python', 'Joes Ellif guru', "ellif Jungle python", 'RedChill Python', 'Sam Books', 'lee books', 'Train to Pasistan', 'Helf Grilfrind', 'After 2020', 'School life', 'India in 2020', 'Life after COVID-19', 'Green Sole', 'Life is Underwater', 'Being Haevy Diver']
        listBox=Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.grid(row = 0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # *****************Button Frame****************
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#B6D0E2")
        framebutton.place(x=0, y=530, width=1530, height=70)


        btnAddDate=Button(framebutton, text="Add Data", font=("arial", 12,"bold" ), width=23, bg="#0000FF", fg="white")
        btnAddDate.grid(row=0, column=0)


        btnAddDate=Button(framebutton, text="Show data", font=("arial", 12,"bold" ), width=23, bg="#0000FF", fg="white")
        btnAddDate.grid(row=0, column=1)

        btnAddDate=Button(framebutton, text="Update", font=("arial", 12,"bold" ), width=23, bg="#0000FF", fg="white")
        btnAddDate.grid(row=0, column=2)

        btnAddDate=Button(framebutton, text="Delete", font=("arial", 12,"bold" ), width=23, bg="#0000FF", fg="white")
        btnAddDate.grid(row=0, column=3)

        btnAddDate=Button(framebutton, text="Reset", font=("arial", 12,"bold" ), width=23, bg="#0000FF", fg="white")
        btnAddDate.grid(row=0, column=4)

        btnAddDate=Button(framebutton, text="Exit", font=("arial", 12,"bold" ), width=23, bg="#0000FF", fg="white")
        btnAddDate.grid(row=0, column=5)



    #    ********************************Information Frame******************************** 
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#B6D0E2")
        frameDetails.place(x=0, y=600, width=1530, height=195)




        Table_frame= Frame(frameDetails,bd=6, relief=RIDGE, bg="#B6D0E2")
        Table_frame.place(x=0, y=2, width=1460, height=190)


        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)





        self.libray_table=ttk.Treeview(Table_frame, columns=("membertype", "prnno", "title", "firstname" ,"lastname", "address1", "address2", "postid", "mobile", "bookid", "booktitle", "auther", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT,fill=Y)


        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)

        self.libray_table.heading("membertype", text="Member Type")
        self.libray_table.heading("prnno", text="PRN No.")
        self.libray_table.heading("title", text="Title")
        self.libray_table.heading("firstname", text="First Name")
        self.libray_table.heading("lastname", text="Last Name")
        self.libray_table.heading("address1", text="Address1")
        self.libray_table.heading("address2", text="Addresss2")
        self.libray_table.heading("postid", text="Post Id")
        self.libray_table.heading("mobile", text="Mobile Number")
        self.libray_table.heading("bookid", text="Book Id")
        self.libray_table.heading("booktitle", text="Book Title")
        self.libray_table.heading("auther", text="Auther")
        self.libray_table.heading("dateborrowed", text="Date of Borrowed")
        self.libray_table.heading("datedue", text="Date Due")
        self.libray_table.heading("days", text="DaysonBook")
        self.libray_table.heading("latereturnfine", text="LaterReturnFine")
        self.libray_table.heading("dateoverdue", text="Date Over Due")
        self.libray_table.heading("finalprice", text="Final Price")

        self.libray_table["show"]= "headings"
        self.libray_table.pack(fill= BOTH, expand=1)



        self.libray_table.column("membertype", width=100)
        self.libray_table.column("prnno", width=100)
        self.libray_table.column("title", width=100)
        self.libray_table.column("firstname", width=100)
        self.libray_table.column("lastname", width=100)
        self.libray_table.column("address1", width=100)
        self.libray_table.column("address2", width=100)
        self.libray_table.column("postid", width=100)
        self.libray_table.column("mobile", width=100)
        self.libray_table.column("bookid", width=100)
        self.libray_table.column("booktitle", width=100)
        self.libray_table.column("auther", width=100)
        self.libray_table.column("dateborrowed", width=100)
        self.libray_table.column("datedue", width=100)
        self.libray_table.column("days", width=100)
        self.libray_table.column("latereturnfine", width=100)
        self.libray_table.column("dateoverdue", width=100)
        self.libray_table.column("finalprice", width=100)




    def adda_data(self):
        conn=mysql.connector.connect    






if __name__ == "__main__":
    root= Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()        