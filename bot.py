
from pyrogram import Client, Filters,Emoji
app = Client("870127745:AAGKhzPQ__N3pn56_44Sn86yGOLKwvbu-0k",715451,"d2cba6f7bf5d1a45682da5bb9071a307")

@app.on_message(Filters.command("send"))
def forawrd(client, message):
 files = open("sure.txt","r")
 x = files.readlines()
 files.close()
 for y in x:
  z = y.split()
  for f in z:
   try:
    client.forward_messages(str(f),message.chat.id,message.reply_to_message.message_id )
   except:
    message.reply("🔥 Sending Failed in " + f)
    continue
@app.on_message(Filters.command("add"))
def forawrd(client, message):
  try:
    x = client.get_chat(str(message.text.split(' ')[1])).title
    file = open("sure.txt","a")
    file.write(" " + message.text.split(" ")[1])
    file.close()
    message.reply("📶 The chat - "+str(x)+" ✅" + " added.")
  except:
   message.reply("♻️ Bot is not a admin in this channel 😣🕵️")

            

app.run()
