
import schedule
import time
import requests

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,  # put your phone number here!!
        'message': 'Hey, Good morning',
        'key': 'textbelt'
    })
    
    print(resp.json())
    
# schedule.every().day.at('07:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)