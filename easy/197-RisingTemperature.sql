-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

SELECT today.id FROM Weather today
INNER JOIN Weather yday ON today.recordDate = yday.recordDate + INTERVAL 1 DAY
WHERE today.temperature > yday.temperature;