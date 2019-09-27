from pyrogram import Client, Filters,Emoji
app = Client("session",bot_token="912058665:AAEoMfZrqGnfd6OJr32sC5e4CEKEpxEVz3w",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")

@app.on_message(Filters.command("send"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  x =  message.reply_to_message.message_id
  y = message.message_id
  for m in range(x,y):
   try:
    client.delete_messages(message.chat.id,m)
   except:
    continue
app.run()
