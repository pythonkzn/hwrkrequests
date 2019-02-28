import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path_in, path_out, lang_in, to_lang = 'ru'):
    text = ''
    out_data = ''

    with open(path_in, 'r') as f:
       for line in f:
           text += line

    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang_in +'-' + to_lang
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    out_data = json_['text'][0]


    with open(path_out, 'w') as output:
        output.write(out_data)

def main():
    translate_it('ES.txt', 'out.txt', 'es')


main()
