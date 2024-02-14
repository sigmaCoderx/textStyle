
import json
import requests
from telebot import TeleBot,types,util
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
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

bot = TeleBot("6729835437:AAHHhiVCEz9Fa_ANtUCrldxQQ8tXMA5WL-c",parse_mode="HTML")

button = InlineKeyboardMarkup()
button.row_width = 2
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
toFonts = InlineKeyboardButton(text="🔙",callback_data="back")
button.add(group,channel,toFonts)

@bot.message_handler(commands=["start"])
def greetUser(msg):
    text = f"Hey dear{user_link(msg.from_user)}send text to style and select your best font on the button"
    bot.reply_to(msg,text,reply_markup=button)

@bot.message_handler(func=lambda m:True)
def chooseFont(msg):

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
    
    bot.send_message(msg.chat.id,text=msg.text,reply_markup=option)

    @bot.callback_query_handler(func=lambda m:True)
    def styleText(msg):
        userMsg = msg.message.text
        clickedButton = msg.data
        chatID = msg.message.chat.id
        msgID = msg.message.id

        data = {
        'text': userMsg,
        'pages': [
            'latest',
            'beautiful',
            'classic',
        ],
        'code': 'main',
        'crazyness': 0,
          }

        response = requests.post('https://www.fontgen.net/build', cookies=cookies, headers=headers, json=data)
        data = json.loads(response.text)

       
        if clickedButton == "font1":
            bot.edit_message_text(data["greekCharMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font2":
            bot.edit_message_text(data["upperAnglesCharMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font3":
            bot.edit_message_text(data["BoldFloara"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font4":
            bot.edit_message_text(data["NinjaText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font5":
            bot.edit_message_text(data["doubleStruckCharMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font6":
            bot.edit_message_text(data["neonCharMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font7":
            bot.edit_message_text(data["oldEnglishCharBoldMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font8":
            bot.edit_message_text(data["oldItalicText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font9":
            bot.edit_message_text(data["FreeFireText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font10":
            bot.edit_message_text(data["Ladyleo"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font11":
            bot.edit_message_text(data["Blocky"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font12":
            bot.edit_message_text(data["butterflyIt"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font13":
            bot.edit_message_text(data["AstroFont"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font14":
            bot.edit_message_text(data["BoldJavaneseText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font15":
            bot.edit_message_text(data["RitualText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font16":
            bot.edit_message_text(data["cursiveLettersBold"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font17":
            bot.edit_message_text(data["ak47GunText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font18":
            bot.edit_message_text(data["FooText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font19":
            bot.edit_message_text(data["GunFire"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font19":
            bot.edit_message_text(data["taiVietCharMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font20":
            bot.edit_message_text(data["eyeOfHorusText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font21":
            bot.edit_message_text(data["Dessert"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font22":
            bot.edit_message_text(data["checksText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font23":
            bot.edit_message_text(data["RainbowText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font24":
            bot.edit_message_text(data["slowSnail"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font25":
            bot.edit_message_text(data["PingPong"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font26":
            bot.edit_message_text(data["MagicalText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font27":
            bot.edit_message_text(data["GunText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font28":
            bot.edit_message_text(data["JavaneseRerengganText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font29":
            bot.edit_message_text(data["featlyFont"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font30":
            bot.edit_message_text(data["fadedBlock"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font31":
            bot.edit_message_text(data["bracketCharMap"],chatID,msgID,reply_markup=button)
        elif clickedButton == "font32":
            bot.edit_message_text(data["gunFireText"],chatID,msgID,reply_markup=button)
        elif clickedButton == "back":
            bot.edit_message_reply_markup(chatID,msgID,reply_markup=option)
        else:
            bot.send_message(chatID,"Please click the Button")
        



bot.infinity_polling()


