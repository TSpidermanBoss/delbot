
from pyrogram import Client, Filters,Emoji
app = Client('666639160:AAEtopjBMU5r_i_UROx8PTWSSOtIrU6V7W8',605563,"7f2c2d12880400b88764b9b304e14e0b")

@app.on_message(Filters.command("send"))
def forawrd(client, message):
 files = open("sure.txt","r")
 x = files.readlines()
 files.close()
 for y in x:
  z = y.split()
  for f in z:
   try:
    client.forward_messages(int(f),message.chat.id,message.reply_to_message.message_id )
   except:
    continue
@app.on_message(Filters.command("add"))
def forawrd(client, message):
    file = open("sure.txt","a")
    file.write(" " + message.text.split(" ")[1])
    file.close()
   
            

app.run()
