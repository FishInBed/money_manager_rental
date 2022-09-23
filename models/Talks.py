from __future__ import unicode_literals
from ast import Call
import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage

import configparser
import math
import pandas as pd

# 我們的函數
from models import utils, CallDatabase, flexTemplate

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))

# 請 LINE 幫我們存入資料
def insert_record(event):
    user_id = event.source.user_id
    group_id = event.source.group_id
    
    if '召喚錢錢管家記一下' in event.message.text:
        
        try:
            record_list = utils.prepare_record(event.message.text)
            for i in record_list:
                i.append(group_id)
                i.append(user_id)
            
            record_tuple = []
            for i in record_list:
                trans = (i[3], i[4], i[0], i[1], i[2])
                record_tuple.append(trans)
            reply = CallDatabase.line_insert_record(record_tuple)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
                )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='嗚嗚失敗了')
            )

        return True
    else:
        return False

def calculate_money(event):
    group_id = event.source.group_id
    group_member_id_df = CallDatabase.call_member_df(group_id)

    if '召喚錢錢管家算一下' in event.message.text:
        try:
            time = utils.prepare_calculation(event.message.text)
            data_df = CallDatabase.line_calculate_money(time, group_id)           
            average = round(data_df['cost'].sum()/len(group_member_id_df['member_id']))
            individual_cost_list = utils.individual_cost(data_df, group_member_id_df)
            
            for i in group_member_id_df['member_id']:
                existence = 0
                for j in individual_cost_list:
                    if i == j[0]:
                        existence = existence+1
                if existence == 0:
                    add_data = [i, 0]
                    individual_cost_list.append(add_data)
            
            raw_result = utils.give_and_take(individual_cost_list, average)
            for i in raw_result:
                profile = line_bot_api.get_group_member_profile(group_id, i[0])
                member_name = str(profile.display_name)
                i[0] = member_name

            message = ""
            for i in range(len(raw_result)):
                if i != 0:
                    if raw_result[i][1] < 0:
                        sentence = "\n" + raw_result[i][0] + "要再付" + str(abs(raw_result[i][1])) + "元"
                    elif raw_result[i][1] == 0:
                        sentence = "\n" + raw_result[i][0] + "不用付錢"
                    else:
                        sentence = "\n" + raw_result[i][0] + "要收到" + str(raw_result[i][1]) + "元"
                    message = message+sentence
                else:
                    if raw_result[i][1] < 0:
                        sentence = raw_result[i][0] + "要再付" + str(abs(raw_result[i][1])) + "元"
                    elif raw_result[i][1] == 0:
                        sentence = raw_result[i][0] + "不用付錢"
                    else:
                        sentence = raw_result[i][0] + "要收到" + str(raw_result[i][1]) + "元"
                    message = message+sentence

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=message)
                )
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='嗚嗚失敗了')
            )

        return True
    else:
        return False

def join_member(event):
    
    if '我決定雇用你了' in event.message.text:
        user_id = event.source.user_id
        group_id = event.source.group_id
        member_data = CallDatabase.call_member_df(group_id)
        
        if isinstance(member_data, str) == False:
            condition = []
            for i in member_data["member_id"]:
                solo_condition = user_id == i
                condition.append(solo_condition)

            if True not in condition:
                try:
                    reply = CallDatabase.write_member_list(group_id, user_id)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=reply)
                        )

                except:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text='嗚嗚失敗了')
                    )

                return True

            else:
                try:
                    reply = "您本來就已經是我的雇主囉~"
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=reply)
                    )
                except:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text='嗚嗚失敗了')
                    )

                return True
        else:
            try:
                reply = CallDatabase.write_member_list(group_id, user_id)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply)
                )

            except:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='嗚嗚失敗了')
                )

            return True
    else:
        return False

def flex_join_member(event):

        if 'new_group_member' in event.postback.data:
            user_id = event.source.user_id
            group_id = event.source.group_id
            member_data = CallDatabase.call_member_df(group_id)
            
            if isinstance(member_data, str) == False:
                condition = []
                for i in range(len(member_data["member_id"])):
                    solo_condition = user_id == member_data["member_id"][i]
                    condition.append(solo_condition)

                if True not in condition:
                    
                    try:
                        reply = CallDatabase.write_member_list(group_id, user_id)
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )

                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text='嗚嗚失敗了')
                        )

                    return True
                else:
                    try:
                        reply = "您本來就已經是我的雇主囉~"
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                            )
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text='怪怪的')
                        )
                    return True
            
            else:
                try:
                    reply = CallDatabase.write_member_list(group_id, user_id)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=reply)
                    )

                except:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text='啊咧？')
                    )

                return True
        else:
            return False

def record_insert_data(event):
    if event.postback.data == "insert_group_data":
        try:
            CallDatabase.open_recorder(event.source.group_id, event.source.user_id)
            print("打開了")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                text = "請問這筆款項的名稱是什麼呢？\n如果不只一筆的話請用空格把它們分開喔~"
                )
            )
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                text = "好像出了什麼問題，請聯絡開發者TT"
                )
            )

def record_product(event):
    try:    
        group_id = event.source.group_id
        user_id = event.source.user_id
        data = CallDatabase.call_condition(group_id, user_id)
        print("拿出來")
        if data["condition"][0] == "true" and data["product"][0] is None:
            if " " not in event.message.text:
                product_list = event.message.text
                reply = CallDatabase.record_product(group_id, user_id, product_list)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text = reply + "\n那您花了多少錢買它呢？"
                        )
                    )
                        
            else:
                product_list = event.message.text
                reply = CallDatabase.record_product(event.source.group_id, event.source.user_id, product_list)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text = reply + "\n那您花了多少錢買它們呢？\n記得要把各個款項照剛剛的順序用空格分開喔~"
                        )
                    )
        else:
            print("條件不符") 
    except Exception as e: 
        print("有問題喔")
        print(e)

def record_money(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        try:
            data = CallDatabase.call_condition(event.source.group_id, event.source.user_id)
            print("拿出來")
            if data["product"][0] is not None and data["price"][0] is None:
                    if " " in event.message.text:
                        data_list = event.message.text
                        reply = CallDatabase.record_price(event.source.group_id, event.source.user_id, data_list)
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(
                                text = reply + "\n這是什麼時候花的錢呢？\n請用年份(四位數字)-月份(兩位數字）-日期（兩位數字）的格式撰寫\n不同筆之間記得也要用空格分開喔~"
                                )
                            )
                            
                    else:
                        data_list = event.message.text
                        reply = CallDatabase.record_price(event.source.group_id, event.source.user_id, data_list)
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(
                                text = reply + "\n這是什麼時候花的錢呢？\n請用年份(四位數字)-月份(兩位數字）-日期（兩位數字）的格式撰寫"
                                )
                            )
            else:
                print("條件不符")
        except Exception as e: 
            print("有問題喔")
            print(e)

def record_data(event):
    try:
        data = CallDatabase.call_condition(event.source.group_id, event.source.user_id)
        print("拿出來")
        if data["price"][0] is not None and data["date"][0] is None:
                data_list = event.message.text
                CallDatabase.record_date(event.source.group_id, event.source.user_id, data_list)
        else: 
            print("條件不符")
        new_data = CallDatabase.call_condition(event.source.group_id, event.source.user_id)
        print("再拿出來")
        if new_data["date"][0] is not None:      
                record_list = utils.flex_prepare_record(new_data)
                reply = CallDatabase.line_insert_record(record_list)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text = reply
                        )
                    )
                print("ok")
                CallDatabase.close_condition(event.source.group_id, event.source.user_id)
                print("大功告成")                
        
        else: 
            print("怪怪")
    except Exception as e: 
        print("有問題喔")
        print(e)

def open_calculator(event):
    if event.postback.data == "calculate_money":
        try:
            reply = CallDatabase.open_calculator(event.source.group_id)
            print("打開了")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                text = reply
                )
            )
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                text = "好像出了什麼問題，請聯絡開發者TT"
                )
            )

def flex_calculate_money(event):
    try:
        group_id = event.source.group_id
        group_member_id_df = CallDatabase.call_member_df(group_id)
        data = CallDatabase.get_calculate_condition(group_id)
        if data["condition"][0] == "true":
            try:
                time = utils.prepare_calculation(event.message.text)
                data_df = CallDatabase.line_calculate_money(time, group_id)           
                average = round(data_df['cost'].sum()/len(group_member_id_df['member_id']))
                individual_cost_list = utils.individual_cost(data_df, group_member_id_df)
                
                for i in group_member_id_df['member_id']:
                    existence = 0
                    for j in individual_cost_list:
                        if i == j[0]:
                            existence = existence+1
                    if existence == 0:
                        add_data = [i, 0]
                        individual_cost_list.append(add_data)
                
                raw_result = utils.give_and_take(individual_cost_list, average)
                for i in raw_result:
                    profile = line_bot_api.get_group_member_profile(group_id, i[0])
                    member_name = str(profile.display_name)
                    i[0] = member_name

                message = ""
                for i in range(len(raw_result)):
                    if i != 0:
                        if raw_result[i][1] < 0:
                            sentence = "\n" + raw_result[i][0] + "要再付" + str(abs(raw_result[i][1])) + "元"
                        elif raw_result[i][1] == 0:
                            sentence = "\n" + raw_result[i][0] + "不用付錢"
                        else:
                            sentence = "\n" + raw_result[i][0] + "要收到" + str(raw_result[i][1]) + "元"
                        message = message+sentence
                    else:
                        if raw_result[i][1] < 0:
                            sentence = raw_result[i][0] + "要再付" + str(abs(raw_result[i][1])) + "元"
                        elif raw_result[i][1] == 0:
                            sentence = raw_result[i][0] + "不用付錢"
                        else:
                            sentence = raw_result[i][0] + "要收到" + str(raw_result[i][1]) + "元"
                        message = message+sentence

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                    )
                CallDatabase.close_calculator(group_id)
            except:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='嗚嗚失敗了')
                )

    except:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='嗚嗚失敗了')
                ) 

