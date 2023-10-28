SELECT name
FROM Customers
WHERE Customers.id NOT IN (SELECT customerId FROM Orders)
