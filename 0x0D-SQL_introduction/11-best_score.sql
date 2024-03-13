-- List all recordw of the table
-- Records are orderd by descending score
SELECT `score`, `name`
from `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
