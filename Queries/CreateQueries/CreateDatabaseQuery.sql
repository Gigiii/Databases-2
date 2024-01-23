CREATE DATABASE HouseRentalDB
ON PRIMARY
  ( NAME='HouseRentalDB_Primary',
    FILENAME=
       'c:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\data\HouseRentalDB_Prm.mdf',
    SIZE=80MB,
    FILEGROWTH=2MB),
FILEGROUP HouseRentalDB_FG1
  ( NAME = 'HouseRentalDB_FG1_Dat1',
    FILENAME =
       'c:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\data\HouseRentalDB_FG1_1.ndf',
    SIZE = 20MB,
    FILEGROWTH=2MB),
  ( NAME = 'HouseRentalDB_FG1_Dat2',
    FILENAME =
       'c:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\data\HouseRentalDB_FG1_2.ndf',
    SIZE = 20MB,
    FILEGROWTH=2MB)
LOG ON
  ( NAME='HouseRentalDB_log',
    FILENAME =
       'c:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\data\HouseRentalDB.ldf',
    SIZE=20MB,
    FILEGROWTH=2MB);
GO


ALTER DATABASE HouseRentalDB 
  MODIFY FILEGROUP HouseRentalDB_FG1 DEFAULT;
GO

USE HouseRentalDB;
GO

CREATE TABLE Countries (
	
	CountryID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	CountryCode varchar(3),
	Title varchar(100) NOT NULL
)
;


CREATE TABLE CreditCardType(

	CreditCardTypeID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	Title varchar(100) NOT NULL,
	Type bit NOT NULL
)
;


CREATE TABLE Customers (

    CustomerID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	CountryID int NOT NULL FOREIGN KEY REFERENCES Countries(CountryID),
    FirstName varchar(50) NOT NULL,
	LastName varchar(70) NOT NULL,
	Age int NOT NULL,
	Gender bit NOT NULL,
    IdentificationDocumentType varchar(255),
    IdentificationDocumentPhoto varchar(512),
	FacePhoto varchar(512),
	City varchar(100) NOT NULL,
    Street varchar(100),
	ZipCode varchar(10),
	PhoneNumber varchar(25),
	Email varchar(320) NOT NULL,
	Password varchar(100) NOT NULL,
	AccountStatus bit NOT NULL
)
;



CREATE TABLE Owners (

    OwnerID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	CountryID int NOT NULL FOREIGN KEY REFERENCES Countries(CountryID),
    FirstName varchar(50) NOT NULL,
	LastName varchar(70) NOT NULL,
	Age int NOT NULL,
	Gender bit NOT NULL,
    IdentificationDocumentType varchar(255) NOT NULL,
    IdentificationDocumentPhoto varchar(512) NOT NULL,
	FacePhoto varchar(512) NOT NULL,
	City varchar(100) NOT NULL,
    Street varchar(100) NOT NULL,
	ZipCode varchar(10) NOT NULL,
	PhoneNumber varchar(25) NOT NULL,
	Email varchar(320) NOT NULL,
	Password varchar(100) NOT NULL,
	BankAccountNumber varchar(70) NOT NULL,
	AccountStatus bit NOT NULL
)
;


CREATE TABLE Administrators  (

	AdministratorID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	Username varchar(100) NOT NULL, 
	Password varchar(255) NOT NULL, 
	Email varchar(320) NOT NULL, 
	FullName varchar(120) NOT NULL, 
	Role tinyInt NOT NULL, 
	LastLoginDate datetime DEFAULT GETDATE(), 
	AccountStatus bit NOT NULL
)
;



CREATE TABLE Properties (

	PropertyID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	OwnerID int NOT NULL FOREIGN KEY REFERENCES Owners(OwnerID),
	CountryID int NOT NULL FOREIGN KEY REFERENCES Countries(CountryID),
	Title varchar(50) NOT NULL,
	PropertyDescription varchar(500),
	City varchar(100) NOT NULL,
    Street varchar(100) NOT NULL,
	ZipCode varchar(10) NOT NULL,
	Size int NOT NULL,
	NumberOfRooms smallint NOT NULL,
	NumberOfBedrooms smallint NOT NULL,
	NumberOfBeds smallint NOT NULL,
	NumberOfLivingSpaces smallint NOT NULL,
	ServicesAvailable varchar(300),
	PricePerNight int NOT NULL,
)
;


CREATE TABLE PropertyPhotos(

	PhotoID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	PropertyID int NOT NULL FOREIGN KEY REFERENCES Properties(PropertyID),
	Link varchar(400) NOT NULL,
	Title varchar(80)

)
;


CREATE TABLE FeatureType(

	FeatureTypeID int NOT NULL PRIMARY KEY IDENTITY(1,1),
	Title varchar(250)  NOT NULL,

)
;


CREATE TABLE Features (

  FeatureID int NOT NULL PRIMARY KEY IDENTITY(1,1),
  PropertyID int NOT NULL FOREIGN KEY REFERENCES Properties(PropertyID),
  TypeID int NOT NULL FOREIGN KEY REFERENCES FeatureType(FeatureTypeID),
  Label varchar(250) NOT NULL,
  Description varchar(400) NOT NULL,
)
;


CREATE TABLE Orders (

 OrderID int NOT NULL PRIMARY KEY IDENTITY(1,1),
 CustomerID int NOT NULL FOREIGN KEY REFERENCES Customers(CustomerID),
 OwnerID int NOT NULL FOREIGN KEY REFERENCES Owners(OwnerID),
 PropertyID int NOT NULL FOREIGN KEY REFERENCES Properties(PropertyID),
 CreditCardTypeID int NOT NULL FOREIGN KEY REFERENCES CreditCardType(CreditCardTypeID),
 CreditCardNumber varchar(16) NOT NULL,
 CreditCardExpirationDate date NOT NULL,
 CreditCardCCV int NOT NULL,
 TotalPrice int NOT NULL,
 AmountPaid int NOT NULL,
 DurationOfStay int NOT NULL,
 CheckInDate date NOT NULL,
 CheckOutDate date NOT NULL,
 OrderStatus varchar(70) NOT NULL,
 CreationTimestamp datetime DEFAULT GETDATE(),
)
;


CREATE TABLE Invoices(

InvoiceID int NOT NULL PRIMARY KEY IDENTITY(1,1),
OrderID int NOT NULL FOREIGN KEY REFERENCES Orders(OrderID) ,
InvoiceFullPaymentDate date,
IsClosed bit NOT NULL, 
AmountAlreadyPaid int NOT NULL,
InvoiceDate date,
)
;
GO

CREATE TABLE Reviews (

 ReviewID int NOT NULL PRIMARY KEY IDENTITY(1,1),
 PropertyID int NOT NULL FOREIGN KEY REFERENCES Properties(PropertyID),
 CustomerID int NOT NULL FOREIGN KEY REFERENCES Customers(CustomerID),
 OverallRating float NOT NULL,
 CleanlinessRating float NOT NULL,
 AccuracyRating float NOT NULL,
 CheckInRating float NOT NULL,
 CommunicationRating float NOT NULL,
 LocationRating float NOT NULL,
 ValueRating float NOT NULL,
 Title varchar(50) NOT NULL,
 ReviewDescription varchar(500),
)
;
GO