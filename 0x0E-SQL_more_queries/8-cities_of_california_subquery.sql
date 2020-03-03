-- creates the MySQL server user
-- create and grants create a new user and set a privileges
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;