import psycopg2
from psycopg2 import Error


def insert_category(Title):
    try:
        connection = psycopg2.connect(user = 'YOU WRITE!', password = 'YOU WRITE!', host = 'YOU WRITE!', port = 5432, database = 'YOU WRITE!')
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Category(Title)
                       VALUES(%s);""", (Title, ))
        
        connection.commit()

        print("Successfull!")

    except(Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Successfully closed!")
            