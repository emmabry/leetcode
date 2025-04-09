CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
IF N < 1 THEN
RETURN;
END IF;

  RETURN QUERY (
    SELECT (SELECT DISTINCT Employee.salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET N - 1)
    AS SecondHighestSalary
  );
END;
$$ LANGUAGE plpgsql;