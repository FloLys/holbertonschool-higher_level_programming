-- List all records of second_table without rows with name value in desc order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
