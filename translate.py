from googletrans import Translator
import pyperclip
import json

translator = Translator()


def get_clipboard():
    return pyperclip.paste()


def translate(phrase):
    return translator.translate(phrase, dest='ja')


previous = get_clipboard()

while True:
    if (clipboard := get_clipboard()) != previous:
        print(clipboard)
        pyperclip.copy(translate(clipboard).text)
