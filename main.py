# importando os módulos necessários
import urllib.request
import urllib.parse
import urllib.error
import json


def get_lyric(mus, art):
    # parse.quote to enconde a string into URL format
    mus = urllib.parse.quote(mus)
    art = urllib.parse.quote(art)

    # search other method to autenticate
    # Personal Key generate by myvagalume.com.br
    key = '5bf325dd4cf0161ca30f8444ce58c48c'

    # API url
    url = f'https://api.vagalume.com.br/search.php?art={art}&mus={mus}&apikey={key}'
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    # Print("Conexão com API estabelecida!")
    js = json.loads(data)

    while True:

        if js['type'] == 'song_notfound':
            print('Música não encontrada!')
            break
        elif js['type'] == 'notfound':
            print('Artista não encontrado!')
            break
        else:
            song = js['mus'][0]['name']
            artist = js['art']['name']
            lyric = js['mus'][0]['text']

        print('\nMúsica: ', song, '\nArtista: ', artist, '\nLetra: \n', lyric)

    # return js


query_mus = input("Digite o nome da música: ")
query_art = input("Digite o artista: ")


if __name__ == "__main__":
    get_lyric(query_mus, query_art)
