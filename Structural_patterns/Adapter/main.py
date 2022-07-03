class Russian:

    def __init__(self):
        self.__message = None

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


class Morse:

    def __init__(self):
        self.__message = None

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


class MorseToRussianAdapter(Russian):
    __alphabet = {
        'А': '.-',
        'Б': '-...',
        'В': '.--',
        'Г': '--.',
        'Д': '-..',
        'Е': '.',
        'Ж': '...-',
        'З': '--..',
        'И': '..',
        'Й': '.---',
        'К': '-.-',
        'Л': '.-..',
        'М': '--',
        'Н': '-.',
        'О': '---',
        'П': '.--.',
        'Р': '.-.',
        'С': '...',
        'Т': '-',
        'У': '..-',
        'Ф': '..-.',
        'Х': '....',
        'Ц': '-.-.',
        'Ч': '---.',
        'Ш': '----',
        'Щ': '--.-',
        'Ъ': '--.--',
        'Ы': '-.--',
        'Ь': '-..-',
        'Э': '..-..',
        'Ю': '..--',
        'Я': '.-.-',
        '.': '.-.-.-',
        ',': '--..--',
        '-': '-.... -',
        '_': '.. - -.-',
        '—': '—',
        ' ': ''
    }

    def __init__(self, morse: Morse):
        super().__init__()
        self.__morse = morse

    @property
    def message(self) -> str:
        return self.__translate(self.__morse)

    def __translate(self, morse: Morse) -> str:
        split_text = morse.message.split(' ')
        translate = ''
        for word in split_text:
            for key, value in self.__alphabet.items():
                if word == value:
                    translate += key
                    break
        return translate.capitalize()


if __name__ == "__main__":
    message = ".- -.. .- .--. - . .-.  —  ..-.. - ---  ... - .-. ..- -.- - ..- .-. -. -.-- .---  .--. .- - - " \
              ". .-. -. --..--  -.- --- - --- .-. -.-- .---  .--. --- --.. .-- --- .-.. .-.- . -  .--. --- " \
              "-.. .-. ..- ...- .. - -..-  -. . ... --- .-- -- . ... - .. -- -.-- .  --- -... --.-- . -.- - " \
              "-.-- .-.-.- "
    morse_text = Morse()
    ru_text = Russian()

    '''
    Выполнение кода без использования адаптера
    '''
    morse_text.message = message
    ru_text.message = morse_text.message
    print("Вывод текста без адаптера: ", ru_text.message)

    '''
        Выполнение кода с использованием адаптера
    '''
    morse_text.message = message
    adapted_text = MorseToRussianAdapter(morse_text)
    ru_text.message = adapted_text.message
    print("Вывод текста с адаптером: ", ru_text.message)
