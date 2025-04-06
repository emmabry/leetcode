SELECT orig.score, COUNT(DISTINCT comp.score) + 1 AS rank
FROM Scores AS orig
LEFT JOIN Scores AS comp ON comp.score > orig.score
GROUP BY orig.score, orig.id
ORDER BY rank;


-- using DENSE_RANK()
SELECT score,
DENSE_RANK() OVER (
   ORDER BY score DESC
) as rank
FROM Scores;