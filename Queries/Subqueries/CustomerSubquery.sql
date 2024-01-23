SELECT 
    C.FirstName, 
    C.LastName, 
    C.Age, 
    C.Gender,
    O.DurationOfStay,
    O.AmountPaid,
    (SELECT AVG(AmountPaid) FROM Orders WHERE CustomerID IN 
        (SELECT CustomerID FROM Customers WHERE Gender = 1 AND Age BETWEEN 18 AND 25)) as AverageAmountPaid
FROM 
    Customers C
INNER JOIN 
    Orders O ON C.CustomerID = O.CustomerID
WHERE 
    C.Gender = 1 AND C.Age BETWEEN 18 AND 25;
