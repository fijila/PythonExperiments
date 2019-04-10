import psycopg2


def connect():
    conn = None
    try:
        print('Connecting to the user1 database...')
        conn = psycopg2.connect('dbname=test2db user=user1 password=root')
        print('db')
        cur = conn.cursor()
        cur.execute('''CREATE  TABLE company(
            ID int primary key NOT NULL,
            Name TEXT NOT NULL,
            Age int NOT NULL

        )''')
        conn.commit()
        print("committed")




    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
