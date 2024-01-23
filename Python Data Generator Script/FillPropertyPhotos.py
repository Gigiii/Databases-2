import pyodbc
import random
import names
from faker import Faker

def fillPropertyPhotos(connectionString, photoAmount, propertyID):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')

    for x  in range(0, photoAmount):
        title = fake.text(max_nb_chars=80)
        link = fake.url()
        insertPhotoQuery = f"INSERT INTO PropertyPhotos (PropertyID, Link, Title) VALUES (?, ?, ?);"
        cursor.execute(insertPhotoQuery, propertyID, link, title) 

    conn.commit()
    # print(str(photoAmount) + " photos have been added to the database")
    conn.close()

# fillPropertyPhotos('DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;', 2, 1)