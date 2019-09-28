from pyrogram import Client, Filters,Emoji
app = Client ("session",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")

@app.on_message(Filters.command("e"))
def forawrd(client, message):
 x = message.text.split(' ')[1]
 y = message.text.split(' ')[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
from pyrogram import Client, Filters,Emoji
app = Client ("session",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")

@app.on_message(Filters.command("a"))
def forawrd(client, message):
 x = message.text.split(' ')[1]
 y = message.text.split(' ')[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("d"))
def forawrd(client, message):
 x = message.text.split(' ')[1]
 y = message.text.split(' ')[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("c"))
def forawrd(client, message):
 x = message.text.split(' ')[1]
 y = message.text.split(' ')[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue
@app.on_message(Filters.command("f"))
def forawrd(client, message):
 x = message.text.split(' ')[1]
 y = message.text.split(' ')[2]
 for m in range(int(x),int(y)):
  try:
   client.delete_messages(message.chat.id,m)
  except:
   continue

app.run()
