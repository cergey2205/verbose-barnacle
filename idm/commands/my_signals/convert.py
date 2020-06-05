from ...objects import dp, MySignalEvent
from ...utils import edit_message, new_message, delete_message, sticker_message

@dp.my_signal_event_handle('раск', 'hfcr', 'конв')
def convert(event: MySignalEvent) -> str:
    _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
    _trans_table = dict(zip(_eng_chars, _rus_chars))
    s = ''
    if bool(event.args):
        s = " ".join(event.args)
    if bool(event.payload):
        s = s + '\n' + event.payload
    if event.reply_message != None:
        s = s + '\n' + event.reply_message['text']
    if s == '':
        new_message(event.api, event.chat.peer_id, message='Нет данных 🤦')
    msg = u''.join([_trans_table.get(c, c) for c in s])
    new_message(event.api, event.chat.peer_id, message=msg)
    return "ok"

@dp.my_signal_event_handle('шрифты')
def fonts(event: MySignalEvent) -> str:
    new_message(event.api, event.chat.peer_id, message="""
    1. 𝕠𝕦𝕥𝕝𝕚𝕟𝕖 (outline)
    2. 𝚝𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛 (typewriter)
    3. 𝓈𝒸𝓇𝒾𝓅𝓉 (script)
    4. 𝓼𝓬𝓻𝓲𝓹𝓽_𝓫𝓸𝓵𝓭 (script_bold)
    5. zɾƃlɟq_ɟʞuʍ (upside_down)
    6. ᴛɪɴʏ_ᴄᴀᴘs (tiny_caps)
    7. ᑕOᗰIᑕ (comic)
    8. 𝐬𝐞𝐫𝐢𝐟_𝐛 (serif_b)
    9. 𝑠𝑒𝑟𝑖𝑓_𝑖 (serif_i)
    10. 𝒔𝒆𝒓𝒊𝒇_𝒃𝒊 (serif_bi)
    11. ⒸⒾⓇⒸⓁⒺⓈ (circles)
    12. 🅒🅘🅡🅒🅛🅔🅢_🅑 (circles_b)
    13. 🅂🅀🅄🄰🅁🄴🅂 (squares)
    14. 𝔤𝔬𝔱𝔥𝔦𝔠 (gothic)
    15. 𝖌𝖔𝖙𝖍𝖎𝖈_𝖇 (gothic_b)""")

@dp.my_signal_event_handle('шрифт')
def font(event: MySignalEvent) -> str:
    alw = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    if event.args:
        if event.args[0] == '1':
            dest = u"~!@#$%^&𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡[]𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝;'𝕫𝕩𝕔𝕧𝕓𝕟𝕞,./ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ{}𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃:\"|ℤ𝕏ℂ𝕍𝔹ℕ𝕄<>?"
        elif event.args[0] == '2':
            dest = u"~!@#$%^&𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙[]𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕;'𝚣𝚡𝚌𝚟𝚋𝚗𝚖,./𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿{}𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻:\"|𝚉𝚇𝙲𝚅𝙱𝙽𝙺<>?"
        elif event.args[0] == '3':
            dest = u"~!@#$%^&𝓆𝓌ℯ𝓇𝓉𝓎𝓊𝒾ℴ𝓅[]𝒶𝓈𝒹𝒻ℊ𝒽𝒿𝓀𝓁;'𝓏𝓍𝒸𝓋𝒷𝓃𝓂,./𝒬𝒲ℰℛ𝒯𝒴𝒰ℐ𝒪𝒫{}𝒜𝒮𝒟ℱ𝒢ℋ𝒥𝒦ℒ:\"|𝒵𝒳𝒞𝒱ℬ𝒩ℳ<>?"
        elif event.args[0] == '4':
            dest = u"~!@#$%^&𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹[]𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵;'𝔃𝔁𝓬𝓿𝓫𝓷𝓶,./𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟{}𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛:\"|𝓩𝓧𝓒𝓥𝓑𝓝𝓜<>?"
        elif event.args[0] == '5':
            dest = u"~¡@#$%^&ɯuqʌɔxzlʞɾ[]ɥƃɟpsɐdoᴉ;'nʎʇɹǝʍb,./ɯuqʌɔxzlʞɾ{}ʎƃɟpsɐdoᴉ:\"|nʎʇɹǝʍb<>¿"
        elif event.args[0] == '6':
            dest = u"~!@#$%^&ǫᴡᴇʀᴛʏᴜɪᴏᴘ[]ᴀsᴅғɢʜᴊᴋʟ;'ᴢxᴄᴠʙɴᴍ,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
        elif event.args[0] == '7':
            dest = u"~!@#$%^&ᑫᗯᗴᖇTYᑌIOᑭ[]ᗩՏᗪᖴᘜᕼᒍKᒪ;'ᘔ᙭ᑕᐯᗷᑎᗰ,./ᑫᗯᗴᖇTYᑌIOᑭ{}ᗩՏᗪᖴᘜᕼᒍKᒪ:\"|ᘔ᙭ᑕᐯᗷᑎᗰ<>?"
        elif event.args[0] == '8':
            dest = u"~!@#$%^&𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩[]𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥;'𝐳𝐱𝐜𝐯𝐛𝐧𝐦,./𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏{}𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋:\"|𝐙𝐗𝐂𝐕𝐁𝐍𝐌<>?"
        elif event.args[0] == '9':
            dest = u"~!@#$%^&𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝[]𝑎𝑠𝑑𝑓𝑔ℎ𝑗𝑘𝑙;'𝑧𝑥𝑐𝑣𝑏𝑛𝑚,./𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃{}𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿:\"|𝑍𝑋𝐶𝑉𝐵𝑁𝑀<>?"
        elif event.args[0] == '10':
            dest = u"~!@#$%^&𝒒𝒘𝒆𝒓𝒕𝒚𝒖𝒊𝒐𝒑[]𝒂𝒔𝒅𝒇𝒈𝒉𝒋𝒌𝒍;'𝒛𝒙𝒄𝒗𝒃𝒏𝒎,./𝑸𝑾𝑬𝑹𝑻𝒀𝑼𝑰𝑶𝑷{}𝑨𝑺𝑫𝑭𝑮𝑯𝑱𝑲𝑳:\"|𝒁𝑿𝑪𝑽𝑩𝑵𝑴<>?"
        elif event.args[0] == '11':
            dest = u"~!@#$%^&ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ[]ⒶⓈⒹⒻⒼⒽⒿⓀⓁ;'ⓏⓍⒸⓋⒷⓃⓂ,./ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ{}ⒶⓈⒹⒻⒼⒽⒿⓀⓁ:\"|ⓏⓍⒸⓋⒷⓃⓂ<>?"
        elif event.args[0] == '12':
            dest = u"~!@#$%^&🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟[]🅐🅢🅓🅕🅖🅗🅙🅚🅛;'🅩🅧🅒🅥🅑🅝🅜,./🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟{}🅐🅢🅓🅕🅖🅗🅙🅚🅛:\"|🅩🅧🅒🅥🅑🅝🅜<>?"
        elif event.args[0] == '13':
            dest = u"~!@#$%^&🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿[]🄰🅂🄳🄵🄶🄷🄹🄺🄻;'🅉🅇🄲🅅🄱🄽🄼,./🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿{}🄰🅂🄳🄵🄶🄷🄹🄺🄻:\"|🅉🅇🄲🅅🄱🄽🄼<>?"
        elif event.args[0] == '14':
            dest = u"~!@#$%^&𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭[]𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩;'𝔷𝔵𝔠𝔳𝔟𝔫𝔪,./𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓{}𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏:\"|ℨ𝔛ℭ𝔙𝔅𝔑𝔐<>?"
        elif event.args[0] == '15':
            dest = u"~!@#$%^&𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕[]𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑;'𝖟𝖝𝖈𝖛𝖇𝖓𝖒,./𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻{}𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷:\"|𝖅𝖃𝕮𝖁𝕭𝕹𝕸<>?"
    else:
        edit_message(event.api, event.chat.peer_id, event.msg['id'], message="""
        Просмотр списка шрифтов - .с шрифты
        \nКоманда для конвертации:\n.с шрифт [номер]\n[текст]
        \n!Русские буквы игнорируются""")
    fonts = dict(zip(alw, dest))
    s = event.payload
    msg = u''.join([fonts.get(c, c) for c in s])
    edit_message(event.api, event.chat.peer_id, event.msg['id'], message=msg)
    return "ok"