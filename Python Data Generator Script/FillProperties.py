import pyodbc
import random
import names
from faker import Faker
from FillPropertyPhotos import fillPropertyPhotos
from FillFeatures import fillFeatures

def fillProperties(connectionString, propertyAmount, ownerID, countryID):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')
    features = cursor.execute("SELECT * FROM FeatureType").fetchall()

    for x  in range(0, propertyAmount):
        title = fake.street_name()
        propertyDescription = fake.text(max_nb_chars=500) 
        address = fake.address().split('\n')
        city = address[1]
        street = address[2]
        zipCode = random.randint(10000, 99999)
        size = random.randint(60, 500)
        numberOfRooms = random.randint(3, 8)
        numberOfBedrooms =  numberOfRooms - random.randint(1,3)
        numberOfBeds = numberOfBedrooms + random.randint(1,3)
        numberOfLivingSpaces = numberOfRooms - numberOfBedrooms
        servicesAvailable = fake.text(max_nb_chars=300) 
        pricePerNight = random.randint(30, 200)

        insertPropertyQuery = f"INSERT INTO Properties (OwnerID, CountryID, Title, PropertyDescription, \
                            City, Street, ZipCode, Size, NumberOfRooms, NumberOfBedrooms, NumberOfBeds, \
                            NumberOfLivingSpaces, ServicesAvailable, PricePerNight) VALUES (?, ?, ?, ?, \
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(insertPropertyQuery, ownerID, countryID, title, propertyDescription, city, street, zipCode, size, numberOfRooms, numberOfBedrooms, numberOfBeds, numberOfLivingSpaces, servicesAvailable, pricePerNight) 
        cursor.execute("SELECT @@IDENTITY AS ID;")
        propertyID = cursor.fetchone()[0]
        conn.commit()
        fillPropertyPhotos(connectionString, random.randint(2,5), propertyID)
        fillFeatures(connectionString, random.randint(5,10), propertyID, features[random.randint(0, len(features) - 1)][0])
    
    # print(str(propertyAmount) + " properties have been added to the database")
    conn.close()

# fillProperties('DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;', 2, 1, 1)