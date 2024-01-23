SELECT FirstName, LastName, Age, IdentificationDocumentType, Countries.Title FROM Owners FULL OUTER JOIN Countries ON 
Owners.CountryID = Countries.CountryID WHERE FirstName = 'James';