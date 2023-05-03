#required packages 
import telebot
import  yt_dlp
TOKEN= "6185487999:AAEP1-Oe1hbP-oLsMpGARl3N66f4xJwrOJs"
#	with open('config.json') as f:
# token = json.load(f)
    
#Intitialize YouTube downloader
ydl_opts = {}
ydl = yt_dlp.YoutubeDL(ydl_opts)


#initialise  bot
#bot = telebot.TeleBot(token)
bot = telebot.TeleBot(TOKEN)
x = bot.get_me()
print(x)
@bot.message_handler(commands=["start"])
def start_message(msg):
    bot.send_message(msg.chat.id, f"Hey! {msg.chat.first_name} 😊, this is a video downloader bot.\t\n 1. Facebook\n 2. Twitter\n3. Youtube.\n4. Instagram.\nCreator:- @wambugu_kinyua")
@bot.message_handler(commands=["video", "Video", "Download","download","Facebook","facebook","Twitter", "twitter","Instagram","instagram","YouTube","youtube"])
def download_shit(message):
    try:
        args = message.text.split()[1]
        #bot.send_message(message.chat.id, text= os.system(f"youtube-dl {args} -g") )
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #       yvd=ydl.download([args]
            try:
                bot.reply_to(message,"Congratulations 🎉🥳.\nVideo found.\nChoose the best with sound.\nBelow are the links:👇👇👇\n")
                with ydl:
                    info = ydl.extract_info( args,download=False)
    
                if 'entries' in info:
                    # Can be a playlist or a list of videos
                    video = info['entries'][0]
                else:
                    # Just a videon 
                    video = info
                
                for i in video['formats']:
                    link = '<a href=\"' + i['url'] + '\">' + 'link' + '</a>'
        
                    if i.get('format_note'):
                        bot.reply_to(message, 'Video Quality- ' + i['format_note'] + ': ' + link, parse_mode='HTML')
                    else:
                        bot.reply_to(message,"Video  download\n"+ link, parse_mode='HTML', disable_notification=True)
            except:
                bot.reply_to(message, ' sorry 🙂This can\'t be downloaded by me🥲🥲🥲')
    except:
        bot.reply_to(message, ' sorry🙂 This can\'t be downloaded by me.🥲🥲🥲')
@bot.message_handler(commands=["help"])
def help_shit(message):
    bot.reply_to(message,"Usage:\n /download 'pase the link'.\n wait for the download link.\nChoose first 720p video for best results.\nIf bot is down contact @wambugu_kinyua.\nUsage below photo 👇👇👇.")
    photo= open("ken.jpg", "rb")
    bot.send_photo(message.chat.id,photo)
    photo.close()
bot.polling()