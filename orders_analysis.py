from cleaning_data import load_clean_data
orders = load_clean_data()["orders"]
print(orders)

def analyze_order(Orders):
    revenue = Orders["Total_Price"].sum()
    total_orders = orders["Order_id"].nunique()
    average_order_value = orders["Total_Price"].mean()

    return{'Revenue':float(revenue),'Total_Orders':int(total_orders),'Average_order_value':float(average_order_value)}

# print(analyze_order(orders))

def monthly_orders(orders):
    orders['months'] = orders['Order_datetime'].dt.to_period('M').astype('str')
    return orders[['Order_id','months']].groupby(by = 'months').count()
print(monthly_orders(orders))


