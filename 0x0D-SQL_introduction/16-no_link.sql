-- lists all records of the table second_table
-- The list should be sorted by the number of records (descending)
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
