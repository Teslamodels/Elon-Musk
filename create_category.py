import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = 'YOU WRITE!', password = 'YOU WRITE!', host = 'YOU WRITE!', port = 5432, database = 'YOU WRITE!')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Category(
                   ID SERIAL PRIMARY KEY,
                   Title VARCHAR(100) NOT NULL
                   );""")
    
    connection.commit()

    print("Successfull!")

except(Exception, Error) as error:
    print("Error", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Successfully closed!")
        