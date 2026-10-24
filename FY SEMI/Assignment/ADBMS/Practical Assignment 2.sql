show databases;

create database company;

use company;

-- Create a table EMPLOYEE with following schema:  
-- (Emp_no, E_name, E_address, E_ph_no, Dept_no, Dept_name,Job_id, Designation, Salary)  
-- Write SQL statements for the following queries.

Create Table EMPLOYEE ( 
EMP_no INT PRIMARY KEY, 
E_name VARCHAR (50), 
E_address VARCHAR (100), 
e_ph_no VARCHAR(15), 
Dept_no INT, 
Dept_name VARCHAR (50), 
Job_id INT, 
Designation VARCHAR (30), 
Salary VARCHAR (12), 
Experience INT, 
Join_date date  
);


DESC EMPLOYEE;
 
INSERT INTO EMPLOYEE VALUES 
(1, 'Pranav', 'Pune', '9370243210', 10, 'IT', 101, 'CLERK' , 12000 , 3, '1980-01-19'), 
(2, 'Aayush', 'Mumbai', '8421543211', 20, 'HR', 102, 'ANALYST' , 18000 , 5, '1981-05-01'), 
(3, 'Prasad', 'Pune', '8208543212', 10, 'IT', 103, 'MANAGER' , 25000 , 8, '1982-02-10'), 
(4, 'Gaurav', 'Nashik', '9022543213', 30, 'SALES', 104, 'CLERK' , 9000 , 2, '1981-12-03'), 
(5, 'Rohan', 'Pune', '7498543214', 20, 'HR', 105, 'ANALYST' , 20000 , 6, '1981-12-17'), 
(6, 'Rudra', 'Mumbai', '9955543215', 10, 'IT', 106, 'MANAGER' , 30000 , 10, '1983-04-15'), 
(7, 'Aditya', 'Pune', '9120543216', 30, 'SALES', 107, 'PRESIDENT' , 40000 , 15, '1984-06-20'), 
(8, 'Pavan', 'Mumbai', '9076543217', 20, 'HR', 108, 'CLERK' , 11000 , 1, '1981-01-05');


SELECT * FROM EMPLOYEE; 

-- 1. List the E_no, E_name, Salary of all employees working for MANAGER. 
 
SELECT EMP_no, E_name, salary 
FROM EMPLOYEE 
WHERE Designation = 'MANAGER';

-- 2. Display all the details of the employee whose salary is more than 10000. 

SELECT * 
FROM EMPLOYEE  
WHERE Salary > 10000; 

-- 3. List the employees in ascending order of Designations of those who joined after 1981. 

SELECT*  
FROM EMPLOYEE  
WHERE Join_date >= '1982-01-01' 
ORDER BY DESIGNATION ASC; 

-- 4. List the employees along with their Experience and Daily Salary.  

SELECT E_name, Experience, Salary , salary / 30 As Daily_Salary 
FROM EMPLOYEE; 

-- 5. List the employees who are either ‘CLERK’ or ‘ANALYST’ .

SELECT *  
FROM EMPLOYEE  
WHERE DESIGNATION = 'CLERK' 
OR DESIGNATION = 'ANALYST'; 

-- 6. List the employees who joined on 1-MAY-1981, 3-DEC-1981, 17-DEC-1981, 19-JAN-1980.

SELECT *  
FROM EMPLOYEE  
WHERE Join_date IN ( 
'1981-05-01', 
'1981-12-03', 
'1981-12-17', 
'1980-01-19' 
);

-- 7. List the employees who are working for Deptno 10 or20. 

SELECT *  
FROM EMPLOYEE  
WHERE dept_no IN (10, 20);

-- 8. List the Enames that start with ‘S’.

INSERT INTO EMPLOYEE VALUES 
(9, 'Shashank', 'Sangli', '8989502410', 30, 'IT', 109, 'CLERK' , 2000 , 3, '1981-01-19');

SELECT E_name 
FROM EMPLOYEE 
WHERE E_NAME LIKE 'S%';

-- 9. Write a SQL query to find the highest salary. Return the highest salary.

ALTER TABLE EMPLOYEE 
MODIFY COLUMN Salary DECIMAL (10, 2);

SELECT * FROM EMPLOYEE;

SELECT MAX(Salary) AS Highest_Salary 
FROM EMPLOYEE; 

-- 10. Display the name and the first five characters of the name starting with ‘H’ . List all the 
-- employees except ‘PRESIDENT’ & ‘MGR” in ascending order of Salaries.

UPDATE EMPLOYEE
SET E_name = "Hussain"
WHERE EMP_no = 5;

SELECT E_name 
FROM EMPLOYEE 
WHERE E_name Like 'H%'; 

SELECT E_name, substr(E_name,1,5) 
FROM EMPLOYEE
WHERE E_name LIKE 'H%';

SELECT E_name, LEFT(E_name,5) AS FIRST_FIVE
FROM EMPLOYEE
WHERE E_name LIKE 'H%';

SELECT * FROM EMPLOYEE;
-- 11. Display the minimum and maximum salary and Experience of the employee.

SELECT MIN(Salary) As MIN_Salary, 
MAX(salary) AS MAX_Salary, 
MIN(Experience) AS MIN_Experience, 
MAX(Experience) AS Max_Experience 
FROM EMPLOYEE; 

-- 12. Display the total salary of all employees. 

SELECT SUM(Salary)AS Total_Salary 
FROM EMPLOYEE;

-- 13. Write a query to display the average salary of employees working in IT department.

SELECT AVG(Salary) AS AVG_Salary 
FROM EMPLOYEE 
Where Dept_name = 'IT'; 

-- 14. Display the Distinct salary of an employee. 

SELECT distinct SALARY 
FROM EMPLOYEE; 

-- 15. Drop the Database.

DROP DATABASE Company;
    