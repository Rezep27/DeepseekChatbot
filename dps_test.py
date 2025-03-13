from openai import OpenAI
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

deep_api = config['ds-api']
client = OpenAI(api_key=deep_api['api_key'], base_url=deep_api['base_url'])


def initial_messaage(message):
    init_mess = [{"role": "system", "content": "Eres un asistente virtual de la empresa Mega Propinec que habla español. Cuando una persona inicie una conversacion contigo"},]
    while (message != "exit"):

        init_mess.append({"role": "user", "content": message},)

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages= init_mess,
            stream=False
        )
        
        init_mess.append(response.choices[0].message)
        print(response.choices[0].message.content)
        message = input("Desea preguntar algo más? ")

my_message = input("Ingrese su respuesta:")

initial_messaage(my_message)


