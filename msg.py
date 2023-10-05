import os
import sys
import keyboard as k
import time
import webbrowser


def msg_send(msg: str, phone_number: str):
   
    msg=msg
    url='https://api.whatsapp.com/send?phone='+phone_number+'&text='+msg
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open(url)

    time.sleep(5)
    k.press_and_release('enter')
    
