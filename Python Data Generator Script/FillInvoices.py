import pyodbc
import random
import names
from faker import Faker
from datetime import date

def fillInvoice(connectionString, orderID):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')
    order = cursor.execute(f"SELECT * FROM Orders where OrderID = {orderID}").fetchone()
    if order == None:
        print("Error, order not found")
        return None
    if order[8] == order[9]:
        invoiceFullPaymentDate = str(date.today())
        isClosed = 1
    else:
        invoiceFullPaymentDate = None
        isClosed = 0
    amountAlreadyPaid = order[9]
    insertInvoiceQuery = f"INSERT INTO Invoices (OrderID, InvoiceFullPaymentDate, IsClosed, AmountAlreadyPaid, InvoiceDate) VALUES (?, ?, ?, ?, ?);"
    cursor.execute(insertInvoiceQuery, orderID, invoiceFullPaymentDate, isClosed, amountAlreadyPaid, str(date.today())) 

    conn.commit()
    # print("invoice has been created in the database")
    conn.close()

# fillInvoice('DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;', 2)