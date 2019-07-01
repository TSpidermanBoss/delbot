from pyrogram import Client, Filters,Emoji
app = Client("870127745:AAGKhzPQ__N3pn56_44Sn86yGOLKwvbu-0k",715451,"d2cba6f7bf5d1a45682da5bb9071a307")

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
 x = client.get_chat_member(message.chat.id , message.from_user.id)
 if x.status == "administrator" or x.status == "creator":
  try:
    client.send_message(message.text.split(" ")[1], "Powered by king")
    x = client.get_chat(str(message.text.split(' ')[1])).title
    file = open("sure.txt","a")
    file.write(" " + message.text.split(" ")[1])
    file.close()
    message.reply("📶 The chat - "+str(x)+" ✅" + " added.")
  except:
    message.reply("♻️ Bot is not a admin in this channel 😣🕵️")

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
     message.reply("☢️ ID not found 🚫")


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
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
      

app.run()
