from googletrans import Translator
import pyperclip
import sys

source = 'en'
target = 'ja'

translator = Translator()


def setup():
    if len(sys.argv) != 1:
        global source
        global target
        source = sys.argv[1]
        target = sys.argv[2]

    if len(sys.argv) > 2:
        print("""
        Usage: python3 translate.py <source language> <target language
        """)


def get_clipboard():
    return pyperclip.paste()


def translate(phrase):
    return translator.translate(phrase, src=source, dest=target)


def treat_string(string: str):
    if string.endswith('\n'):
        return string[:-1]
    else:
        return string


def verify_copied(copied):
    if copied is None:
        return str(None)

    return copied


def main():
    setup()

    print('service start')

    previous = ''
    translated = ''

    while True:

        if (clipboard := get_clipboard()) != previous and clipboard is not None and translated != clipboard:
            translated = translate(clipboard).text
            pyperclip.copy(translated)
            print(f'{treat_string(clipboard)} -> {treat_string(translated)}')


try:
    main()
except KeyboardInterrupt:
    print('exit')
    sys.exit()
