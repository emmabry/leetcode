SELECT * 
FROM Cinema
WHERE id % 2 != 0
AND NOT description = 'boring'
ORDER BY rating DESC;