from googletrans import Translator
import pyperclip

translator = Translator()


def get_clipboard():
    return pyperclip.paste()


def translate(phrase):
    return translator.translate(phrase, dest='ja')


previous = ''

while True:
    if (clipboard := get_clipboard()) != previous:
        previous = clipboard
        pyperclip.copy(translate(clipboard).text)
