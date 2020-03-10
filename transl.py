from translate import Translator
from io import open

translator = Translator(to_lang='ja')

try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)

except FileNotFoundError as e:
    print('File do not exist')
