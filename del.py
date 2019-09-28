from pyrogram import Client, Filters,Emoji
app = Client("session",bot_token="745460463:AAGN6LBCTNI-9ZXz5eQF9ouP0M8p3rzyZAM",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")

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
