from cleaning_data import load_clean_data
import pandas as pd

orders = load_clean_data()['orders']
delivery = load_clean_data()['delivery']

print(orders,delivery)

def analyze_delivery(orders,delivery):
    df = pd.merge(orders,delivery[['Order_id','Delivery_time']],how= 'left',on= ['Order_id'])
    print(df)
    df['delivery_minutes'] = df['Delivery_time'] - df['Order_datetime']
    return df 

def delivery_status(delivery):
    return delivery['Status'].value_counts()

print(delivery_status(delivery))

# print(analyze_delivery(orders,delivery))


