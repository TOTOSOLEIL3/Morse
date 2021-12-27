import time
import pyttsx3 as pyttsx
                 
MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}


def Txt_to_Morse():
    txt = input('Entre le texte Ã  convertir: ')
    code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in txt if i.upper() in MORSE_CODE_DICT.keys()]
    morse=''.join(code)
    print(morse)
    
def Morse_to_Txt():
    txt = input('Entre ton code morse a convertir en texte ')
    code = [k for i in txt.split() for k,v in MORSE_CODE_DICT.items() if i==v]
    newtxt = ''.join(code)
    print(newtxt)
    engine = pyttsx.init()
    engine.say(newtxt)
    engine.runAndWait()

print('''\n1 - Convertir texte en morse \n2 - Convertir morse en texte\n3 - quitter\n ''')

while True:
    try:
        selection = int(input('Choisis ton mode:'))
        if selection == 1:
            print(Txt_to_Morse())
            break
        elif selection == 2:
            print(Morse_to_Txt())
            break
        elif selection == 3:
            print('Exiting')
            break
        else:
            print('Mauvaise selection, recommence')
    except:
        print('Mauvaise selection, recommence')
