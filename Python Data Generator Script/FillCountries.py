import pyodbc

def fillCountries(connectionString):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    countries = cursor.execute('SELECT * FROM Countries')

    #If empty insert 3 example countries
    if countries.fetchall() == []:
        insertCountriesQuery = ["INSERT INTO Countries (CountryCode, Title) VALUES (383, 'Kosovo')", 
                    "INSERT INTO Countries (CountryCode, Title) VALUES (995, 'Georgia')",
                    "INSERT INTO Countries (CountryCode, Title) VALUES (351, 'Portugal')"]

        for script in insertCountriesQuery:
            cursor.execute(script)
        conn.commit()
    else:
        print("The Countries are already inserted into the database")
    conn.close()

