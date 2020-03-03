-- create and grants create a new user and set a privileges
-- create and grants create a new user and set a privileges
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;