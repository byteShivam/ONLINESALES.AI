
-- Task-1 SQL Query

-- To generate the output report in SQL, assuming the data is stored in separate tables for each worksheet, you can use the following query:

SELECT DEPT_NAME, AVG(MONTHLY_SALARY) AS AVG_MONTHLY_SALARY
FROM Employee
GROUP BY DEPT_NAME
ORDER BY AVG_MONTHLY_SALARY DESC
LIMIT 3;

-- Assumptions:

-- The table for the Employee data is named "Employee."
-- The column for the department name is "DEPT_NAME."
-- The column for the monthly salary is "MONTHLY_SALARY."
-- The average monthly salary is calculated using the AVG function.
-- The report should list the top 3 departments based on average monthly salary, in descending order.

-- Test case:

-- Ensure that the query returns the correct results by running it against the database and comparing the output with the expected report.



