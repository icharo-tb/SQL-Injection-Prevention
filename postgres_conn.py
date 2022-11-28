import psycopg2
from config_parser import config


def connect_db(employee_data):

    conn = None
    try:
        params = config()

        print(f'Connecting to PostgreSQL Database...\n')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        query = """INSERT INTO employees_01 (name, surname, age, department) VALUES (%s,%s,%s,%s);"""

        print(f'Reading data...')
        for employee in employee_data:
            cur.execute(query,employee)

        conn.commit()
        cur.close()
    except (Exception,psycopg2.DatabaseError) as e:
        print(f'Error: {e}')
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__=='__main__':

    data = [("John","Smith",34,"HHRR"),("Allen","Kenway",23,"Consulting"),("Oliver","Atom",26,"Marketing"),
    ("Francis","Uter",47,"IT"),("Eleanor","Cubosky",35,"Marketing"),("Sarah","Tarh",24,"Marketing"),
    ("Emily","Connor",47,"IT"),("Hanzo","Hattori",45,"Consulting"),("Charles","Reigberg",34,"HHRR")]

    connect_db(data)