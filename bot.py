from pyrogram import Client, Filters



app = Client('my_account')



@app.on_message(Filters.chat(-1001278232224 & Filters.text)
def forward(client, message):
          client.forward_messages(-1001344956857, -1001129914210, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
          client.forward_messages(-1001356076506, -1001129914210, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    

app.run()

