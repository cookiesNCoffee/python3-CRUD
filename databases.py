import sqlite3

def main():
    conn = sqlite3.connect('test.db')

    conn.execute('drop table if exists employee')
    conn.execute('create table employee (id int, name text)')

    #Create
    conn.execute('insert into employee (id, name) values (1, "Nirjhor")')
    conn.execute('insert into employee (id, name) values (2, "Turjoy")')
    conn.execute('insert into employee (id, name) values (3, "Badhon")')
    conn.execute('insert into employee (id, name) values (4, "Babar")')
    conn.commit()

    #Retrieve
    print("Original: \n")
    cursor = conn.execute('select * from employee')
    for row in cursor:
        print(row)

    #Update
    conn.execute('update employee set name="Nayeem" where id=1')
    print("\n\nUpdated: \n")
    cursor = conn.execute('select * from employee')
    for row in cursor:
        print(row)

    #Delete
    conn.execute('delete from employee where id=2')
    print("\n\nDeleted: \n")
    cursor = conn.execute('select * from employee where id>2')
    for row in cursor:
        print(row)
    
if __name__ == "__main__" : main()
