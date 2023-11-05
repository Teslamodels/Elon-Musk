import psycopg2
from psycopg2 import Error


def insert_data():
    try:
        connection = psycopg2.connect(user = 'YOU WRITE!', password = 'YOU WRITE!', host = 'YOU WRITE!', port = 5432, database = 'YOU WRITE!')
        cursor = connection.cursor()

        cursor.execute("""SELECT Product.id, Product.Title, Product.category_id, Category.id, Category.Title FROM Product INNER JOIN Category ON Product.Category_id = Category.id;""")
        
        User = cursor.fetchall()

        return User

    except(Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Successfully closed!")

print(insert_data())