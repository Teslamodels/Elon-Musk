import psycopg2
from psycopg2 import Error


def insert_product(Title, Expiration_date, Price, Category_id):
    try:
        connection = psycopg2.connect(user = 'YOU WRITE!', password = 'YOU WRITE!', host = 'YOU WRITE!', port = 5432, database = 'YOU WRITE!')
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Product(Title, Expiration_date, Price, Category_id)
                       VALUES(%s, %s, %s, %s);""", (Title, Expiration_date, Price, Category_id))
        
        connection.commit()

        print("Successfull!")

    except(Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Successfully closed!")
            