-- creates the MySQL server user
-- create and grants create a new user and set a privileges
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT '1',
name VARCHAR(256));