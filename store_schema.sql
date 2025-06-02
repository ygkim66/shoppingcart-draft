PRAGMA foreign_keys=off;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    username        varchar(50) not null PRIMARY KEY,
    password        varchar(50) not null,
    name            varchar(50) not null,
    email           varchar(50) not null
);

DROP TABLE IF EXISTS items;
CREATE TABLE items (
    id              varchar(32) not null PRIMARY KEY,
    name            varchar(50) not null,
--    search_keyword  varchar(50) not null,--
    price           double(10) not null,
    type            varchar(50) not null,
    color           varchar(50),
    stock           int(6) not null,
    image           varchar(100)
);

DROP TABLE IF EXISTS pastOrders;
CREATE TABLE pastOrders (
    username            varchar(32) not null PRIMARY KEY,
    itemname            varchar(50) not null,
    itemtype            varchar(50) not null,
    itemquantity        varchar(50) not null
);
PRAGMA foreign_keys=on;

INSERT INTO users VALUES ('HectorP42', '324468', 'Hector Pearlman', 'hector@gmail.com');
INSERT INTO users VALUES ('YGKim', 'saf83nDas0', 'Y.G. Kim', 'yg@gmail.com');
INSERT INTO users VALUES ('MaxE', 'Pdf93Ln.eS', 'Maxwell Eichholz', 'max@gmail.com');
INSERT INTO users VALUES ('RuthAM', '39rR3na)Dks', 'Ruth Morehouse', 'ruth@gmail.com');
INSERT INTO users VALUES ('testuser', 'testpass', 'Test', 'test@gmail.com');

INSERT INTO items VALUES ('B1111', 'Strawberry Protein Bar', 3.00, 'Protein Bar', null, 1000, 'static\images\strawberrybar.jpg'); 
INSERT INTO items VALUES ('B2111', 'Blueberry Protein Bar', 2.00, 'Protein Bar', null, 1000, 'static\images\blueberrybar.jpg'); 
INSERT INTO items VALUES ('B3111', 'Chocolate Protein Bar',1.00 , 'Protein Bar', null, 1000, 'static\images\chocolatebar.jpg'); 
INSERT INTO items VALUES ('D1111', 'Chocolate Protein Shake', 2.00, 'Protein Shake', null, 1000, 'static\images\chocolateshake.jpg');
INSERT INTO items VALUES ('D2111', 'Vanilla Protein Shake',3.00 , 'Protein Shake', null, 1000, 'static\images\vanillashake.jpg');
INSERT INTO items VALUES ('D3111', 'Strawberry Protein Shake',4.00 , 'Protein Shake', null, 1000, 'static\images\strawberryshake.jpg');
INSERT INTO items VALUES ('D4111', 'Marshmallow Protein Shake', 3.00, 'Protein Shake', null, 1000, 'static\images\marshmallowshake.jpg');
INSERT INTO items VALUES ('C1111', 'Creatine Monohydrate',15.00 , 'Creatine', null, 10000, 'static\images\creatine.jpg');
INSERT INTO items VALUES ('P1111', 'Preworkout Powder',10.00 , 'Caffeine', null, 1000, 'static\images\preworkout.jpg');
INSERT INTO items VALUES ('P2111', 'Monster Energy Drink',4.00 , 'Caffeine', null, 1000, 'static\images\monster.jpg');

