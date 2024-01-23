import pyodbc

def fillCreditCardType(connectionString):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    creditCardType = cursor.execute('SELECT * FROM CreditCardType')

    #If empty insert all creditCardTypes
    if creditCardType.fetchall() == []:
        insertCreditCardTypeQuery = ["INSERT INTO CreditCardType (Title, Type) VALUES ('MasterCard', 0)", "INSERT INTO CreditCardType (Title, Type) VALUES ('MasterCard', 1)", 
                                  "INSERT INTO CreditCardType (Title, Type) VALUES ('Visa', 0)", "INSERT INTO CreditCardType (Title, Type) VALUES ('Visa', 1)",
                                  "INSERT INTO CreditCardType (Title, Type) VALUES ('AmericanExpress', 0)", "INSERT INTO CreditCardType (Title, Type) VALUES ('AmericanExpress', 1)",]

        for script in insertCreditCardTypeQuery:
            cursor.execute(script)
        conn.commit()
    else:
        print("The CreditCardTypes are already inserted into the database")
    conn.close()

