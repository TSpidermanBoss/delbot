
from pyrogram import Client, Filters,Emoji
app = Client('878426361:AAEv5nyWvDwikohxrGxS6mCLpgeyPVjHKTQ',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = '-1001202080858'

s = '-1001378725482'

@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)
def forawrd(client, message):
   client.send_message(int(u),message.text.replace('🎾' , '🥎'))
           


@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
   client.send_sticker(int(u),message.sticker.file_id)
            

app.run()
