from pyrogram import Client, Filters,Emoji
import re

app = Client("session",bot_token="622131522:AAFUneglCPEgaZKa8lcaYCnIKitXjct8YGU",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")

@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is antiusername created by a wonderful [person](https://t.me/Google_console) ✍️.

Add me to your group i will delete username from non admins automatically.""")


@app.on_message(Filters.text)
def main(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if not b == 'administrator' or b == "creator":  
   txt = message.text
   x = re.search("^@", txt)
   print(x)
   #client.delete_messages(message.chat.id, message.message_id)



app.run()
