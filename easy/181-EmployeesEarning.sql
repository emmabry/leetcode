-- Write a solution to find the employees who earn more than their managers.

-- Return the result table in any order.

SELECT emp.name AS Employee
FROM Employee emp
LEFT JOIN Employee man ON emp.managerId = man.id
WHERE emp.salary > man.salary;