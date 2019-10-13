from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
import math
import pynewtonmath

app = Client("mnnn",bot_token="836655322:AAGlcw1XO_I7ZJqs9iVzQE8RgMbfCcHWxk0",api_id=768402,api_hash="f6420bf67303614279049d48d3e670f6")

@app.on_message(Filters.private & Filters.command("derive"))
def main(client, message):
 x = message.text.split(' ')[1]
 message.reply(pynewtonmath.derive(x))

app.run()
