 import telegram.ext 

def start(update, context):
    update.message.reply_text("Namaste")

def help(update, context):
        update.message.reply_text(
            """
            /start -> Welcome to the channel
            /help -> This particuler message
            /content -> About various Playlists of Prof. Barapate's Tutorials
            /ElectornicCircuits -> The first video from the Electronic Circuit playlist
            /ElectricalCircuits -> The first video from Electrical playlist
            /ControlSystems -> The first video from Control Systems Playlist
            /contact -> contact information
            """
        )

def content(update, context):
    update.message.reply_text(" We have various playlists available")

def ElectornicCircuits(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/OQCSycXJN10")

def ElectricalCircuits(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/G0VOm1y0yOw")

def ControlSystems(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/EtMRJkCqJN0")
    
def contact(update, context):
    update.message.reply_text(" You can contact on the registered mail id provided on the website")
    
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
dispatcher.add_handler(telegram.ext.CommandHandler('ElectornicCircuits', ElectornicCircuits))
dispatcher.add_handler(telegram.ext.CommandHandler('ElictricalCircuits', ElectricalCircuits))
dispatcher.add_handler(telegram.ext.CommandHandler('ControlSystems', ControlSystems))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()          
updater.idle()                    

