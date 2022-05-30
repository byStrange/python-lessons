import asyncio
from telethon import TelegramClient, events
import os
import asyncio
from pprint import pprint
from users import *
# import api_id and api_hash from .env file
from dotenv import load_dotenv
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_name = os.getenv('SESSION_NAME')
# login As telegram user

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        print('\033[92m' + 'success' + '\033[0m')
        messages = await client.get_messages(abror, limit=10)
        messages.reverse()
        for message in messages:
            # print(message.message)
            if message.text:
                print(message.text)
        await client.run_until_disconnected()

    

asyncio.run(main())