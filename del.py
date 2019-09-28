from pyrogram import Client, Filters,Emoji
app = Client ("session",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")

@app.on_message(Filters.command("e"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.command("a"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue
@app.on_message(Filters.command("b"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue
@app.on_message(Filters.command("c"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue
@app.on_message(Filters.command("d"))
def main(client, message):
 for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

app.run()
