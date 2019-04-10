import psycopg2
class recipe:
    def connect(self,recipetableobj):
        conn = None
        try:
            print('Connecting to user database...' )
            conn=psycopg2.connect('dbname=recipedb user=user password=root')
            print('db')
            table_name="recipe"
            cur=conn.cursor()
            cur.execute('''INSERT INTO %s (description,author,videolink)
                           VALUES(%%s,%%s,%%s)''' %table_name,[recipetableobj.description,recipetableobj.author,recipetableobj.videolink])
            conn.commit()
            print('Committed..')


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
class recipetable:
    def __init__(self,description,author,videolink):
        self.description=description
        self.author=author
        self.videolink=videolink


recipetableobj=recipetable('Mutton_curry','Mia_Kitchen','miakitchen.chickencurry')


rec=recipe()
rec.connect(recipetableobj)