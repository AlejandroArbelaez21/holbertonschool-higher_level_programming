-- displays the number of records with id = 89 in the table first_table
-- count commands that count the once that are the words in specific in table of a databases
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month > 6 and month < 9 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
