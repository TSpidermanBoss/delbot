from pyrogram import Client, Filters
app = Client('666639160:AAEtopjBMU5r_i_UROx8PTWSSOtIrU6V7W8')

u = '-1001336546427'
s = '-1001369162545'
@app.on_message(Filters.chat(int(s)) & Filters.text)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if '🖲' in message.text :
            client.send_message(int(u),message.text.replace('🖲' , '💘'))
        else:
          if '📟' in message.text :
            client.send_message(int(u),message.text.replace('📟' , '🏝'))
          else:
            if message.text == '6' :
               client.send_sticker(int(u),'CAADBQADHAAD271NHXPgZgboyWwDAg')
               client.send_message(int(u),message.text.replace('🎾' , '🥎'))
            else:
              if message.text == '4' :
               client.send_sticker(int(u),'CAADBQADGwAD271NHWpGz0fJOgEPAg')
               client.send_message(int(u),message.text.replace('🎾' , '🥎'))
              else:
                if message.text == 'WD' :
                  client.send_sticker(int(u),'CAADBQADHgAD271NHUFx5PgLyzp9Ag')
                  client.send_message(int(u),message.text.replace('WD' , 'WIDE BALL 🙅‍♂️'))
                else:
                    if message.text == 'WKT' :
                     client.send_sticker(int(u),'CAADBQADHQAD271NHQimFHP2bU9cAg')
                     client.send_message(int(u),message.text.replace('WKT' , '🚾 Wicket Wicket Wicket 🚾 ')) 
                    else:
                       if message.text == 'NO BALL':
                         client.send_message(int(u),message.text.replace('NO BALL' , '🤦‍♂️ NO BALL '))
                       else:
                          if 'DRINKS BREAK' in message.text:
                            client.send_sticker(int(u),'"CAADBQADIwAD271NHfRwgjZiWt3-Ag')
                            client.send_message(int(u), '🍻 DRINKS BREAK 🍻') 
                          else:
                            client.send_message(int(u),message.text.replace('🎾' , '🥎'))


@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if message.sticker.file_id == 'CAADBQADkgIAAlTquhpPMfzjWNqQagI' :
            client.send_sticker(int(u),'CAADBQADHwAD271NHQtXw-moeKYWAg')
            client.send_message(int(u),'🍾INNINIGS BREAK🍾' )

@app.on_message(Filters.command('status'))
def main(client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")        
@app.on_message(Filters. private)
def ran( client, message) :
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('offline'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
@app.on_message(Filters.command('online'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
app.run()
