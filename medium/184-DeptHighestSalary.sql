SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
INNER JOIN Department ON Department.id = departmentId
WHERE (Department.id, Salary) IN (
SELECT departmentId, MAX(salary) AS Salary
FROM Employee
GROUP BY departmentId
);