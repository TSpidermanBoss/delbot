from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client("my_account",800295,"3d6ffe66b0d34f2921b964da418d9931")
@app.on_message(Filters.command("e"))
def main(client, message):
 x = message.command[1]
 y = message.command[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("b"))
def main(client, message):
 x = message.command[1]
 y = message.command[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("a"))
def main(client, message):
 x = message.command[1]
 y = message.command[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("c"))
def main(client, message):
 x = message.command[1]
 y = message.command[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("d"))
def main(client, message):
 x = message.command[1]
 y = message.command[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue

app.run()
