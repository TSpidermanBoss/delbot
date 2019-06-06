
from pyrogram import Client, Filters,Emoji
app = Client('666639160:AAEtopjBMU5r_i_UROx8PTWSSOtIrU6V7W8',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = '-1001336546427'

s = '-1001378725482'

@app.on_message(Filters.chat(int(s)) & Filters.text)
def forawrd(client, message):
   client.send_message(int(u),message.text.replace('🎾' , '🥎'))
           


@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
   client.send_sticker(int(u),message.sticker.file_id)
            

app.run()
