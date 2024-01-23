SELECT 
    O.FirstName, 
    O.LastName, 
    O.Age, 
    P.PricePerNight,
    (SELECT AVG(PricePerNight) FROM Properties WHERE OwnerID IN 
        (SELECT OwnerID FROM Owners WHERE Age > 35)) as AveragePricePerNight
FROM 
    Owners O
INNER JOIN 
    Properties P ON O.OwnerID = P.OwnerID
WHERE 
    O.Age > 30;
