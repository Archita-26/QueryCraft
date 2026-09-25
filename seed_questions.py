from database import SessionLocal
from models import Question

db = SessionLocal()

questions = [
    {"title": "Employees in IT department", "description": "Get all employees in IT department", "difficulty": "Easy", "topic": "WHERE", "expected_query": "SELECT * FROM employees WHERE department = 'IT'"},
    {"title": "Employee names only", "description": "Show only names of all employees", "difficulty": "Easy", "topic": "SELECT", "expected_query": "SELECT name FROM employees"},
    {"title": "Employees earning less than 50000", "description": "Find employees with salary below 50000", "difficulty": "Easy", "topic": "WHERE", "expected_query": "SELECT * FROM employees WHERE salary < 50000"},
    {"title": "Employees sorted by salary", "description": "Show employees ordered by salary ascending", "difficulty": "Easy", "topic": "ORDER BY", "expected_query": "SELECT * FROM employees ORDER BY salary ASC"},
    {"title": "Employees sorted by name", "description": "Show employees ordered alphabetically by name", "difficulty": "Easy", "topic": "ORDER BY", "expected_query": "SELECT * FROM employees ORDER BY name ASC"},
    {"title": "Total number of employees", "description": "Count total employees in the table", "difficulty": "Easy", "topic": "AGGREGATE", "expected_query": "SELECT COUNT(*) FROM employees"},
    {"title": "Average salary", "description": "Find average salary of all employees", "difficulty": "Easy", "topic": "AGGREGATE", "expected_query": "SELECT AVG(salary) FROM employees"},
    {"title": "Total salary expense", "description": "Find sum of all employee salaries", "difficulty": "Easy", "topic": "AGGREGATE", "expected_query": "SELECT SUM(salary) FROM employees"},
    {"title": "Lowest paid employee", "description": "Find employee with minimum salary", "difficulty": "Medium", "topic": "ORDER BY", "expected_query": "SELECT * FROM employees ORDER BY salary ASC LIMIT 1"},
    {"title": "Top 2 highest paid employees", "description": "Find the 2 highest paid employees", "difficulty": "Medium", "topic": "ORDER BY", "expected_query": "SELECT * FROM employees ORDER BY salary DESC LIMIT 2"},
    {"title": "Employees not in Sales", "description": "Find employees who are not in Sales department", "difficulty": "Medium", "topic": "WHERE", "expected_query": "SELECT * FROM employees WHERE department != 'Sales'"},
    {"title": "Departments with average salary", "description": "Show average salary per department", "difficulty": "Medium", "topic": "GROUP BY", "expected_query": "SELECT department, AVG(salary) FROM employees GROUP BY department"},
    {"title": "Max salary per department", "description": "Find highest salary in each department", "difficulty": "Medium", "topic": "GROUP BY", "expected_query": "SELECT department, MAX(salary) FROM employees GROUP BY department"},
    {"title": "Employees with name starting with A", "description": "Find employees whose name starts with letter A", "difficulty": "Medium", "topic": "LIKE", "expected_query": "SELECT * FROM employees WHERE name LIKE 'A%'"},
    {"title": "Employees in Sales or HR", "description": "Get employees who are in Sales or HR department", "difficulty": "Medium", "topic": "WHERE", "expected_query": "SELECT * FROM employees WHERE department IN ('Sales', 'HR')"},
    {"title": "Employees with salary between range", "description": "Find employees earning between 40000 and 55000", "difficulty": "Medium", "topic": "WHERE", "expected_query": "SELECT * FROM employees WHERE salary BETWEEN 40000 AND 55000"},
    {"title": "Distinct departments", "description": "List all unique departments", "difficulty": "Easy", "topic": "SELECT", "expected_query": "SELECT DISTINCT department FROM employees"},
    {"title": "Departments with more than 1 employee", "description": "Find departments having more than 1 employee", "difficulty": "Hard", "topic": "GROUP BY", "expected_query": "SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 1"},
    {"title": "Second highest salary", "description": "Find the second highest salary among employees", "difficulty": "Hard", "topic": "SUBQUERY", "expected_query": "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)"},
    {"title": "Employees earning above average", "description": "Find employees who earn more than average salary", "difficulty": "Hard", "topic": "SUBQUERY", "expected_query": "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)"},
]

for q in questions:
    new_q = Question(**q)
    db.add(new_q)

db.commit()
db.close()
print("Questions added successfully!")