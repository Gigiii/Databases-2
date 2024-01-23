import pyodbc
import random
import names
from faker import Faker
from FillProperties import fillProperties

def fillOwners(connectionString, ownerAmount):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    countries = cursor.execute("SELECT * FROM Countries").fetchall()
    fake = Faker('en_GB')
    identificationDocumentTypesList = ["Passport", "National ID", "Biometric Passport", "NIF"]


    for x in range(0, ownerAmount):
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
        gender = 0
        identificationDocumentType = identificationDocumentTypesList[random.randint(0, len(identificationDocumentTypesList) - 1)]
        identificationDocumentPhoto = fake.url()
        facephoto = fake.url()
        city = address[1]
        street = address[2]
        zipCode = random.randint(10000, 99999)
        phoneNumber = "+" + str(countries[chosenCountry][1]) + str(random.randint(100000000, 999999999))
        email = firstName + "." + lastName + "@gmail.com"
        bankAccountNumber = str(random.randint(100000000, 999999999))
        password = firstName[:1] + lastName[:1] + str(random.randint(1000,1000000)) + str(age) + str(countries[chosenCountry][2][:2])
        accountStatus = 0
        insertUserQuery = f"INSERT INTO Owners (CountryID, FirstName, LastName, Age, Gender, \
                            IdentificationDocumentType, IdentificationDocumentPhoto, FacePhoto, \
                            City, Street, ZipCode, PhoneNumber, Email, Password, BankAccountNumber, \
                            AccountStatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(insertUserQuery, countryId, firstName, lastName, age, gender, identificationDocumentType, identificationDocumentPhoto, facephoto, city, street, zipCode, phoneNumber, email, bankAccountNumber, password, accountStatus)
        cursor.execute("SELECT @@IDENTITY AS ID;")
        ownerID = cursor.fetchone()[0]
        conn.commit()
        fillProperties(connectionString, random.randint(1,3), ownerID, countryId)
        print(f"{x} owners have been added")

    
    print(str(ownerAmount) + " owners have been added to the database alongside their properties")
    conn.close()