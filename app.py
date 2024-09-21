import os
import sys


from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,LocationSendMessage


from fsm import TocMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message, send_text_message_AI




load_dotenv()




machine = TocMachine(
    states=[
        'choose',
        'menu',
        'location',
        'reserve_people',
        'reserve_time',
        'reserve_result',
        'employee'
    ],
    transitions=[
        
         {'trigger': 'advance', 'source': 'user', 'dest': 'choose', 'conditions': 'is_going_to_choose'},
        {'trigger': 'advance', 'source': 'choose', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
        {'trigger': 'advance', 'source': 'choose', 'dest': 'location', 'conditions': 'is_going_to_location'},
         {'trigger': 'advance', 'source': 'choose', 'dest': 'employee', 'conditions': 'is_going_to_employee'},
        
        
        {'trigger': 'advance', 'source': 'choose', 'dest': 'reserve_people', 'conditions': 'is_going_to_reserve_people'},
        
        
        {'trigger': 'advance', 'source': 'reserve_people', 'dest': 'reserve_time', 'conditions':'is_going_to_reserve_time'},
        
        {'trigger': 'advance', 'source': 'reserve_time', 'dest': 'reserve_result', 'conditions': 'is_going_to_reserve_result'},
        
        
        
        
          {'trigger': 'advance', 'source': 'menu', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source': 'location', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source':  'reserve_result', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source':  'employee', 'dest': 'choose', 'conditions': 'go_back'},
    
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


app = Flask(__name__, static_url_path='')




# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)


line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


mode = 0


@app.route('/callback', methods=['POST'])
def webhook_handler():
    global mode
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f'Request body: {body}')


    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)


    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f'\nFSM STATE: {machine.state}')
        print(f'REQUEST BODY: \n{body}')
        
        response = machine.advance(event)
        if response == False:
      
            if machine.state == 'user':
             url = 'https://img.onl/gnwV1F'
             send_image_message(event.reply_token, url)


            elif machine.state == 'reserve_people':
                send_text_message(event.reply_token, '請輸入人數(1~10)')
            elif machine.state == 'reserve_time':
                send_text_message(event.reply_token, '請輸入時間(格式xx:xx)')
            elif event.message.text.lower() == 'fsm':
                send_image_message(event.reply_token, 'https://f74062044.herokuapp.com/show-fsm')
           
            
    return 'OK'




if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port, debug=True)
