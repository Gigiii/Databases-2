CREATE TRIGGER TR_Customers
ON Customers
AFTER INSERT, UPDATE
AS
BEGIN
  DECLARE @Age INT, @CountryID INT
  SELECT @Age = Age, @CountryID = CountryID FROM inserted
  IF @Age < 18
  BEGIN
    ROLLBACK TRANSACTION
    RAISERROR ('User must be 18 or above', 16, 1)
    RETURN
  END
  IF NOT EXISTS (SELECT * FROM Countries WHERE CountryID = @CountryID)
  BEGIN
    ROLLBACK TRANSACTION
    RAISERROR ('Invalid country ID', 16, 1)
    RETURN
  END
END
