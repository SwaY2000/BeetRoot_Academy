import sqlite3

db = sqlite3.connect('task1.db')

sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS customers(
login TEXT,
password TEXT,
cash BIGINT)""")

db.commit()

def add(name_table):
    user_login = input()
    user_password = input()

    sql.execute(f"SELECT login FROM {name_table}")

    if sql.fetchone() != user_login:
        print(sql.fetchall())
        sql.execute(f"INSERT INTO {name_table} VALUES('{user_login}', {user_password}, {0})")
        print('alright')
        db.commit()
    print(f'Statements add to table: {name_table}')

def read(name_table):
    print(f'Statements from table: {name_table}')
    for value in sql.execute(f"SELECT * FROM {name_table}"):
        print(value)

def rename(name_table, rename):
    sql.execute(f"ALTER TABLE {name_table} RENAME TO {rename}")
    read(rename)
    db.commit()

def add_column(name_table, name_column, type_table):
    sql.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_table}")
    # sql.execute(f"INSERT INTO {name} VALUES('{10}')")
    db.commit()

def update_statement(name_table, where_update_statement, statements_for_update:int, essence, essence_will_update):
    sql.execute(f"UPDATE {name_table} SET {where_update_statement}={statements_for_update}"
                f" WHERE {essence}='{essence_will_update}'")
    db.commit()

def delete_statements(name_table, essence, essence_will_delete):
    sql.execute(f"DELETE FROM {name_table}"
                f" WHERE {essence} LIKE '%{essence_will_delete}%'")
    print(f'Statement {essence}->{essence_will_delete} from {name_table} deleted successful')
    db.commit()

add('customers')

add('customers')

read('customers')

rename('customers', 'users')

add_column('users', 'years', 'INT')

read('users')

update_statement('users', 'years', 20, 'login', 'danil')

read('users')

delete_statements('users', 'login', 'dasha')

read('users')
