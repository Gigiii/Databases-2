import pyodbc
import random
import names
from faker import Faker

def fillAdministrators(connectionString, administratorAmount):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    fake = Faker('en_GB')

    for x in range(0, administratorAmount):
        insertUserQuery = ""
        if random.randint(0,1) == 0:
            firstName = names.get_first_name(gender="male")
        else:
            firstName = names.get_first_name(gender="female")
        username = fake.bban()
        lastName = names.get_last_name()
        fullName = firstName+lastName
        email = firstName + "." + lastName + "@gmail.com"
        password = firstName[:1] + lastName[:1] + str(random.randint(1000,1000000)) + fake.iban()
        accountStatus = 0
        role = random.randint(0,4)
        insertUserQuery = f"INSERT INTO Administrators (Username, Password, Email, FullName, \
                            Role, AccountStatus) VALUES (?, ?, ?, ?, ?, ?);"
        cursor.execute(insertUserQuery, username, password, email, fullName, role, accountStatus)

    conn.commit()
    print(str(administratorAmount) + " administrators have been added to the database")
    conn.close()