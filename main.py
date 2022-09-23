from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent, JoinEvent, FlexSendMessage, LeaveEvent

import configparser

from models import utils, Talks, Flex, flexTemplate, CallDatabase

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 消費紀錄
@handler.add(MessageEvent, message=TextMessage)
def reply_text_message(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reply = False
        
        if not reply:
            reply = Talks.insert_record(event)
        if not reply:
            reply = Talks.calculate_money(event)
        if not reply:
            reply = Talks.join_member(event)
        if not reply:
            reply = Flex.call_housekeeper(event)
        if not reply:
            if Talks.record_data(event) is not None:
                reply = Talks.record_data(event)
            elif Talks.record_money(event) is not None:
                reply = Talks.record_money(event)
            elif Talks.record_product(event) is not None:
                reply = Talks.record_product(event)
        

@handler.add(PostbackEvent)
def reply_postback_event(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reply = False
        
        if not reply:
            reply = Flex.call_manual(event)
        if not reply:
            reply = Talks.flex_join_member(event)
        if not reply:
            reply = Talks.record_insert_data(event)

@handler.add(JoinEvent)
def reply_join_event(event):
    reply = False

    if not reply:
        reply = line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(
            alt_text = "歡迎訊息",
            contents = flexTemplate.default_flex_template()
        )
    )
    
@handler.add(LeaveEvent)
def leave_event(event):
    CallDatabase.delete_data(event.source.group_id)

if __name__ == "__main__":
    app.run()
