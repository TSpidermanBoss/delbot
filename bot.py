from pyrogram import Client, Filters,Emoji
app = Client("session",bot_token="663574960:AAGWg1VGruCPuckHzjbpDLRIbPWkX6YcDlc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")

@app.on_message(Filters.command("send"))
def forawrd(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  files = open("sure.txt","r")
  x = files.readlines()
  files.close()
  for y in x:
   z = y.split()
   for f in z:
    try:
     client.forward_messages(str("@"+f),message.chat.id,message.reply_to_message.message_id )
    except:
     message.reply("🔥 Sending Failed in " + f)
     continue
  message.reply("🔁 operation completed 🔁")

@app.on_message(Filters.command("add"))
def forawrd(client, message):
 o = False
 file = open("sure.txt","r")
 t = file.readlines()
 file.close()
 for h in t:
  print(h)
  print(message.text.split(" ")[1])
  if h.casefold == message.text.split(" ")[1].casefold:
   o = True
 if not o :
  x = client.get_chat_member(message.chat.id , message.from_user.id)
  if x.status == "administrator" or x.status == "creator":
   try:
     client.send_message(message.text.split(" ")[1], "Powered by king")
     y = client.get_chat(str(message.text.split(' ')[1])).title
     file = open("sure.txt","a")
     file.write(" " + message.text.split(" ")[1])
     file.close()
     message.reply("📶 The chat - "+str(y)+" ✅" + " added. 😋😝😜😍")
   except:
     message.reply("♻️ Bot is not a admin in this channel 😡🤬🤬")
 if o:
  message.reply("already added 😏😏")

@app.on_message(Filters.command('remove'))
def forward(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  try:
   file = open("sure.txt" , "r")
   u = file.readlines()
   file.close()
   for v in u:
     lines = v.split() 
     del lines[lines.index(message.text.split(' ')[1])]
     y = " ".join(str(x) for x in lines)
     files = open("sure.txt" , "w") 
     files.write(y)
     files.close()
     message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been removed to my database. ✅✅")
  except:
     message.reply("☢️ ID not found 🧐🙄😒")


@app.on_message(Filters.command('list'))
def forward(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  file = open("sure.txt" , "r")
  u = file.readlines()
  file.close()
  for v in u :
      message.reply("🏘️ List of Chat_ids in my database are ```" + str(v) + "```.")
 
@app.on_message(Filters.command('clear1') & Filters.user(491634139))
def forward(client, message):
    with open("sure.txt" , "w") as file:
     file.write("cfamovies")
     file.close()
     message.reply("☢️ Done, Success ✅✅")

  
@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ The bot is Promotion bot created by a wonderful person 😘😊😋. Work only in groups😂😭. ✅✅")
      

app.run()
