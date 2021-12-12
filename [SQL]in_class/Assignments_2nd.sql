SELECT employees.first_name, employees.last_name, employees.department_id, departments.location_id, locations.city
    FROM employees, departments, locations
WHERE employees.department_id = departments.department_id 
    AND departments.location_id = locations.location_id 
    AND employees.first_name = 'David'
    AND salary.employees >= 6000;
