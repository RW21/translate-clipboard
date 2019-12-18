from googletrans import Translator
import pyperclip

translator = Translator()


def get_clipboard():
    return pyperclip.paste()


def translate(phrase):
    return translator.translate(phrase, dest='ja')


previous = ''

while True:
    clipboard = get_clipboard()
    if clipboard != previous:
        previous = clipboard
        pyperclip.copy(translate(clipboard).text)
