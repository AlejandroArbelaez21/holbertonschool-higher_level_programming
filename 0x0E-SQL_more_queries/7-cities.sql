-- creates the MySQL server user
-- create and grants create a new user and set a privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL UNIQUE AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
CONSTRAINT states PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES cities(id));