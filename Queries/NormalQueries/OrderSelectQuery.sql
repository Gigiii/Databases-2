SELECT Orders.OrderID, Customers.FirstName, Orders.CheckInDate, Orders.CheckOutDate, Orders.TotalPrice
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID WHERE Totalprice > 500 ORDER BY OrderID;