-- Create the database
CREATE DATABASE IF NOT EXISTS mariadb-doordash-prod-db;
USE mariadb-doordash-prod-db;

-- Create the Users table
CREATE TABLE IF NOT EXISTS Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    RegistrationDate DATE
);
 
-- Create the Products table
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT
);

-- Create the Orders table
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    OrderDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create the OrderDetails table
CREATE TABLE IF NOT EXISTS OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


INSERT INTO Users (UserID, UserName, Email, RegistrationDate) VALUES
    (1, 'scriiiiiiiiiiiiiiiiiiiible', 'mafumafu@gmail.com', '2023-01-01'),
    (2, 'ruarua', 'mogumogu-station@gmail.com', '2023-02-15');


INSERT INTO Products (ProductID, ProductName, Price, StockQuantity) VALUES
    (1, 'Mcchicken', 1200.00, 50),
    (2, 'Fries, two cokes, and a cookie', 800.00, 100),
    (3, 'two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda', 100.00, 200);


INSERT INTO Orders (OrderID, UserID, OrderDate) VALUES
    (1, 1, '2023-03-10'),
    (2, 2, '2023-04-05');


INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
    (1, 1, 1, 2),
    (2, 1, 2, 1),
    (3, 2, 3, 5);
