import pandas as pd

from sqlalchemy import create_engine 

def connect_database():
    try:
        engine = create_engine(url="mysql+mysqldb://root:bhoomi@localhost/food_delivery")

        # return engine
    except:
        # print("Database connection failed",e)
        return None,False
    else:
        return engine,True

# if connect_database():
#     print("Database connected successfully")

def connect_tables():
    try:
        engine,_ = connect_database()
        customers = pd.read_sql_query("select * from customers;",engine)
        rest= pd.read_sql_query("select * from Restaurants;",engine)
        menu_items = pd.read_sql_query("select * from Menu_items;",engine)
        orders = pd.read_sql_query("select * from Orders;",engine)
        delivery = pd.read_sql_query("select * from Delivery;",engine)
        # return customers,rest,menu_items,orders,delivery
    except:
        print("Error loading tables:")
        # raise
        
    else:
        return customers,rest,menu_items,orders,delivery


# connect_tables()

