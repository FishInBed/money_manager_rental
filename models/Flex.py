from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FlexSendMessage

import configparser

from models import utils, CallDatabase, flexTemplate

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))

def call_housekeeper(event):
    user_id = event.source.user_id
    group_id = event.source.group_id
    if event.message.text == '召喚錢錢管家':
        member_data = CallDatabase.call_member_df(group_id)
        if isinstance(member_data, str) == False:
            condition = []
            for i in member_data["member_id"]:
                solo_condition = user_id == i
                condition.append(solo_condition)
            
            if True not in condition:
                line_bot_api.reply_message(
                    event.reply_token,
                    FlexSendMessage(
                    alt_text = '哈囉我是錢錢管家~',
                    contents = flexTemplate.default_flex_template()
                        )
            )
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    FlexSendMessage(
                    alt_text = '哈囉我是你的錢錢管家~',
                    contents = flexTemplate.old_flex_template()
                        )
            )
        else:
            line_bot_api.reply_message(
                    event.reply_token,
                    FlexSendMessage(
                    alt_text = '哈囉我是錢錢管家~',
                    contents = flexTemplate.default_flex_template()
                        )
            )

def call_manual(event):
    if "call_manual" in event.postback.data:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '錢錢管家的打開方式',
                contents = flexTemplate.manual()
            )
        )

