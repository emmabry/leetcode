SELECT (SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1)
AS SecondHighestSalary;

-- Wrapping in subquery will cause NULL to be returned instead of an empty result.