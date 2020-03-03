-- displays the number of records with id = 89 in the table first_table
-- count commands that count the once that are the words in specific in table of a databases
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
