from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client("s",965018,"6cd1a0cfc1a3e76076a8331c4319e97c")
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
