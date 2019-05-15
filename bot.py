from pyrogram import Client, Filters



app = Client('890398475:AAFKe-e5H2owXvzoB-AlIpy3ELE-0f7OoNs')



@app.on_message(Filters.chat(-1001353340635) & Filters.text)
def forward(client, message):
          client.forward_messages(-1001344956857, -1001353340635, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
          client.forward_messages(-1001356076506, -1001353340635, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    

app.run()

