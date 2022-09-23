import pandas as pd

def prepare_record(text):
    text_list = text.split('\n')
    
    record_list = []
      
    for i in text_list[1:]:
        temp_list = i.split(' ')
        temp_product = temp_list[0]    
        temp_cost = int(temp_list[1])
        temp_date = temp_list[2]
        record = [temp_product, temp_cost, temp_date]
        record_list.append(record)
            
    return record_list

def prepare_calculation(text):
    text_list = text.split('\n')
    time = str(text_list[1]).split("-")
    return time

def individual_cost(data_frame, member_id_list):
    paylist = []
    for i in member_id_list['member_id']:
        new_df = data_frame[data_frame['payer'] == i]
        total_pay = [i, new_df['cost'].sum()]
        paylist.append(total_pay)
    
    return paylist

def give_and_take(paylist, average):
    total_list = []
    for i in paylist:
        total = [i[0], i[1]-int(average)]
        total_list.append(total)
    
    return(total_list)

def check_list_length(df, user_id):
    clean_df = df.loc[(df['user_id'] == user_id)]
    target = clean_df["data_list"][0]
    length = len(target.split(","))
    return length

def flex_prepare_record(data): 
    length = len(data["product"][0].split(" "))
    product_list = data["product"][0].split(" ")
    price_list = data["price"][0].split(" ")
    date_list = data["date"][0].split(" ")
    for i in range(len(price_list)):
        price_list[i] = int(price_list[i])
    data_list = []
    for i in range(length):
        data_tuple = (data["group_id"][0], data["user_id"][0], product_list[i], price_list[i], date_list[i])
        data_list.append(data_tuple)
    return data_list
