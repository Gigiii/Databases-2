import pyodbc

def fillFeatureType(connectionString):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    featureType = cursor.execute('SELECT * FROM FeatureType')

    #If empty insert all featureTypes
    if featureType.fetchall() == []:
        insertFeatureTypeQuery = ["INSERT INTO FeatureType (Title) VALUES ('Bathroom')", "INSERT INTO FeatureType (Title) VALUES ('Bedroom')", 
                                  "INSERT INTO FeatureType (Title) VALUES ('Safety')", "INSERT INTO FeatureType (Title) VALUES ('Laundry')",
                                  "INSERT INTO FeatureType (Title) VALUES ('Internet')", "INSERT INTO FeatureType (Title) VALUES ('Entertainment')",
                                  "INSERT INTO FeatureType (Title) VALUES ('Kitchen')", "INSERT INTO FeatureType (Title) VALUES ('Family')",
                                  "INSERT INTO FeatureType (Title) VALUES ('Location')", "INSERT INTO FeatureType (Title) VALUES ('AirConditioning')",
                                  "INSERT INTO FeatureType (Title) VALUES ('Outdoor')"]

        for script in insertFeatureTypeQuery:
            cursor.execute(script)
        conn.commit()
    else:
        print("The FeatureTypes are already inserted into the database")
    conn.close()

