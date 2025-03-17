import aiohttp
import json
from configparser import ConfigParser 
import asyncio

config = ConfigParser()

config.read("config.ini")
wa_config = config["wa-api"]

ACCESS_TOKEN = wa_config["token"]
PHONE_NUMBER_ID = wa_config["id_wa_test_num"]
BOT_PHONE = wa_config["test_number"]
RECIPIENT_PHONE = "+593969795728"
WHATSAPP_API_URL = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
http_headers = {
    "Authorization" : f"Bearer {ACCESS_TOKEN}",
    "Content-Type" : "application/json"
}

def create_message_structure(message, number):
     return json.dumps({
        "messaging_product" : "whatsapp",
        "to" : number,
        "type" : "text",
        "recipient_type": "individual",
        "text" : {
            "body" : message
        }
    })

async def send_message(data):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(WHATSAPP_API_URL, data=data, headers=http_headers) as response:
                if response.status == 200:
                    print("Mensaje http enviado con exito")
                    print("Status:", response.status)
                    print("Content-type:", response.headers['content-type'])
    
                    html = await response.text()
                    print("Body:", html)
                else:
                    print(response.status)        
                    print(response)        
        except aiohttp.ClientConnectorError as e:
            print('Connection Error', str(e))


myMessage = create_message_structure("Este es otro ya que me respondiste", RECIPIENT_PHONE)
asyncio.run(send_message(myMessage))


