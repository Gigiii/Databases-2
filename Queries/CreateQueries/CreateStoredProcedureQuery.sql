CREATE PROCEDURE GetPropertiesOverPricePerNight @PricePerNight DECIMAL(5, 0)
AS
BEGIN
    SELECT *
    FROM Properties
    WHERE PricePerNight > @PricePerNight;
END;

GO