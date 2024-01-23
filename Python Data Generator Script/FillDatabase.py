import pyodbc
from FillCustomers import fillCustomers
from FillCountries import fillCountries
from FillOwners import fillOwners
from FillFeatureType import fillFeatureType
from FillAdministrators import fillAdministrators
from FillCreditCardType import fillCreditCardType

connectionString = 'DRIVER={SQL Server};SERVER=DESKTOP-BUGKGO7;DATABASE=HouseRentalDB;UID=Admin;PWD=xJuKV0I5KdjDbFJ;'
amountOfCustomers = 800
amountOfOwners = 300
amountOfAdministrators = 15
fillCountries(connectionString)
fillFeatureType(connectionString)
fillAdministrators(connectionString, amountOfAdministrators)
fillCreditCardType(connectionString)
fillOwners(connectionString, amountOfOwners)
fillCustomers(connectionString, amountOfCustomers)