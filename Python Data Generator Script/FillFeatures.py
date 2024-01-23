import pyodbc
import random
import names
from faker import Faker

def fillFeatures(connectionString, featureAmount, propertyID, typeID):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')

    for x  in range(0, featureAmount):
        label = fake.text(max_nb_chars=40)
        featureDescription = fake.text(max_nb_chars=100)
        insertPhotoQuery = f"INSERT INTO Features (PropertyID, TypeID, Label, Description) VALUES (?, ?, ?, ?);"
        cursor.execute(insertPhotoQuery, propertyID, typeID, label, featureDescription) 

    conn.commit()
    # print(str(featureAmount) + " features have been added to the database")
    conn.close()

# fillFeatures('DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;', 2, 1, 1)