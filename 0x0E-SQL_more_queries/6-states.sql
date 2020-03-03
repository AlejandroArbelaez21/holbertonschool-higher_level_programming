-- creates the MySQL server user
-- create and grants create a new user and set a privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
CONSTRAINT states PRIMARY KEY (id));