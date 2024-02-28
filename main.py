
# parser libraries
import json
import requests
#<---------------->
# database library
from pymongo import MongoClient
#<---------------->
# bot library 
from telebot import TeleBot,types,util
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton,InlineQueryResultArticle,InputTextMessageContent
from telebot.util import user_link

cookies = {
    '_ga': 'GA1.1.516210836.1707903644',
    'FontGenerator': 's%3ADFVgC5LIFqXpCbOMczNIGhcNvYja6dq0.JGepYo6n0Ux8M9Ad7MWhGmxH2vop363Fed884UBFzu4',
    '_ga_N1VSP6S9LM': 'GS1.1.1707918739.2.1.1707919163.0.0.0',
}

headers = {
    'authority': 'www.fontgen.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8,ru;q=0.7,am;q=0.6',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.516210836.1707903644; FontGenerator=s%3ADFVgC5LIFqXpCbOMczNIGhcNvYja6dq0.JGepYo6n0Ux8M9Ad7MWhGmxH2vop363Fed884UBFzu4; _ga_N1VSP6S9LM=GS1.1.1707918739.2.1.1707919163.0.0.0',
    'origin': 'https://www.fontgen.net',
    'referer': 'https://www.fontgen.net/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
#bot = TeleBot("7071225685:AAG-IrTmXsg5kbVw3pGHFyhJpLcO8hHDw8Q",parse_mode="HTML")
parser = "HTML"
botToken = "6729835437:AAHHhiVCEz9Fa_ANtUCrldxQQ8tXMA5WL-c"
bot = TeleBot(botToken,parse_mode=parser)

button = InlineKeyboardMarkup()
button.row_width = 2

group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
toFonts = InlineKeyboardButton(text="🔙",callback_data="back")
button.add(group,channel,toFonts)


connection = "mongodb+srv://sigmaCoder:19932021Abc@sigmacoder.9r7hnap.mongodb.net/?retryWrites=true&w=majority&appName=sigmaCoder"
client = MongoClient(connection)

# crate a database ["styleText"]
db = client.styleText
# create a collection["botUsers"] 
users = db.botUsers
# create a collection["admins"]
admins = db.admins
admin_id = [640419142,2069970688]
total_user = users.count_documents({})

# handle /start command
@bot.message_handler(commands=["start"])
def greetUser(msg):
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}" 
    data = {"userid":userID,"first_name":firstName,"user_name":userName}
    if users.find_one({"userid":userID}) == None:
        to_db = users.insert_one(data)

    text = f"Hey dear {user_link(msg.from_user)} send text to style and select your best font on the button"
    bot.reply_to(msg,text,reply_markup=button)

# direction on how to use the bot
@bot.message_handler(commands=["help"])
def userManual(msg):
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}" 
    data = {"userid":userID,"first_name":firstName,"user_name":userName}
    if users.find_one({"userid":userID}) == None:
        to_db = users.insert_one(data)
    bugReport = InlineKeyboardMarkup()
    bug = InlineKeyboardButton(text="Report a bug",url="t.me/neuralg")
    bugReport.add(bug)
    #text = """You can use this bot in two ways\n1)Through buttons and\n2)Through inline ...using <code>@styleTextRobot your text here</code>\nto use through button mode first you have to write pound symbol(hash symbol)<b>#</b> before your text,it help me to protect the conflict occured during the inline query and inline button\nExample on how to use through button
      # deathLover """
    text = """ # 𝖄𝖔𝖚 𝖈𝖆𝖓 𝖚𝖘𝖊 𝖙𝖍𝖎𝖘 𝖇𝖔𝖙 𝖎𝖓 𝖙𝖜𝖔 𝖜𝖆𝖞𝖘
1)𝕿𝖍𝖗𝖔𝖚𝖌𝖍 𝖇𝖚𝖙𝖙𝖔𝖓𝖘 𝖆𝖓𝖉
2)𝕿𝖍𝖗𝖔𝖚𝖌𝖍 𝖎𝖓𝖑𝖎𝖓𝖊,𝖜𝖗𝖎𝖙𝖊 𝖇𝖔𝖙 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 𝖙𝖍𝖊𝖓 𝖙𝖍𝖊 𝖙𝖊𝖝𝖙 𝖞𝖔𝖚 𝖜𝖆𝖓𝖙,𝖑𝖎𝖐𝖊 𝖙𝖍𝖎𝖘: @𝖘𝖙𝖞𝖑𝖊𝕿𝖊𝖝𝖙𝕽𝖔𝖇𝖔𝖙 𝖞𝖔𝖚𝖗 𝖙𝖊𝖝𝖙 𝖍𝖊𝖗𝖊
⚠️𝕯𝖔𝖓'𝖙 𝖚𝖘𝖊 𝖎𝖓𝖑𝖎𝖓𝖊 𝖒𝖔𝖉𝖊 𝖍𝖊𝖗𝖊 𝖎𝖓 𝖇𝖔𝖙!"""
    bot.reply_to(msg,text,reply_markup=bugReport)

# This is the /broadcast command 
@bot.message_handler(commands=["broadcast"])
def broadcast(msg):
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}" 
    data = {"userid":userID,"first_name":firstName,"user_name":userName}

    if userID not in admin_id:
        bot.reply_to(msg,"This command is for admins only!")
    else:
        bot.reply_to(msg,"Send me a broadcasting message:")
        bot.register_next_step_handler(msg,send)

def send(msg):
    for ids in users.find({}):
        id = ids["userid"]
        #uid = 5249435830 --admin id---
        bot.send_message(id,f"{msg.text}",reply_markup=buttons)
        #bot.reply_to(msg,f"""Your msg: {msg.text}\n broadcasted successfully!""")

@bot.message_handler(commands=["notify"])
def notify(msg):
    #send msg to specific user
    userID = msg.from_user.id
    text = msg.text
    if userID in admin_id:
        bot.reply_to(msg,"Send me with this format: <b>/id</b>\n <b>your text here in new line</b>")
        bot.register_next_step_handler(msg,sendto_user)
    else:
        bot.send_message(msg.chat.id,"You are not in admins list:)")

def sendto_user(message):
    id = message.text.split("/")[1]
    msg = message.text.splitlines()
    print(msg)
    bot.send_message(id,msg[1])
    bot.reply_to(message,f"Your msg {msg[1]} delivered successfully:)")

@bot.message_handler(commands=["adminreg"])
def adminRegister(msg):
    userID = msg.from_user.id
    #check user if he is allowed or not
    if userID in admin_id:
        #t = """Send me your information separated with(<b>|</b>) example <b>yourID|</b><b>name|</b><b>username:\n example: 5342<b>|</b>The Ep<b>|</b>@The_ep"""
        text = "Please send admin id and permission bool:True or False\n example: <b>453</b>|<b>True</b>\t acceptable with format only."
        bot.send_message(msg.chat.id,text)
        bot.register_next_step_handler(msg,getInfo)
    else:
        bot.send_message(msg.chat.id,"You are not in allowed to use this command!")    
        
def getInfo(msg):
    info = msg.text.split("|")
    adm_id = info[0]
    is_admin = info[1]
    #adm_fName = info[1]
    #adm_userName = f"@{info[2]}"
    #admin_data = {"adminID":int(adm_id),"adminName":adm_fName,"adminUsername":adm_userName}
    admin_data = {"adminID":[adm_id],"admin":is_admin}
    if admins.find_one({"adminID":adm_id}) == None:
        to_db = admins.insert_one(admin_data)
        #print(admin_data["adminUsername"])
    else:
        pass
    bot.reply_to(msg,f"Your msg: <b>{admin_data}</b> successfully saved on db!")

@bot.message_handler(commands=["count"])
def count_users(msg):
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}" 
    data = {"userid":userID,"first_name":firstName,"user_name":userName}
    if users.find_one({"userid":userID}) == None:
        to_db = users.insert_one(data)
    bot.send_message(msg.chat.id,f"We have:<b>{total_user} users</b> in our bot!")

# this decorator handles incoming text
@bot.message_handler(func=lambda m:True)
def chooseFont(msg):
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}" 
    data = {"userid":userID,"first_name":firstName,"user_name":userName}
    if users.find_one({"userid":userID}) == None:
        to_db = users.insert_one(data)

    fontkeyValue = {"greekCharMap":"font1","upperAnglesCharMap":"font2","BoldFloara":"font3","NinjaText":"font4","doubleStruckCharMap":"font5",
                    "neonCharMap":"font6","oldEnglishCharBoldMap":"font7","oldItalicText":"font8","FreeFireText":"font9","Ladyleo":"font10",
                    "Blocky":"font11","butterflyIt":"font12","AstroFont":"font13","BoldJavaneseText":"font14","RitualText":"font15",
                    "cursiveLettersBold":"font16","ak47GunText":"font17","FooText":"font18","GunFire":"font19","taiVietCharMap":"font20",
                    "eyeOfHorusText":"font21","Dessert":"font22","checksText":"font23","RainbowText":"font24","slowSnail":"font25","PingPong":"font26",
                    "MagicalText":"font27","GunText":"font28","JavaneseRerengganText":"font29","featlyFont":"font30",
                    "fadedBlock":"font31","bracketCharMap":"font32","gunFireText":"font33"}
    option = InlineKeyboardMarkup()
    op1 = InlineKeyboardButton("∂єαтнℓσνєя",callback_data=f"{fontkeyValue['greekCharMap']}")
    op2 = InlineKeyboardButton("DΣΛƬΉᄂӨVΣЯ",callback_data=f"{fontkeyValue['upperAnglesCharMap']}")
    op3 = InlineKeyboardButton("❀ꗥ～ꗥ❀ 𝐝𝐞𝐚𝐭𝐡𝐋 𝐨𝐯𝐞𝐫 ❀ꗥ～ꗥ❀",callback_data=f"{fontkeyValue['BoldFloara']}")
    op4 = InlineKeyboardButton("đēⱥⱦħŁꝋꝟēɍ𓆪",callback_data=f"{fontkeyValue['NinjaText']}")
    op5 = InlineKeyboardButton("𝕕𝕖𝕒𝕥𝕙𝕃𝕠𝕧𝕖𝕣",callback_data=f"{fontkeyValue['doubleStruckCharMap']}")
    op6 = InlineKeyboardButton("ᗪEᗩTᕼᒪOᐯEᖇ",callback_data=f"{fontkeyValue['neonCharMap']}")
    op7 = InlineKeyboardButton("𝖉𝖊𝖆𝖙𝖍𝕷𝖔𝖛𝖊𝖗",callback_data=f"{fontkeyValue['oldEnglishCharBoldMap']}")
    op8 = InlineKeyboardButton("𐌃𐌄𐌀𐌕𐋅𐌋Ꝋᕓ𐌄𐌓",callback_data=f"{fontkeyValue['oldItalicText']}")
    op9 = InlineKeyboardButton("★彡( ĐɆ₳₮ⱧⱠØVɆⱤ )彡★",callback_data=f"{fontkeyValue['FreeFireText']}")
    op10 = InlineKeyboardButton("❀💋❀ ƊƸ𐤠ƬǶȴΘƲƸⱤ ❀💋❀",callback_data=f"{fontkeyValue['Ladyleo']}")
    op11 = InlineKeyboardButton("▁▂▄▅▆▇█ DΣΛƬΉᄂӨVΣЯ █▇▆▅▄▂▁",callback_data=f"{fontkeyValue['Blocky']}")
    op12 = InlineKeyboardButton("♥Ƹ̵̡Ӝ ̵̨̄Ʒ♥ 𝖉𝖊𝖆𝖙𝖍𝕷𝖔𝖛𝖊𝖗 ♥Ƹ̵̡Ӝ̵̨̄Ʒ♥",callback_data=f"{fontkeyValue['butterflyIt']}")
    op13 = InlineKeyboardButton("✫☼☾☁ 𝝙𝝚𝝖𝝩𝝜Ⳑ𝝤ꓴ𝝚Ɍ ☁☾☼✫",callback_data=f"{fontkeyValue['AstroFont']}")
    op14 = InlineKeyboardButton("꧁༺ 𝓭𝓮𝓪𝓽𝓱𝓛𝓸𝓿𝓮𝓻 ༻꧂',",callback_data=f"{fontkeyValue['BoldJavaneseText']}")
    op15 = InlineKeyboardButton("ᘛᗽ ɖɛǟȶɦʟօʋɛʀ ᘀᘗ'",callback_data=f"{fontkeyValue['RitualText']}")
    op16 = InlineKeyboardButton("𝓭𝓮𝓪𝓽𝓱𝓛𝓸𝓿𝓮𝓻",callback_data=f"{fontkeyValue['cursiveLettersBold']}")
    op17 = InlineKeyboardButton("╤╦︻ ƊƸ𐤠ƬǶȴΘƲƸⱤ ︻╦╤─",callback_data=f"{fontkeyValue['ak47GunText']}")
    op18 = InlineKeyboardButton("'ཫ꙳✱( ๔єคՇђɭ๏שєг )✱꙳ཀ",callback_data=f"{fontkeyValue['FooText']}")
    op19 = InlineKeyboardButton("DΣΛƬΉᄂӨVΣЯ ︻╦̵̵̿╤─ ҉~•",callback_data=f"{fontkeyValue['GunFire']}")
    op20 = InlineKeyboardButton("ᦔꫀꪖꪻꫝꪶꪮꪜꫀ᥅",callback_data=f"{fontkeyValue['taiVietCharMap']}")
    op21 = InlineKeyboardButton("𓂀 𝒹𝑒𝒶𝓉𝒽𝓛𝑜𝓋𝑒𝓇 𓂀",callback_data=f"{fontkeyValue['eyeOfHorusText']}")
    op22 = InlineKeyboardButton("𐋐﹍𖼜﹍𖼜﹍ 𝚍𝚎𝚊𝚝𝚑𝙻𝚘𝚟𝚎𝚛 ﹍𐋐﹍𐋐﹍𖼜𖼜﹍☀",callback_data=f"{fontkeyValue['Dessert']}")
    op23 = InlineKeyboardButton("'▟▛▜▟▛▜▟▛ 🄳🄴🄰🅃🄷🄻🄾🅅🄴🅁 ▟▛▜▟▛▜▟▛",callback_data=f"{fontkeyValue['checksText']}")
    op24 = InlineKeyboardButton("𝐝𝐞𝐚𝐭𝐡𝐋𝐨𝐯𝐞𝐫🌈™",callback_data=f"{fontkeyValue['RainbowText']}")
    op25 = InlineKeyboardButton("_꩜ 𝘥𝘦𝘢𝘵�𝘓𝘰𝘷𝘦𝘳 ꩜_",callback_data=f"{fontkeyValue['slowSnail']}")
    op26 = InlineKeyboardButton("(•_•)O*¯`·.¸ ๔єคՇђɭ๏שєг ¸.·´¯*O(•_•)",callback_data=f"{fontkeyValue['PingPong']}")
    op27 = InlineKeyboardButton("☆꧁✬◦°˚°◦. ɖɛ     ǟȶɦʟօʋɛʀ .◦°˚°◦✬꧂☆",callback_data=f"{fontkeyValue['MagicalText']}")
    op28 = InlineKeyboardButton("▄︻デɖɛǟȶɦʟօʋɛʀ═══━一",callback_data=f"{fontkeyValue['GunText']}")
    op29 = InlineKeyboardButton("꧁༺deathLover ༻꧂",callback_data=f"{fontkeyValue['JavaneseRerengganText']}")
    op30 = InlineKeyboardButton("·ᰄ· ԂⲈშԷ𐌷ᒷ❍ƲⲈՐ ·ᰄ·",callback_data=f"{fontkeyValue['featlyFont']}")
    op31= InlineKeyboardButton("▂▃▅▇█▓▒░𝚍𝚎𝚊𝚝𝚑𝙻𝚘�𝚎𝚛░░▒▓█▇▅▃▂",callback_data=f"{fontkeyValue['fadedBlock']}")
    op32 = InlineKeyboardButton("🄓🄔🄐🄣🄗🄛🄞🄥🄔🄡",callback_data=f"{fontkeyValue['bracketCharMap']}")
    op33 = InlineKeyboardButton("'一═デ︻ ∂єαтнℓσνєя ︻デ═一",callback_data=f"{fontkeyValue['gunFireText']}")

    
    option.add(op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11,op12,op13,op14,op15,
               op16,op17,op18,op19,op20,op21,op22,op23,op24,op25,op26,op27,op28,op29,op30,op31,op32,op33)
    
    """
    The below code use to filter the message sent to the bot and handle it
    # here i used conditional statement to remove the conflict occured during inline query and inline button
    if "#" in msg.text:
        separate = msg.text.split("#")
        #print(separate)
        bot.send_message(msg.chat.id,text=msg.text[1:],reply_markup=option)
    else:
        pass
    """
    bot.send_message(msg.chat.id,msg.text,reply_markup=option)
# this decorator handles when the buttons pressed
@bot.callback_query_handler(func=lambda m:True)
def styleText(msg):
    userMsg = msg.message.text
    clickedButton = msg.data
    chatID = msg.message.chat.id
    msgID = msg.message.id

    json_data = {
    'text': userMsg,
    'pages': [
        'latest',
        'beautiful',
        'classic',
    ],
    'code': 'main',
    'crazyness': 0,
        }

    response = requests.post('https://www.fontgen.net/build', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)

    try:
        if clickedButton == "font1":
            bot.edit_message_text(f' ```\n{data["greekCharMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font2":
            bot.edit_message_text(f' ```\n{data["upperAnglesCharMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font3":
            bot.edit_message_text(f' ```\n{data["BoldFloara"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font4":
            bot.edit_message_text(f' ```\n{data["NinjaText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font5":
            bot.edit_message_text(f' ```\n{data["doubleStruckCharMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font6":
            bot.edit_message_text(f' ```\n{data["neonCharMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font7":
            bot.edit_message_text(f' ```\n{data["oldEnglishCharBoldMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font8":
            bot.edit_message_text(f' ```\n{data["oldItalicText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font9":
            bot.edit_message_text(f' ```\n{data["FreeFireText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font10":
            bot.edit_message_text(f' ```\n{data["Ladyleo"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font11":
            bot.edit_message_text(f' ```\n{data["Blocky"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font12":
            bot.edit_message_text(f' ```\n{data["butterflyIt"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font13":
            bot.edit_message_text(f' ```\n{data["AstroFont"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font14":
            bot.edit_message_text(f' ```\n{data["BoldJavaneseText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font15":
            bot.edit_message_text(f' ```\n{data["RitualText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font16":
            bot.edit_message_text(f' ```\n{data["cursiveLettersBold"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font17":
            bot.edit_message_text(f' ```\n{data["ak47GunText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font18":
            bot.edit_message_text(f' ```\n{data["FooText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font19":
            bot.edit_message_text(f' ```\n{data["GunFire"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font19":
            bot.edit_message_text(f' ```\n{data["taiVietCharMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font20":
            bot.edit_message_text(f' ```\n{data["eyeOfHorusText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font21":
            bot.edit_message_text(f' ```\n{data["Dessert"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font22":
            bot.edit_message_text(f' ```\n{data["checksText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font23":
            bot.edit_message_text(f' ```\n{data["RainbowText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font24":
            bot.edit_message_text(f' ```\n{data["slowSnail"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font25":
            bot.edit_message_text(f' ```\n{data["PingPong"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font26":
            bot.edit_message_text(f' ```\n{data["MagicalText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font27":
            bot.edit_message_text(f' ```\n{data["GunText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font28":
            bot.edit_message_text(f' ```\n{data["JavaneseRerengganText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font29":
            bot.edit_message_text(f' ```\n{data["featlyFont"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font30":
            bot.edit_message_text(f' ```\n{data["fadedBlock"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font31":
            bot.edit_message_text(f' ```\n{data["bracketCharMap"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "font32":
            bot.edit_message_text(f' ```\n{data["gunFireText"]}``` ',chatID,msgID,reply_markup=button,parse_mode="MarkdownV2")
        elif clickedButton == "back":
            bot.edit_message_reply_markup(chatID,msgID,reply_markup=option)
        else:
            bot.send_message(chatID,"Please click the Button")
    except Exception as ex:
        print(ex)
    

# this decorator handles query through inline 
@bot.inline_handler(func=lambda m:True)
def inlineStyleText(msg):
    id = msg.id
    userMsg = msg.query
    json_data = {
    'text': userMsg,
    'pages': [
        'latest',
        'beautiful',
        'classic',
    ],
    'code': 'main',
    'crazyness': 0,
        }

    response = requests.post('https://www.fontgen.net/build', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)

    
    markup = InlineKeyboardMarkup()
    channel = InlineKeyboardButton(text="⚡️",url="t.me/neuralp")
    markup.add(channel)
    
    try:
        font1 = InlineQueryResultArticle(1,"∂єαтнℓσνєя",InputTextMessageContent(data["greekCharMap"]),reply_markup=markup)
        font2 = InlineQueryResultArticle(2,"DΣΛƬΉᄂӨVΣЯ",InputTextMessageContent(data["upperAnglesCharMap"]),reply_markup=markup)
        font3 = InlineQueryResultArticle(3,"❀ꗥ～ꗥ❀ 𝐝𝐞𝐚𝐭𝐡𝐋 𝐨𝐯𝐞𝐫 ❀ꗥ～ꗥ❀",InputTextMessageContent(data["BoldFloara"]),reply_markup=markup)
        font4 = InlineQueryResultArticle(4,"đēⱥⱦħŁꝋꝟēɍ𓆪",InputTextMessageContent(data["NinjaText"]),reply_markup=markup)
        font5 = InlineQueryResultArticle(5,"𝕕𝕖𝕒𝕥𝕙𝕃𝕠𝕧𝕖𝕣",InputTextMessageContent(data["doubleStruckCharMap"]),reply_markup=markup)
        font6 = InlineQueryResultArticle(6,"ᗪEᗩTᕼᒪOᐯEᖇ",InputTextMessageContent(data["neonCharMap"]),reply_markup=markup)
        font7 = InlineQueryResultArticle(7,"𝖉𝖊𝖆𝖙𝖍𝕷𝖔𝖛𝖊𝖗",InputTextMessageContent(data["oldEnglishCharBoldMap"]),reply_markup=markup)
        font8 = InlineQueryResultArticle(8,"𐌃𐌄𐌀𐌕𐋅𐌋Ꝋᕓ𐌄𐌓",InputTextMessageContent(data["oldItalicText"]),reply_markup=markup)
        font9 = InlineQueryResultArticle(9,"★彡( ĐɆ₳₮ⱧⱠØVɆⱤ )彡★",InputTextMessageContent(data["FreeFireText"]),reply_markup=markup)
        font10 = InlineQueryResultArticle(10,"❀💋❀ ƊƸ𐤠ƬǶȴΘƲƸⱤ ❀💋❀",InputTextMessageContent(data["Ladyleo"]),reply_markup=markup)
        font11 = InlineQueryResultArticle(11,"▁▂▄▅▆▇█ DΣΛƬΉᄂӨVΣЯ █▇▆▅▄▂▁",InputTextMessageContent(data["Blocky"]),reply_markup=markup)
        font12 = InlineQueryResultArticle(12,"♥Ƹ̵̡Ӝ ̵̨̄Ʒ♥ 𝖉𝖊𝖆𝖙𝖍𝕷𝖔𝖛𝖊𝖗 ♥Ƹ̵̡Ӝ̵̨̄Ʒ♥",InputTextMessageContent(data["butterflyIt"]),reply_markup=markup)
        font13 = InlineQueryResultArticle(13,"✫☼☾☁ 𝝙𝝚𝝖𝝩𝝜Ⳑ𝝤ꓴ𝝚Ɍ ☁☾☼✫",InputTextMessageContent(data["AstroFont"]),reply_markup=markup)
        font14 = InlineQueryResultArticle(14,"꧁༺ 𝓭𝓮𝓪𝓽𝓱𝓛𝓸𝓿𝓮𝓻 ༻꧂",InputTextMessageContent(data["BoldJavaneseText"]),reply_markup=markup)
        font15 = InlineQueryResultArticle(15,"ᘛᗽ ɖɛǟȶɦʟօʋɛʀ ᘀᘗ",InputTextMessageContent(data["RitualText"]),reply_markup=markup)
        font16 = InlineQueryResultArticle(16,"𝓭𝓮𝓪𝓽𝓱𝓛𝓸𝓿𝓮𝓻",InputTextMessageContent(data["cursiveLettersBold"]),reply_markup=markup)
        font17 = InlineQueryResultArticle(17,"╤╦︻ ƊƸ𐤠ƬǶȴΘƲƸⱤ ︻╦╤─",InputTextMessageContent(data["ak47GunText"]),reply_markup=markup)
        font18 = InlineQueryResultArticle(18,"ཫ꙳✱( ๔єคՇђɭ๏שєг )✱꙳ཀ",InputTextMessageContent(data["FooText"]),reply_markup=markup)
        font19 = InlineQueryResultArticle(19,"DΣΛƬΉᄂӨVΣЯ ︻╦̵̵̿╤─ ҉~•",InputTextMessageContent(data["GunFire"]),reply_markup=markup)
        font20 = InlineQueryResultArticle(20,"ᦔꫀꪖꪻꫝꪶꪮꪜꫀ᥅",InputTextMessageContent(data["eyeOfHorusText"]),reply_markup=markup)
        font21 = InlineQueryResultArticle(21,"𓂀 𝒹𝑒𝒶𝓉𝒽𝓛𝑜𝓋𝑒𝓇 𓂀",InputTextMessageContent(data["Dessert"]),reply_markup=markup)
        font22 = InlineQueryResultArticle(22,"𐋐﹍𖼜﹍𖼜﹍ 𝚍𝚎𝚊𝚝𝚑𝙻𝚘𝚟𝚎𝚛 ﹍𐋐﹍𐋐﹍𖼜𖼜﹍☀",InputTextMessageContent(data["checksText"]),reply_markup=markup)
        font23 = InlineQueryResultArticle(23,"▟▛▜▟▛▜▟▛ 🄳🄴🄰🅃🄷🄻🄾🅅🄴🅁 ▟▛▜▟▛▜▟▛",InputTextMessageContent(data["RainbowText"]),reply_markup=markup)
        font24 = InlineQueryResultArticle(24,"𝐝𝐞𝐚𝐭𝐡𝐋𝐨𝐯𝐞𝐫🌈™",InputTextMessageContent(data["slowSnail"]),reply_markup=markup)
        font25 = InlineQueryResultArticle(25,"_꩜ 𝘥𝘦𝘢𝘵�𝘓𝘰𝘷𝘦𝘳 ꩜_",InputTextMessageContent(data["PingPong"]),reply_markup=markup)
        font26 = InlineQueryResultArticle(26,"(•_•)O*¯`·.¸ ๔єคՇђɭ๏שєг ¸.·´¯*O(•_•)",InputTextMessageContent(data["MagicalText"]),reply_markup=markup)
        font27 = InlineQueryResultArticle(27,"☆꧁✬◦°˚°◦. ɖɛ     ǟȶɦʟօʋɛʀ .◦°˚°◦✬꧂☆",InputTextMessageContent(data["GunText"]),reply_markup=markup)
        font28 = InlineQueryResultArticle(28,"▄︻デɖɛǟȶɦʟօʋɛʀ═══━一",InputTextMessageContent(data["JavaneseRerengganText"]),reply_markup=markup)
        font29 = InlineQueryResultArticle(29,"꧁༺deathLover ༻꧂",InputTextMessageContent(data["featlyFont"]),reply_markup=markup)
        font30 = InlineQueryResultArticle(30,"·ᰄ· ԂⲈშԷ𐌷ᒷ❍ƲⲈՐ ·ᰄ·",InputTextMessageContent(data["fadedBlock"]),reply_markup=markup)
        font31 = InlineQueryResultArticle(31,"▂▃▅▇█▓▒░𝚍𝚎𝚊𝚝𝚑𝙻𝚘�𝚎𝚛░░▒▓█▇▅▃▂",InputTextMessageContent(data["bracketCharMap"]),reply_markup=markup)
        font32 = InlineQueryResultArticle(32,"🄓🄔🄐🄣🄗🄛🄞🄥🄔🄡",InputTextMessageContent(data["gunFireText"]),reply_markup=markup)

        bot.answer_inline_query(id,[font1,font2,font3,font4,font5,font6,font7,font8,font9,font10,font11,font12,font13,font14,font15,font16,font17,
                                    font18,font19,font20,font21,font22,font23,font24,font25,font26,font27,font28,font29,font30,font31,font32])
    except Exception as e:
        print(e)


bot.infinity_polling()


