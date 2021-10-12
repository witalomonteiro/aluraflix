from filme import Filme
from playlist import Playlist
from serie import Serie

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

programas = [vingadores, atlanta]
minha_lista = Playlist("Minha Playlist", programas)

for programa in minha_lista:
    print(programa)

print(len(minha_lista))