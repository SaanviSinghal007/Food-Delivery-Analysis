## customer analysis

from cleaning_data import load_clean_data

def customer_analysis(customer_df,Orders):
    total_customers = customer_df["Customer_id"].nunique()
    gender_count = customer_df['Gender'].value_counts()
    city = []
   
    for address in customer_df['Address']:
        city.append(address.split(',')[-1].strip())
    customer_df['city'] = city
    city_count = customer_df['city'].value_counts()
    repeted_customers = Orders["Customer_id"].value_counts()>1
    total_repeted_customers = repeted_customers.sum()
    new_customers = total_customers - total_repeted_customers

    return {'Total_customers':total_customers,
            'Gender_count':gender_count,
            'City_count':city_count,
            'repeted_customers':int(total_repeted_customers),
            'New_customers':int(new_customers)}
            
customer_df = load_clean_data()['customers']
orders_df = load_clean_data()["orders"]
Res_df = load_clean_data()['rest']
# print(customer_analysis (customer_df))
print(orders_df.columns)
print(Res_df.columns)
print(customer_analysis(customer_df,orders_df))




