from pyrogram import Client, Filters,Emoji
app = Client("session",bot_token="912058665:AAEoMfZrqGnfd6OJr32sC5e4CEKEpxEVz3w",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")
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
     mes = client.forward_messages(str(f),message.chat.id,message.reply_to_message.message_id )
     fie = open(str(f)+".txt","w")
     fie.write(str(mes.message_id))
     fie.close()
    except:
     message.reply("🔥 Sending Failed in " + f)
     continue
  message.reply("🔁 operation completed 🔁")

@app.on_message(Filters.command("add"))
def forawrd(client, message):
 o = False
 fil = open("sure.txt","r")
 t = fil.readlines()
 fil.close()
 for h in t:
   q = h.split()
   for d in q:
    if d.casefold() == message.text.split(" ")[1].casefold():
      o = True
 if not o :
  x = client.get_chat_member(message.chat.id , message.from_user.id)
  if x.status == "administrator" or x.status == "creator":
   try:
     client.send_message(message.text.split(" ")[1], "Powered by Hulk")
     y = client.get_chat(str(message.text.split(' ')[1])).title
     file = open("sure.txt","a")
     file.write(" " + message.text.split(" ")[1])
     file.close()
     message.reply("📶 The chat - "+str(y)+" ✅" + " added .")
   except:
     message.reply("♻️ I is not a admin in " + str(y))
 if o:
     message.reply("🔰 Chat already in List 💼")

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
     message.reply("☢️ ID not found!")

@app.on_message(Filters.command("delete"))
def main(client, message):
  files = open("sure.txt","r")
  x = files.readlines()
  files.close()
  for y in x:
   z = y.split()
   for f in z:
    files = open(str(f)+".txt" , "r")
    d = files.readlines()
    files.close()
    for c in d:
     x = c.split()
     for id in x:
      try:
       client.delete_messages(str(f).replace ("@",""),int(id))
       with open(str(f)+".txt" , "w") as file:
        file.write("")
        file.close()
      except:
       message.reply("Deletion Failed in >>>> " + str(f))
       continue
  message.reply("🔁 operation completed 🔁")

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
     file.write("")
     file.close()
     message.reply("☢️ Done, Success ✅✅") 
@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("""♻️ The bot is Promotion bot created by a wonderful person . 
Work only in groups. ✅✅

How to use:

👉 add a channel
1. ```/add @username```

👉 remove a channel
2. ```/remove @username```

👉 list of channels
3. ```/list```

👉 send a list
4. reply a list of Channel to ```/send``` for send it to all Channels.

👉 Delete Lists
5. ```/delete``` all lists 

only Admin exist that's command in supergroups. ✍️

Powered by Hulk Promotion 👊.     """)
app.run()
