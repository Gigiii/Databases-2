import pyodbc
import random
import names
from faker import Faker
from FillOrders import fillOrders

def fillCustomers(connectionString, customerAmount):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    countries = cursor.execute("SELECT * FROM Countries").fetchall()
    properties = cursor.execute("SELECT * FROM Properties").fetchall()
    creditCardType = cursor.execute("SELECT * FROM CreditCardType").fetchall()
    fake = Faker('en_GB')

    for x in range(0, customerAmount):
        insertUserQuery = ""
        chosenCountry = random.randint(0,len(countries)-1)
        countryId = countries[chosenCountry][0]
        address = fake.address().split('\n')
        
        if random.randint(0,1) == 0:
            firstName = names.get_first_name(gender="male")
            gender = 0
        else:
            firstName = names.get_first_name(gender="female")
            gender = 1

        lastName = names.get_last_name()
        age = random.randint(18, 40)
       
        city = address[1]
        street = address[2]
        zipCode = random.randint(10000, 99999)
        phoneNumber = "+" + str(countries[chosenCountry][1]) + str(random.randint(100000000, 999999999))
        email = firstName + "." + lastName + "@gmail.com"
        password = firstName[:1] + lastName[:1] + str(random.randint(1000,1000000)) + str(age) + str(countries[chosenCountry][2][:2])
        accountStatus = 0
        insertUserQuery = f"INSERT INTO Customers (CountryID, FirstName, LastName, Age, \
                            Gender, City, Street, ZipCode, PhoneNumber, Email, Password, \
                            AccountStatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(insertUserQuery, countryId, firstName, lastName, age, gender, city, street, zipCode, phoneNumber, email, password, accountStatus)
        cursor.execute("SELECT @@IDENTITY AS ID;")
        customerID = cursor.fetchone()[0]
        conn.commit()
        property = properties[random.randint(0, len(properties) - 1)]
        fillOrders(connectionString, random.randint(1,3), customerID, property[1], property[0], creditCardType[random.randint(0, len(creditCardType) - 1)][0])
        print(f"{x} users have been added")
    conn.commit()
    print(str(customerAmount) + " customers have been added to the database alongside their orders, invoices, and reviews")
    conn.close()
