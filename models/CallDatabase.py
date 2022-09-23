import psycopg2
import os
import pandas as pd

def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(group_id, payer, product, cost, date)'
    postgres_insert_query = f"""INSERT INTO payment_data {table_columns} VALUES (%s,%s,%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功由錢錢管家掌握！"
    print(message)

    cursor.close()
    conn.close()
    
    return message

def line_calculate_money(time, group_id): #時間格式：西元年-兩位數月份
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    year = time[0]
    month = time[1]
    group = "('"+ group_id + "')"
    big = ["01", "03", "05", "07", "08", "10", "11"]
    if month in big:
        postgres_select_query = f"""SELECT * FROM payment_data 
                                WHERE group_id = {group}
                                AND date BETWEEN '{year}-{month}-01' AND '{year}-{month}-31';
                                """
    elif month == "02" and year % 4 == 0:
        postgres_select_query = f"""SELECT * FROM payment_data 
                                WHERE group_id = {group}
                                AND date BETWEEN '{year}-{month}-01' AND '{year}-{month}-29';
                                """
    elif month == "02" and year % 4 != 0:
        postgres_select_query = f"""SELECT * FROM payment_data 
                                WHERE group_id = {group}
                                AND date BETWEEN '{year}-{month}-01' AND '{year}-{month}-28';
                                """                            
    else:
        postgres_select_query = f"""SELECT * FROM payment_data 
                                WHERE group_id = {group}
                                AND date BETWEEN '{year}-{month}-01' AND '{year}-{month}-30';
                                """

    cursor.execute(postgres_select_query)
    raw_data = cursor.fetchall()
    data = pd.DataFrame(raw_data, columns = ['record_num', 'group', 'payer', 'product', 'cost', 'date'])
    
    cursor.close()
    conn.close()

    return data

def write_member_list(group, id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    member_data = (group, id)
    table_columns = '(group_id, member_id)'
    table_column = '(group_id, user_id)'
    print("1")
    postgres_insert_query = f"""INSERT INTO member_data {table_columns} VALUES (%s,%s);"""
    cursor.execute(postgres_insert_query, member_data)
    conn.commit()
    print("2")

    postgress_insert = f"""INSERT INTO record_data {table_column} VALUES (%s,%s);"""
    cursor.execute(postgress_insert, member_data)
    conn.commit()

    message = f"恭喜您成為錢錢管家服侍的對象！"
    print(message)

    cursor.close()
    conn.close()
    
    return message

def call_member_df(group_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group = "('"+ group_id + "')"
    postgres_select_query = f"""SELECT * FROM member_data 
                            WHERE group_id = {group};
                            """
    cursor.execute(postgres_select_query)
    raw_data = cursor.fetchall()
    
    if len(raw_data) != 0:
        data = pd.DataFrame(raw_data, columns = ['record_num', 'group_id', 'member_id'])
    else:
        data = "No data"
    
    cursor.close()
    conn.close()

    return data

def open_recorder(group_id, user_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    data = "TRUE"
    group_id = "('"+ group_id + "')"
    user_id = "('"+ user_id + "')"
    postgres_insert_query = f"""
                             UPDATE record_data 
                             SET condition = {data} 
                             WHERE group_id = {group_id} AND user_id = {user_id};
                             """

    cursor.execute(postgres_insert_query)
    conn.commit()

    cursor.close()
    conn.close()

def call_condition(group_id, user_id):
    
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group = "('"+ group_id + "')"
    user = "('"+ user_id + "')"
    postgres_select_query = f"""SELECT * FROM record_data 
                            WHERE group_id = {group} AND user_id = {user};
                            """
    cursor.execute(postgres_select_query)
    raw_data = cursor.fetchall()
    data = pd.DataFrame(raw_data, columns = ['record_num', 'group_id', 'user_id', 'condition', 'product', 'price', 'date'])
    
    cursor.close()
    conn.close()

    return data

def record_product(group_id, user_id, product_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    group = "('"+ group_id + "')"
    user = "('"+ user_id + "')"
    product = "('"+ product_list + "')"

    postgres_insert_query = f"""
                             UPDATE record_data 
                             SET product = {product} 
                             WHERE group_id = {group} AND user_id = {user};
                             """

    cursor.execute(postgres_insert_query)
    conn.commit()

    message = f"收到！"
    print(message)

    cursor.close()
    conn.close()
    
    return message

def record_price(group_id, user_id, data_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group_id = "('"+ group_id + "')"
    user_id = "('"+ user_id + "')"
    price = "('"+ data_list + "')"

    postgres_insert_query = f"""
                             UPDATE record_data 
                             SET price = {price} 
                             WHERE group_id = {group_id} AND user_id = {user_id};
                             """

    cursor.execute(postgres_insert_query)
    conn.commit()

    message = f"好的！最後一個問題！"
    print(message)

    cursor.close()
    conn.close()
    
    return message

def record_date(group_id, user_id, data_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    group_id = "('"+ group_id + "')"
    user_id = "('"+ user_id + "')"
    date = "('"+ data_list + "')"

    postgres_insert_query = f"""
                             UPDATE record_data 
                             SET date = {date} 
                             WHERE group_id = {group_id} AND user_id = {user_id};
                             """

    cursor.execute(postgres_insert_query)
    conn.commit()

    message = f"done！"
    print(message)

    cursor.close()
    conn.close()
    
    return message

def close_condition(group_id, user_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group_id = "('" + group_id + "')"
    user_id = "('" + user_id + "')"
    delete_temp_data = f'''UPDATE record_data 
                           SET condition = NULL WHERE group_id = {group_id} AND user_id = {user_id};
                           UPDATE record_data
                           SET product = NULL WHERE group_id = {group_id} AND user_id = {user_id};
                           UPDATE record_data
                           SET price = NULL WHERE group_id = {group_id} AND user_id = {user_id};
                           UPDATE record_data
                           SET date = NULL WHERE group_id = {group_id} AND user_id = {user_id};'''

    cursor.execute(delete_temp_data)
    conn.commit()
    message = f"完成！"
    print(message)

    cursor.close()
    conn.close()

def delete_data(group_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group_id = group_id
    delete_member_data = f'''DELETE FROM member_data WHERE group_id = '{group_id}';'''
    delete_data = f'''DELETE FROM payment_data WHERE group_id = '{group_id}';'''
    delete_record_data = f'''DELETE FROM record_data WHERE group_id = '{group_id}';'''

    cursor.execute(delete_member_data)
    conn.commit()
    cursor.execute(delete_data)
    conn.commit()
    cursor.execute(delete_record_data)
    conn.commit()

    message = f"感謝您這段時間的照顧，您過去的紀錄都刪掉囉~"
    print(message)

    cursor.close()
    conn.close()

def create_calculator(group_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    table_columns = '(group_id)'
    postgres_insert_query = f"""INSERT INTO calculate_data {table_columns} VALUES (%s);"""
    cursor.execute(postgres_insert_query, group_id)
    conn.commit()
    cursor.close()
    conn.close()

def open_calculator(group_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    data = "TRUE"
    group_id = "('"+ group_id + "')"
    postgres_insert_query = f"""
                             UPDATE calculate_data 
                             SET condition = {data} 
                             WHERE group_id = {group_id};
                             """

    cursor.execute(postgres_insert_query)
    conn.commit()

    message = f"請問您要算哪個月的帳呢？\n請用「西元年份-月份（兩位數）」的格式撰寫"
    print(message)

    cursor.close()
    conn.close()

def get_calculate_condition(group_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group = "('"+ group_id + "')"
    postgres_select_query = f"""SELECT * FROM calculate_data 
                            WHERE group_id = {group};
                            """
    cursor.execute(postgres_select_query)
    raw_data = cursor.fetchall()
    data = pd.DataFrame(raw_data, columns = ['record_num', 'group_id', 'condition'])
    
    cursor.close()
    conn.close()

    return data

def close_calculator(group_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    group_id = "('" + group_id + "')"
    user_id = "('" + user_id + "')"
    delete_temp_data = f'''UPDATE calculate_data 
                           SET condition = NULL WHERE group_id = {group_id};'''
    cursor.execute(delete_temp_data)
    conn.commit()
    message = f"完成！"
    print(message)

    cursor.close()
    conn.close()