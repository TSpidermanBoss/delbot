from telegram import ParseMode
import time
from telegram.ext import MessageHandler, Filters, Updater,run_async,CommandHandler
bot = '1044884743:AAEVHIR-LJP7mBRnYqWhByGeO89QlpLGjA8'
des = -1001165875030
s = -1001483523101
updater = Updater(token=bot,use_context=True)
@run_async
def send(update,context):
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🥳','link','❓','garr','audio','whatsapp','book','bhai','🐴','only','tennis','teen','line','WICKET LU','?','telegram',"kama","lakh",' id','स']
 for word in words:
  if word.casefold() in update.effective_message.text.casefold():
    return
 file = open("des.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
   mes = context.bot.send_message(int(line),"*" + update.effective_message.text + "*",parse_mode=ParseMode.MARKDOWN)
   fie = open("ids.txt","a")
   fie.write(" " + str(update.effective_message.message_id) + " " + str(mes.message_id))
   fie.close()
@run_async
def edit(update,context):
 file = open("des.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
   files = open("ids.txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(update.effective_message.message_id)
    if id in x:
      context.bot.edit_message_text("*" + update.effective_message.text + "*",line,int(x[x.index(id)+1]),parse_mode=ParseMode.MARKDOWN)
@run_async
def clear(update,context):
  with open("ids.txt","w") as fie:
   fie.write("001 002")
   fie.close()
   update.message.reply_text("☢️ Done, Editing data cleared ✅✅")

@run_async
def des(update,context):
 file = open("des.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  update.message.reply_text("Current destination " + line)
 if len(update.message.text.split(' ')) > 1:
  if len(update.message.text.split(' ')[1]) == 14:
     files = open("des.txt" , "w") 
     files.write(update.message.text.split(' ')[1])
     files.close()
     update.message.reply_text("Destination Changed")

dispatcher = updater.dispatcher
send = MessageHandler(Filters.chat(s) & Filters.text & ~ Filters.update.edited_channel_post ,send)
edit = MessageHandler(Filters.chat(s) & Filters.update.edited_channel_post,edit)
des = CommandHandler("des",des)
clear = CommandHandler("clear",clear)
dispatcher.add_handler(send)
dispatcher.add_handler(edit)
dispatcher.add_handler(clear)
dispatcher.add_handler(des)

updater.start_polling()
