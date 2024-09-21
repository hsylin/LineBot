from transitions.extensions import GraphMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from bs4 import BeautifulSoup
import requests
from linebot.models import (ImageCarouselColumn, URITemplateAction, MessageTemplateAction,MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,LocationSendMessage)
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
import pandas as pd
import random




import os
import sys


from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv








channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)


# global variable
hour = 0
minute = 0
part = ''
people = 0
line_bot_api = LineBotApi(channel_access_token)


class TocMachine(GraphMachine):


    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)


    # user start
         
    def is_going_to_choose(self, event):
        text = event.message.text
        if text == '蟹堡王':
            return True
        return False
    
    def on_enter_choose(self, event):
        title = '歡迎光臨蟹堡王'
        text = '你可以 訂位/查看菜單/查看餐廳位置/餐廳人員介紹'
        btn = [
            MessageTemplateAction(
                 label = '訂位',
                text ='訂位'
            ),
            MessageTemplateAction(
                label = '查看菜單',
                text = '查看菜單'
            ),
            
             MessageTemplateAction(
                label = '查看餐廳位置',
                text = '查看餐廳位置'
            ),
             MessageTemplateAction(
                label = '餐廳人員介紹',
                text = '餐廳人員介紹'
            ),
        ]
        url = 'https://img.onl/pVmoZS'
        send_button_message(event.reply_token, title, text, btn, url)
        
          
        
    def is_going_to_menu(self, event):
        text = event.message.text
        if text == '查看菜單':
            return True
        return False


   
    def on_enter_menu(self, event):
        message = [ 
            ImageSendMessage(  
            original_content_url='https://img.onl/hVRwPJ',
            preview_image_url='https://img.onl/hVRwPJ'
            
            ),
                TextSendMessage(  
                    text = '輸入任意值以返回'
                ),
            ]
        line_bot_api.reply_message(event.reply_token,message)   


       
        
    def is_going_to_location(self, event):
        text = event.message.text
        if text == '查看餐廳位置':
            return True
        return False


    def on_enter_location(self, event):
        
        message= [
        LocationSendMessage(
        title='my location',
        address='蟹堡王',
        latitude=32.6948660,
        longitude=-162.0703120),
        TextSendMessage(  
                    text = '輸入任意值以返回'
                ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
       


        
       
      
      
    def is_going_to_reserve_people(self, event):
        text = event.message.text
        if text == '訂位':
            return True
        return False        
      
    def on_enter_reserve_people(self, event):
        send_text_message(event.reply_token, '請輸入人數(1~10)')


    def is_going_to_reserve_time(self, event):
        global people
        text = event.message.text
        if text.lower().isnumeric():
            people = int(text)
        if people >=1 and people <=10:
            return True
        return False
        
    def on_enter_reserve_time(self, event):
        send_text_message(event.reply_token, '請輸入時間(格式xx:xx)')
        
    def is_going_to_reserve_result(self, event):
        global hour
        global minute
        text = event.message.text
        time = text.split(':')
        if time[0].lower().isnumeric():
            hour = int(time[0])
        else:
            return False
        if time[1].lower().isnumeric():
            minute = int(time[1])
        else:
            return False   
            
        if hour>=0 and hour <24 and  minute>=0 and minute <60:
            return True
        return False
        


    def on_enter_reserve_result(self, event):
        global x
        x=random.randint(0,1)


        if x == 0:
            message = [ 
            ImageSendMessage(  
            original_content_url='https://img.onl/q4QIHO',
            preview_image_url='https://img.onl/q4QIHO'
                ),
                TextSendMessage(  
                    text = '輸入任意值以返回'
                ),
            ]
        else:
            message = [ 
            ImageSendMessage(  
            original_content_url='https://img.onl/rROg7',
            preview_image_url='https://img.onl/rROg7'
            
            ),
                TextSendMessage(  
                    text = '輸入任意值以返回'
                ),
            ]
        line_bot_api.reply_message(event.reply_token,message)   


        
        
        
    def is_going_to_employee(self, event):
        text = event.message.text
        if text == '餐廳人員介紹':
            return True
        return False
   
    def on_enter_employee(self, event):
        send_text_message(event.reply_token, '輸入任意值以返回')    
        
     
    def go_back(self, event):
        return True
