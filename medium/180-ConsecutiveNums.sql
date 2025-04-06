SELECT DISTINCT(initial.num) AS ConsecutiveNums
From Logs as initial
LEFT JOIN Logs AS plus1 on plus1.id = initial.id + 1
LEFT JOIN Logs AS plus2 on plus2.id = initial.id + 2
WHERE initial.num = plus1.num AND plus1.num = plus2.num;