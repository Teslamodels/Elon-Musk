from insert_category import insert_category
from insert_product import insert_product


Title = input("Title, please: ")

insert_category(Title = Title)



Title = input("Title, please: ") 
Expiration_date = input("Expiration date, please: ")
Price = float(input("Price, please: "))
Category_id = int(input("Category id, please: "))

insert_product(Title = Title, Expiration_date = Expiration_date, Price = Price, Category_id = Category_id)
