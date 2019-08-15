from pyrogram import Client, Filters,Emoji
app = Client("session",bot_token="903164012:AAH6f9qw6TGaF7DJkiaCeqjp7oaM92p93fc",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")

#("session",bot_token="622131522:AAFUneglCPEgaZKa8lcaYCnIKitXjct8YGU",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")

@app.on_message(Filters.text)
def main(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if not b == 'administrator' or b == "creator":  
  if "@" in message.text:
   client.delete_messages(message.chat.id, message.message_id)

@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is antiusername created by a wonderful [person](https://t.me/Google_console) ✍️.

Add me to your group i will delete username from non admins automatically.""")


app.run()
