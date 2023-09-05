-- 570. Managers with at Least 5 Direct Reports
-- Medium
-- 669
-- 64
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Employee

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | department  | varchar |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table indicates the name of an employee, their department, and the id of their manager.
-- If managerId is null, then the employee does not have a manager.
-- No employee will be the manager of themself.
 

-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.

-- The result format is in the following example.


SELECT Manager.name
FROM Employee Employee, Employee Manager
WHERE Manager.id = Employee.managerId
GROUP BY Employee.managerId
HAVING COUNT(Employee.managerId) >= 5