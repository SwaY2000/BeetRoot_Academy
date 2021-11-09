import sqlite3

def get_statements_first_last_name():
    db = sqlite3.connect('HW.db')
    sql = db.cursor()
    sql.execute("""SELECT first_name, last_name FROM employees""")
    return sql.fetchall()

def get_statements_id():
    db = sqlite3.connect('HW.db')
    sql = db.cursor()
    sql.execute("""SELECT first_name, last_name, employee_id FROM employees""")
    return sql.fetchall()

def get_all_sorted_statements():
    db = sqlite3.connect('HW.db')
    sql = db.cursor()
    sql.execute("""SELECT * FROM employees ORDER BY first_name""")
    return sql.fetchall()

def get_salary():
    db = sqlite3.connect('HW.db')
    sql = db.cursor()
    sql.execute("""SELECT first_name, last_name, salary FROM employees""")
    return sql.fetchall()

def get_max_min():
    db = sqlite3.connect('HW.db')
    sql = db.cursor()
    sql.execute("""SELECT first_name as 'First_Name', last_name as "Last_Name", salary as 'MIN_Salary' 
    FROM employees WHERE salary = (SELECT MAX(salary) FROM employees)""")
    temp = sql.fetchall()
    sql.execute("""SELECT first_name as 'First_Name', last_name as "Last_Name", salary as 'MIN_Salary' 
        FROM employees WHERE salary = (SELECT MIN(salary) FROM employees)""")
    temp = [*temp, *sql.fetchall()]
    return temp


def read_table(name_table):
    db = sqlite3.connect('task1.db')
    sql = db.cursor()
    sql.execute(f"""SELECT * FROM {name_table}""")
    rows = sql.fetchall()
    [print(row) for row in rows]

def add_full_name(name_table, *args):
    db = sqlite3.connect('task1.db')
    sql = db.cursor()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}(first_name TEXT, last_name TEXT)""")
    for statements in args:
        sql.execute(f"INSERT INTO {name_table} VALUES ('{statements[0]}', '{statements[1]}')")
        db.commit()

def add_id_employees(name_table, *args):
    db = sqlite3.connect('task1.db')
    sql = db.cursor()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}(first_name TEXT, last_name TEXT, ID INT)""")
    for statements in args:
        sql.execute(f"INSERT INTO {name_table} VALUES ('{statements[0]}', '{statements[1]}', '{statements[2]}')")
        db.commit()

def add_sorted_all_statements(name_table, *args):
    db = sqlite3.connect('task1.db')
    sql = db.cursor()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}(ID INT, first_name VARCHAR, 
    last_name VARCHAR, email VARCHAR, 
    phone_number VARCHAR, hire_date DATE, job_id VARCHAR, salary DECIMAL , commission_pct NUMBER ,
     manager_id INT, department_id INT, Avg_Salary NUMERIC)""")
    for statements in args:
        sql.execute(f"""INSERT INTO {name_table} VALUES ('{statements[1]}', '{statements[1]}', '{statements[2]}',
                    '{statements[3]}', '{statements[4]}', '{statements[5]}', '{statements[6]}', '{statements[7]}',
                    '{statements[8]}', '{statements[9]}', '{statements[10]}', '{statements[11]}')""")
        db.commit()

def add_salary_pf(name_table, *args):
    db = sqlite3.connect('task1.db')
    sql = db.cursor()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}(first_name VARCHAR, last_name VARCHAR, salary FLOAT, PF FLOAT)""")
    for statements in args:
        sql.execute(f"INSERT INTO {name_table} VALUES ('{statements[0]}', '{statements[1]}', '{statements[2]}', '{(statements[2]*(12/100))}')")
        db.commit()

def add_max_min_salary(name_table, *args):
    db = sqlite3.connect('task1.db')
    sql = db.cursor()
    sql.execute(
        f"""CREATE TABLE IF NOT EXISTS {name_table}(full_name_max VARCHAR, max_salary FLOAT, full_name_min VARCHAR, min_salary FLOAT)""")
    for statements in args:
        sql.execute(
            f"INSERT INTO {name_table} VALUES ('{statements[0][0]+' '+statements[0][1]}', '{statements[0][2]}','{statements[1][0]+' '+statements[1][1]}', '{statements[1][2]}')")
        db.commit()




add_full_name('all_employees', *get_statements_first_last_name())
read_table('all_employees')

add_full_name('id', *get_statements_id())
read_table('id')

add_sorted_all_statements('sorted_in_first_name', *get_all_sorted_statements())
read_table('sorted_in_first_name')

add_salary_pf('PF', *get_salary())
read_table('PF')

add_max_min_salary('max_and_min_salary', get_max_min())
read_table('max_and_min_salary')
