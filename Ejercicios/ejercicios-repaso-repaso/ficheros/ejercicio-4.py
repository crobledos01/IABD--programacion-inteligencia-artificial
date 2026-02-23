from urllib import request
from urllib.error import URLError

def contar_palabras_por_url(url):
    try:
        with request.urlopen(url) as f:
            bytes_texto = f.read()
    except URLError:
        print(f"La url {url} no existe o no es accesible")
        return

    texto = bytes_texto.decode("utf-8")
    palabras = texto.rstrip()
    print(f"El fichero tiene {len(palabras)} palabras.")

contar_palabras_por_url("https://www.gutenberg.org/")