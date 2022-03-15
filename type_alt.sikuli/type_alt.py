# -*- coding: utf-8 -*-
from sikuli import *
# Copyright (C)2022 WitHub Tecnologia, Marketing e Educação
# Free for use under MIT License
# Author: Felipe Garbin
# Contact: lipnotic@gmail.com
# Dictionary codes extracted from https://www.freecodecamp.org/news/alt-codes-special-characters-keyboard-symbols-windows-list/ (4 digits codes)
# And from https://theasciicode.com.ar/ascii-codes.txt for 3 digits codes
dict_alt = { 
u"Ç":"128",
u"ü":"129",
u"é":"130",
u"â":"131",
u"ä":"132",
u"à":"133",
u"å":"134",
u"ç":"135",
u"ê":"136",
u"ë":"137",
u"è":"138",
u"ï":"139",
u"î":"140",
u"ì":"141",
u"Ä":"142",
u"Å":"143",
u"É":"144",
u"æ":"145",
u"Æ":"146",
u"ô":"147",
u"ö":"148",
u"ò":"149",
u"û":"150",
u"ù":"151",
u"ÿ":"152",
u"Ö":"153",
u"Ü":"154",
u"ø":"155",
u"£":"156",
u"Ø":"157",
u"×":"158",
u"ƒ":"159",
u"á":"160",
u"í":"161",
u"ó":"162",
u"ú":"163",
u"ñ":"164",
u"Ñ":"165",
u"ª":"166",
u"º":"167",
u"¿":"168",
u"®":"169",
u"¬":"170",
u"½":"171",
u"¼":"172",
u"¡":"173",
u"«":"174",
u"»":"175",
u"░":"176",
u"▒":"177",
u"▓":"178",
u"│":"179",
u"┤":"180",
u"Á":"181",
u"Â":"182",
u"À":"183",
u"©":"184",
u"╣":"185",
u"║":"186",
u"╗":"187",
u"╝":"188",
u"¢":"189",
u"¥":"190",
u"┐":"191",
u"└":"192",
u"┴":"193",
u"┬":"194",
u"├":"195",
u"─":"196",
u"┼":"197",
u"ã":"198",
u"Ã":"199",
u"╚":"200",
u"╔":"201",
u"╩":"202",
u"╦":"203",
u"╠":"204",
u"═":"205",
u"╬":"206",
u"¤":"207",
u"ð":"208",
u"Ð":"209",
u"Ê":"210",
u"Ë":"211",
u"È":"212",
u"ı":"213",
u"Í":"214",
u"Î":"215",
u"Ï":"216",
u"┘":"217",
u"┌":"218",
u"█":"219",
u"▄":"220",
u"¦":"221",
u"Ì":"222",
u"▀":"223",
u"Ó":"224",
u"ß":"225",
u"Ô":"226",
u"Ò":"227",
u"õ":"228",
u"Õ":"229",
u"µ":"230",
u"þ":"231",
u"Þ":"232",
u"Ú":"233",
u"Û":"234",
u"Ù":"235",
u"ý":"236",
u"Ý":"237",
u"¯":"238",
u"´":"239",
u"¬":"240",
u"±":"241",
u"‗":"242",
u"¾":"243",
u"¶":"244",
u"§":"245",
u"÷":"246",
u"¸":"247",
u"°":"248",
u"¨":"249",
u"•":"250",
u"¹":"251",
u"³":"252",
u"²":"253",
u"■":"254",
u" ":"255",
u"€":"0128",
u"‘":"0130",
u"ƒ":"0131",
u"„":"0132",
u"…":"0133",
u"†":"0134",
u"‡":"0135",
u"‰":"0137",
u"Š":"0138",
u"‹":"0139",
u"Œ":"0140",
u"Ž":"0142",
u"‘":"0145",
u"’":"0146",
u"“":"0147",
u"”":"0148",
u"—":"0151",
u"™":"0153",
u"š":"0154",
u"›":"0155",
u"œ":"0156",
u"ž":"0158",
u"Ÿ":"0159",
u"¤":"0164",
u"¦":"0166",
u"¨":"0168",
u"©":"0169",
u"¯":"0175",
u"²":"0178",
u"³":"0179",
u"´":"0180",
u"·":"0183",
u"¸":"0184",
u"¹":"0185",
u"¼":"0188",
u"½":"0189",
u"¾":"0190",
u"À":"0192",
u"Á":"0193",
u"Â":"0194",
u"Ã":"0195",
u"Ä":"0196",
u"Å":"0197",
u"Æ":"0198",
u"Ç":"0199",
u"È":"0200",
u"É":"0201",
u"Ê":"0202",
u"Ë":"0203",
u"Ì":"0204",
u"Í":"0205",
u"Ï":"0206",
u"Ï":"0207",
u"Ð":"0208",
u"Ò":"0210",
u"Ó":"0211",
u"Ô":"0212",
u"Õ":"0213",
u"Ö":"0214",
u"×":"0215",
u"Ø":"0216",
u"Ù":"0217",
u"Ú":"0218",
u"Û":"0219",
u"Ü":"0220",
u"Ý":"0221",
u"Þ":"0222",
u"ß":"0223",
u"à":"0224",
u"á":"0225",
u"â":"0226",
u"ã":"0227",
u"ä":"0228",
u"å":"0229",
u"æ":"0230",
u"ç":"0231",
u"è":"0232",
u"é":"0233",
u"ê":"0234",
u"ë":"0235",
u"ì":"0236",
u"í":"0237",
u"î":"0238",
u"ï":"0239",
u"ð":"0240",
u"ò":"0242",
u"ó":"0243",
u"ô":"0244",
u"õ":"0245",
u"ö":"0246",
u"÷":"0247",
u"ø":"0248",
u"ú":"0249",
u"û":"0250",
u"ü":"0251",
u"ù":"0252",
u"ý":"0253",
u"þ":"0254",
u"ÿ":"0255"
}

def type_alt(line):
    for letter in line:
        nums = dict_alt.get(letter, "")
        if nums == "":
            type(letter)
            continue
        keyDown(Key.ALT)
        for n in nums:
            # Here the eval() function was used to be able to "attach" the variable n 'to the expression Key.NUM2 for example where the number varies according to the code collected by the dictionary
            eval( "type(Key.NUM" + n + ")" )
        keyUp()