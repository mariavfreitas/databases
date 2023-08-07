
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS "order" CASCADE;
DROP TABLE IF EXISTS pay CASCADE;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS process CASCADE;
DROP TABLE IF EXISTS department CASCADE;
DROP TABLE IF EXISTS workplace CASCADE;
DROP TABLE IF EXISTS works CASCADE;
DROP TABLE IF EXISTS office CASCADE;
DROP TABLE IF EXISTS warehouse CASCADE;
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS contains CASCADE;
DROP TABLE IF EXISTS supplier CASCADE;
DROP TABLE IF EXISTS delivery CASCADE;


CREATE TABLE customer (
    cust_no INTEGER PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address VARCHAR(255)
);
CREATE TABLE "order" (
    order_no INTEGER PRIMARY KEY,
    cust_no INTEGER NOT NULL REFERENCES customer ON DELETE CASCADE,
    date DATE NOT NULL
    --order_no must exist in contains
);
CREATE TABLE pay(
    order_no INTEGER PRIMARY KEY REFERENCES "order" ON DELETE CASCADE,
    cust_no INTEGER NOT NULL REFERENCES customer ON DELETE CASCADE
);
CREATE TABLE employee(
    ssn VARCHAR(20) PRIMARY KEY,
    TIN VARCHAR(20) UNIQUE NOT NULL,
    bdate DATE,
    name VARCHAR NOT NULL
    --age must be >=18
);
CREATE TABLE process(
    ssn VARCHAR(20) REFERENCES employee ON DELETE CASCADE,
    order_no INTEGER REFERENCES "order" ON DELETE CASCADE,
    PRIMARY KEY (ssn, order_no)
);
CREATE TABLE department(
    name VARCHAR PRIMARY KEY
);
CREATE TABLE workplace(
    address VARCHAR PRIMARY KEY,
    lat NUMERIC(8, 6) NOT NULL,
    long NUMERIC(9, 6) NOT NULL,
    UNIQUE(lat, long)
    --address must be either in warehouse or office
    --address cannot be both in warehouse and office simultaneously
);
CREATE TABLE office(
    address VARCHAR(255) PRIMARY KEY REFERENCES workplace ON DELETE CASCADE
);
CREATE TABLE warehouse(
    address VARCHAR(255) PRIMARY KEY REFERENCES workplace ON DELETE CASCADE
);
CREATE TABLE works(
    ssn VARCHAR(20) REFERENCES employee ON DELETE CASCADE,
    name VARCHAR(200) REFERENCES department ON DELETE CASCADE,
    address VARCHAR(255) REFERENCES workplace ON DELETE CASCADE,
    PRIMARY KEY (ssn, name, address)
);
CREATE TABLE product(
    SKU VARCHAR(25) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description VARCHAR,
    price NUMERIC(10, 2) NOT NULL,
    ean NUMERIC(13) UNIQUE
);
CREATE TABLE contains(
    order_no INTEGER REFERENCES "order" ON DELETE CASCADE,
    SKU VARCHAR(25) REFERENCES product ON DELETE CASCADE,
    qty INTEGER,
    PRIMARY KEY (order_no, SKU)
);
CREATE TABLE supplier (
    TIN VARCHAR(20) PRIMARY KEY,
    name VARCHAR(200),
    address VARCHAR(255),
    SKU VARCHAR(25) REFERENCES product ON DELETE CASCADE,
    date DATE
);

CREATE TABLE delivery(
    address VARCHAR(255) REFERENCES warehouse ON DELETE CASCADE,
    TIN VARCHAR(20) REFERENCES supplier ON DELETE CASCADE ,
    PRIMARY KEY (address, TIN)
);



INSERT INTO customer (cust_no, name, email, phone, address)
VALUES
(1, 'John Doe', 'johndoe@email.com', '1234567890', 'Avenida de Saboia, 9, 2765-580, Estoril'),
(2, 'Jane Smith', 'janesmith@email.com', '9876543210', 'Avenida de Saboia, 11, 2765-581, Estoril'),
(3, 'Maria Silva', 'mariasilva@email.pt', '5551234567', 'Rua das Flores, 123,1209-809, Lisboa'),
(4, 'João Santos', 'joaosantos@email.pt', '5559876543', 'Avenida Central, 456,2670-993,Loures'),
(5, 'Sofia Pereira', 'sofiapereira@email.pt', '5555555555', 'Avenida Central, 400,2670-990,Loures'),
(6, 'Pedro Fernandes', 'pedrofernandes@email.pt', '5556666666', 'Rua das Flores, 120,1209-800, Lisboa');



INSERT INTO "order" (order_no,cust_no,date)
VALUES
(1, 1,'2023-05-01'),
(2, 2,'2020-03-09'),
(3, 2,'2023-01-01'),
(4, 4,'2023-01-05'),
(5, 6,'2023-01-15'),
(6, 5,'2023-05-20'),
(7, 3,'2020-01-19'),
(8, 3,'2017-10-01'),
(9, 5,'2021-09-04'),
(10, 1,'2006-11-19'),
(11, 6, '2022-05-13');


INSERT INTO pay (order_no, cust_no)
VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 4),
(6, 5);





INSERT INTO employee (ssn, TIN, bdate, name)
VALUES
(123456789, 'TIN123', '1990-01-01', 'Jane Smith'),
(987654321, 'TIN589', '1995-03-15', 'John Johnson'),
(654321987, 'TIN987', '1988-09-10', 'Anabela Sousa'),
(321987654, 'TIN654', '1992-05-20', 'Luís Ferreira'),
(789654123, 'TIN389', '1995-03-15', 'Mariana Gonçalves'),
(456123789, 'TIN456', '1990-07-25', 'Ricardo Santos'),
(159357456, 'TIN369', '1993-05-12', 'Ana Costa');



INSERT INTO process (ssn,order_no)
VALUES
(123456789,1),
(987654321,1),
(654321987,1),
(321987654,2),
(654321987,3),
(789654123,4),
(456123789,5),
(789654123,6),
(456123789,7),
(789654123,8),
(456123789,9),
(159357456,4),
(789654123,5),
(987654321,11);



INSERT INTO department (name)
VALUES
('RH'),
('Finanças'),
('TI'),
('Vendas'),
('Marketing');



INSERT INTO workplace (address, lat, long)
VALUES
('Rua da Rosa, 2, 1200-700,Lisboa', 40.1234, -74.5678),
('Avenida Infante Santo, 12, 1200-701,Lisboa', 40.9876, -74.1234),
('Avenida Alvares Cabral, 9, 1200-702,Lisboa', 41.2345, -75.6789),
('Rua Mirante, 4, 1200-703,Lisboa', 40.5678, -74.9012),
('Rua das Madres, 27, 1200-704,Lisboa', 41.3456, -75.4321),
('Rua dos Anjos, 78,1200-705,Lisboa', 41.1234, -8.9876),
('Avenida dos Aliados, 10, 1200-706,Lisboa', 40.4321, -8.9012),
('Rua das Oliveiras, 54, 1200-707,Lisboa', 40.5678, -8.3456),
('Rua das Margaridas, 321, 1200-708,Lisboa', 41.9876, -8.7654),
('Avenida dos Cravos, 456, 1200-709,Lisboa', 40.5432, -8.1234),
('Travessa dos Lírios, 654, 1200-710,Lisboa', 40.7890, -8.4321),
('Rua das Violetas, 123, 1200-711,Lisboa', 41.2346, -8.9867),
('Rua dos Cravos, 789, 1200-712, Lisboa', 40.5423, -8.1243);



INSERT INTO office (address)
VALUES
('Rua da Rosa, 2, 1200-700,Lisboa'),
('Avenida Infante Santo, 12, 1200-701,Lisboa'),
('Avenida Alvares Cabral, 9, 1200-702,Lisboa'),
('Rua Mirante, 4, 1200-703,Lisboa'),
('Rua das Madres, 27, 1200-704,Lisboa'),
('Rua dos Anjos, 78,1200-705,Lisboa');



INSERT INTO warehouse (address)
VALUES
('Avenida dos Aliados, 10, 1200-706,Lisboa'),
('Rua das Oliveiras, 54, 1200-707,Lisboa'),
('Rua das Margaridas, 321, 1200-708,Lisboa'),
('Avenida dos Cravos, 456, 1200-709,Lisboa'),
('Travessa dos Lírios, 654, 1200-710,Lisboa'),
('Rua das Violetas, 123, 1200-711,Lisboa'),
('Rua dos Cravos, 789, 1200-712, Lisboa');


INSERT INTO works (ssn, name,address)
VALUES
(123456789,'Vendas','Avenida dos Aliados, 10, 1200-706,Lisboa'),
(987654321,'RH','Rua dos Anjos, 78,1200-705,Lisboa'),
(159357456,'Vendas','Avenida dos Aliados, 10, 1200-706,Lisboa'),
(654321987,'Finanças','Rua da Rosa, 2, 1200-700,Lisboa'),
(321987654,'TI','Rua das Margaridas, 321, 1200-708,Lisboa'),
(789654123,'Vendas','Avenida dos Aliados, 10, 1200-706,Lisboa'),
(456123789,'Marketing','Avenida Alvares Cabral, 9, 1200-702,Lisboa');



INSERT INTO product (sku, name, description, price,ean)
VALUES
(1, 'Produto 1', 'Descrição 1', 9.99,123),
(2, 'Produto 2', 'Descrição 2', 19.99,124),
(3, 'Produto 3', 'Descrição 3', 29.99,125),
(4, 'Produto 4', 'Descrição 4', 39.99,126),
(5, 'Produto 5', 'Descrição 5', 99.99,127),
(6, 'Produto 6', 'Descrição 6', 59.99,128),
(7, 'Produto 7', 'Descrição 7', 59.99,120),
(8, 'Produto 8', 'Descrição 8', 69.99,121),
(9, 'Produto 9', 'Descrição 9', 79.99,122),
(10, 'Produto 10', 'Descrição 10', 89.99,987),
(11, 'Produto 11', 'Descrição 11', 99.99,986),
(12, 'Produto 12', 'Descrição 12', 109.99,999);



INSERT INTO contains (order_no, sku, qty)
VALUES
(1, 1, 5),
(2, 2, 3),
(1, 3, 2),
(1, 4, 3),
(2, 5, 2),
(3, 6, 1),
(4, 7, 2),
(5, 8, 3),
(6, 9, 1),
(7, 10, 4),
(8, 11, 2),
(9, 12, 1),
(10, 4, 6),
(11, 5, 7);




INSERT INTO supplier (TIN, name, address,SKU,date)
VALUES
('TIN456', 'Fornecedor 1', 'Rua dos lirios, 8,2670-990,Loures',1,'2023-05-01'),
('TIN789', 'Fornecedor 2', 'Rua de Londres,9,2670-991,Loures',2,'2023-05-03'),
('TIN987', 'Fornecedor 3', 'Rua das Amoras, 1,2670-992,Loures',3,'2022-12-09'),
('TIN654', 'Fornecedor 4', 'Avenida das Palmeiras, 20,2670-993,Loures',4,'2023-03-09'),
('TIN321', 'Fornecedor 5', 'Rua dos Carvalhos, 5,2670-994,Loures',5,'2023-05-05'),
('TIN879', 'Fornecedor 6', 'Rua das Azáleas, 10,2670-995,Loures',6,'2023-02-17'),
('TIN546', 'Fornecedor 7', 'Avenida das Camélias, 30,2670-996,Loures',7,'2023-05-19'),
('TIN123', 'Fornecedor 8', 'Travessa dos Lírios, 5,2670-997,Loures',8,'2023-01-03');



INSERT INTO delivery (address,TIN)
VALUES
('Avenida dos Aliados, 10, 1200-706,Lisboa','TIN456'),
('Rua das Oliveiras, 54, 1200-707,Lisboa','TIN789'),
('Rua das Margaridas, 321, 1200-708,Lisboa','TIN123'),
('Avenida dos Cravos, 456, 1200-709,Lisboa','TIN654'),
('Travessa dos Lírios, 654, 1200-710,Lisboa','TIN546'),
('Rua das Violetas, 123, 1200-711,Lisboa','TIN321'),
('Rua dos Cravos, 789, 1200-712, Lisboa','TIN987');