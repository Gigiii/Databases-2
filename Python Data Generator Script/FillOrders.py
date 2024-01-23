import pyodbc
import random
import names
from datetime import date, timedelta
from faker import Faker
from FillInvoices import fillInvoice
from FillReviews import fillReviews

def fillOrders(connectionString, ordersAmount, customerID, ownerID, propertyID, creditCardTypeID):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')

    for x  in range(0, ordersAmount):
        creditCardNumber = random.randint(1000000000000000, 9999999999999999)
        creditCardExpirationDate = fake.date_between(date(2024, 4, 3), date(2030, 8, 18))
        creditCardCCV = random.randint(100,999)
        durationOfStay = random.randint(1,14)
        totalPrice = durationOfStay * random.randint(20,100)
        if random.randint(0,1) == 1:
            amountPaid = totalPrice
        else:
            amountPaid = totalPrice - random.randint(5,20)
        checkInDate = fake.date_between(date(2024, 2, 3), date(2024, 4, 18))
        checkOutDate = checkInDate + timedelta(days=durationOfStay)
        orderStatus = "Completed"
        insertOrderQuery = f"INSERT INTO Orders (CustomerID, OwnerID, PropertyID, CreditCardTypeID, \
                             CreditCardNumber, CreditCardExpirationDate, CreditCardCCV, TotalPrice, \
                             AmountPaid, DurationOfStay, CheckInDate, CheckOutDate, OrderStatus)    \
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(insertOrderQuery, customerID, ownerID, propertyID, creditCardTypeID,
                       creditCardNumber, str(creditCardExpirationDate), creditCardCCV, totalPrice,
                       amountPaid, durationOfStay, str(checkInDate), str(checkOutDate), orderStatus)
        cursor.execute("SELECT @@IDENTITY AS ID;")
        orderID = cursor.fetchone()[0]
        conn.commit()
        fillInvoice(connectionString, orderID)
        fillReviews(connectionString, 1, propertyID, customerID)
    # print(str(ordersAmount) + " orders have been added to the database")
    conn.close()

# fillOrders('DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;', 2, 1, 1, 1, 1)
