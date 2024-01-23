import pyodbc
import random
import names
from faker import Faker

def fillReviews(connectionString, reviewAmount, propertyID, customerID):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')

    for x  in range(0, reviewAmount):
        title = fake.text(max_nb_chars=50)
        reviewDescription = fake.text(max_nb_chars=500)
        cleanlinessRating = round(random.random() * 5, 1)
        accuracyRating = round(random.random() * 5, 1)
        checkInRating = round(random.random() * 5, 1)
        communicationRating = round(random.random() * 5, 1)
        locationRating = round(random.random() * 5, 1)
        valueRating = round(random.random() * 5, 1)
        overallRating = round((cleanlinessRating + accuracyRating + checkInRating + communicationRating + locationRating + valueRating) / 6, 2)
        insertReviewQuery = f"INSERT INTO Reviews (PropertyID, CustomerID, OverallRating, CleanlinessRating, \
                            AccuracyRating, CheckInRating, CommunicationRating, LocationRating, ValueRating, Title, \
                            ReviewDescription) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(insertReviewQuery, propertyID, customerID, overallRating, cleanlinessRating,
                        accuracyRating, checkInRating, communicationRating, locationRating, valueRating, title, reviewDescription) 

    conn.commit()
    # print(str(reviewAmount) + " reviews have been added to the database")
    conn.close()

# fillReviews('DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;', 2, 1, 1)