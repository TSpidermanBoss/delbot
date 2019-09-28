from pyrogram import Client, Filters,Emoji
app = Client("my_account",800295,"3d6ffe66b0d34f2921b964da418d9931")

@app.on_message(Filters.command("e"))
def main(client, message):
 for message.message_id in range(int(message.command[1]), int(message.command[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.command("a"))
def main(client, message):
 for message.message_id in range(int(message.command[1]), int(message.command[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.command("b"))
def main(client, message):
 for message.message_id in range(int(message.command[1]), int(message.command[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.command("c"))
def main(client, message):
 for message.message_id in range(int(message.command[1]), int(message.command[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue

@app.on_message(Filters.command("d"))
def main(client, message):
 for message.message_id in range(int(message.command[1]), int(message.command[2])):
  try:
   client.delete_messages(message.chat.id,message.message_id)
  except:
   continue


app.run()
