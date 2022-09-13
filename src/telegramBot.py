from dotenv import load_dotenv
import os

load_dotenv()#está parte do cógio serve para esconder a key do boto, ou seja quando eu enviar este arquivo para alguém, ele não terá acesso ao bot e somente ao código
TOKEN = os.getenv("api_key") 

class telegramBot:
    def __init__(self):
        TOKEN = os.getenv("api_key")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"

    def get_mensage(self):
        link_request = f"{self.url}getUpdates?timeout=1000"

