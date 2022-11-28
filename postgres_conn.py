import psycopg2
from config_parser import config


def connect_db(employee_data):

    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        prepared = False

        prep_query = """PREPARE employees_01_prepared (varchar,varchar,smallint,varchar) AS
        INSERT INTO employees_01 (name, surname, age, department) VALUES (%s,%s,%s,%s);"""
        query = """EXECUTE employees_01_prepared (%s,%s,%s,%s);"""

        if prepared == False:
            cur.execute(prep_query,employee_data)
            prepared = True
        else:
            raise Exception

        if prepared == True:
            cur.execute(query,employee_data)
        else:
            raise Exception

        conn.commit()
        print(f'Uploaded: {employee_data}')
        cur.close()
    except (Exception,psycopg2.DatabaseError) as e:
        print(f'Error: {e}')
    finally:
        if conn is not None:
            conn.close()


if __name__=='__main__':

    data = [("John","Smith",34,"HHRR"),("Allen","Kenway",23,"Consulting"),("Oliver","Atom",26,"Marketing"),
    ("Francis","Uter",47,"IT"),("Eleanor","Cubosky",35,"Marketing"),("Sarah","Tarh",24,"Marketing"),
    ("Emily","Connor",47,"IT"),("Hanzo","Hattori",45,"Consulting"),("Charles","Reigberg",34,"HHRR")]

    for employee in data:
        connect_db(employee)