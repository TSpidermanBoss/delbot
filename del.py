from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client (session_name=input("Enter session name : ") ,api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = input("Enter bot token: "))                                   

@app.on_message(Filters.command("e"))
def main(client, message):
x = message.command[1]
y = message.command[2]
print(x)
print(y)
print(int(x))
for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
app.run()
