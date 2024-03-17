import speech_recognition as sr
import pyautogui
import time
from easygoogletranslate import EasyGoogleTranslate
from colorama import Fore, Style, init
import pyperclip
import os

init()
os.system('cls')
os.system("title Roblox Speech to Translated Text")

print(Fore.MAGENTA + r"""
__________ ________ __________.____    ________  ____  ___                                            
\______   \\_____  \\______   \    |   \_____  \ \   \/  /                                            
 |       _/ /   |   \|    |  _/    |    /   |   \ \     /                                             
 |    |   \/    |    \    |   \    |___/    |    \/     \                                             
 |____|_  /\_______  /______  /_______ \_______  /___/\  \                                            
        \/         \/       \/        \/       \/      \_/                                            
  __________________________________________________   ___ ___                                        
 /   _____/\______   \_   _____/\_   _____/\_   ___ \ /   |   \                                       
 \_____  \  |     ___/|    __)_  |    __)_ /    \  \//    ~    \                                      
 /        \ |    |    |        \ |        \\     \___\    Y    /                                      
/_______  / |____|   /_______  //_______  / \______  /\___|_  /                                       
        \/                   \/         \/         \/       \/                                        
_____________________    _____    _______    _________.____       ________________________ __________ 
\__    ___/\______   \  /  _  \   \      \  /   _____/|    |     /  _  \__    ___/\_____  \\______   \
  |    |    |       _/ /  /_\  \  /   |   \ \_____  \ |    |    /  /_\  \|    |    /   |   \|       _/
  |    |    |    |   \/    |    \/    |    \/        \|    |___/    |    \    |   /    |    \    |   \
  |____|    |____|_  /\____|__  /\____|__  /_______  /|_______ \____|__  /____|   \_______  /____|_  /
                   \/         \/         \/        \/         \/       \/                 \/       \/ 
                             By: theboety & paradiseeffect
--------------------------------------------------------------------------------------------------------
""" + Style.RESET_ALL)


language_codes = {
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "assamese": "as",
    "aymara": "ay",
    "azerbaijani": "az",
    "bambara": "bm",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bhojpuri": "bho",
    "bosnian": "bs",
    "bulgarian": "bg",
    "catalan": "ca",
    "cebuano": "ceb",
    "chinese": "zh",
    "chinese zh-tw": "zh-TW",
    "corsican": "co",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dhivehi": "dv",
    "dogri": "doi",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "ewe": "ee",
    "filipino": "fil",
    "finnish": "fi",
    "french": "fr",
    "frisian": "fy",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "guarani": "gn",
    "gujarati": "gu",
    "haitian creole": "ht",
    "hausa": "ha",
    "hawaiian": "haw",
    "hebrew": "he",
    "hindi": "hi",
    "hmong": "hmn",
    "hungarian": "hu",
    "icelandic": "is",
    "igbo": "ig",
    "ilocano": "ilo",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jv",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "kinyarwanda": "rw",
    "konkani": "gom",
    "korean": "ko",
    "krio": "kri",
    "kurdish": "ku",
    "kyrgyz": "ky",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lingala": "ln",
    "lithuanian": "lt",
    "luganda": "lg",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "maithili": "mai",
    "malagasy": "mg",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "meiteilon mni-mtei": "mni-Mtei",
    "mizo": "lus",
    "mongolian": "mn",
    "myanmar": "my",
    "nepali": "ne",
    "norwegian": "no",
    "nyanja": "ny",
    "odia": "or",
    "oromo": "om",
    "pashto": "ps",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "quechua": "qu",
    "romanian": "ro",
    "russian": "ru",
    "samoan": "sm",
    "sanskrit": "sa",
    "scots gaelic": "gd",
    "sepedi": "nso",
    "serbian": "sr",
    "sesotho": "st",
    "shona": "sn",
    "sindhi": "sd",
    "sinhala": "si",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tagalog": "tl",
    "tajik": "tg",
    "tamil": "ta",
    "tatar": "tt",
    "telugu": "te",
    "thai": "th",
    "tigrinya": "ti",
    "tsonga": "ts",
    "turkish": "tr",
    "turkmen": "tk",
    "twi": "ak",
    "ukrainian": "uk",
    "urdu": "ur",
    "uyghur": "ug",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
    "zulu": "zu"
}

def translate_text(input_text, target_language):
    translator = EasyGoogleTranslate(target_language=target_language)
    translated_text = translator.translate(input_text)
    return translated_text

def get_target_language():
    while True:
        target_language_input = input("Enter the name of the target language: ").lower()  # Convert input to lowercase
        if target_language_input in language_codes:
            language_name = target_language_input
            iso_code = language_codes[target_language_input]
            return language_name, iso_code
        else:
            print(Fore.RED + "Language not found. Please enter a valid language name." + Style.RESET_ALL)

def listen_and_translate(target_language):

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.WHITE + "Listening..." + Style.RESET_ALL)
        audio = recognizer.listen(source)

    try:
        
        input_text = recognizer.recognize_google(audio)
        print(Fore.YELLOW + "You said: " + input_text + Style.RESET_ALL)
        translated_text = translate_text(input_text, target_language)
        print(Fore.GREEN + "Translated text: " + translated_text + Style.RESET_ALL)
        
        
        pyperclip.copy(translated_text) #this is so that pyautogui can type it, because it doesn't recognize some of the characters from other languages.
        pyautogui.keyDown('/')
        pyautogui.keyUp('/') ########## For making use with other platforms, this can be removed, this is only here so it starts typing in roblox. ##########
        time.sleep(0.5)  
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)  
        pyautogui.press('enter')
    except sr.UnknownValueError:
        print(Fore.WHITE + "Background noise..." + Style.RESET_ALL)
    except sr.RequestError as e:
        print(Fore.RED + f"Could not request results from Google Speech Recognition service; {e}" + Style.RESET_ALL)


target_language_name, target_language_iso_code = get_target_language()


while True:
    listen_and_translate(target_language_iso_code)
