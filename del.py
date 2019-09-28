from pyrogram import Client, Filters,Emoji
app = Client("session",728044,"a41ddadc9696482aff94a4b37221574a")

@app.on_message(Filters.command("e"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  x = int(message.text.split(' ')[1])
  y = int(message.text.split(' ')[2])
  for m in range(x,y):
   try:
    client.delete_messages(message.chat.id,m)
   except:
    continue
@app.on_message(Filters.command("a"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  x = int(message.text.split(' ')[1])
  y = int(message.text.split(' ')[2])
  for m in range(x,y):
   try:
    client.delete_messages(message.chat.id,m)
   except:
    continue
@app.on_message(Filters.command("b"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  x = int(message.text.split(' ')[1])
  y = int(message.text.split(' ')[2])
  for m in range(x,y):
   try:
    client.delete_messages(message.chat.id,m)
   except:
    continue
@app.on_message(Filters.command("c"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  x = int(message.text.split(' ')[1])
  y = int(message.text.split(' ')[2])
  for m in range(x,y):
   try:
    client.delete_messages(message.chat.id,m)
   except:
    continue
@app.on_message(Filters.command("d"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  x = int(message.text.split(' ')[1])
  y = int(message.text.split(' ')[2])
  for m in range(x,y):
   try:
    client.delete_messages(message.chat.id,m)
   except:
    continue

app.run()
