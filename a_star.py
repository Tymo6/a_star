import os
import numpy as np

def heurystyka(meta, y, coords):
    odleglosc = np.sqrt(np.sum((coords[meta] - coords[y])**2))
    return odleglosc

def A_gwiazdka(start, meta, graf):
    przejrzane = set()
    rozpatrywane = {start}
    przyszedl_z = {}
    n_wierzcholkow = graf.shape[0]

    g = {i: float("inf") for i in range(n_wierzcholkow)}
    g[start] = 0.0
    f = {i: float("inf") for i in range(n_wierzcholkow)}
    f[start] = heurystyka(meta, start, coords)

    while rozpatrywane:
        x = min(rozpatrywane, key=f.get)
        if x == meta:
            trasa = zrekonstruuj_trase(przyszedl_z, x)
            return trasa, g[x]

        rozpatrywane.remove(x)
        przejrzane.add(x)

        sasiedzi_x = np.where(graf[x] != 0)[0]
        for y in sasiedzi_x:
            tymczasowe_g = g[x] + graf[x, y]
            if tymczasowe_g < g[y]:
                przyszedl_z[y] = x
                g[y] = tymczasowe_g
                f[y] = g[y] + heurystyka(meta, y, coords)
                if y not in rozpatrywane:
                    rozpatrywane.add(int(y))

    return None, None

def zrekonstruuj_trase(przyszedl_z, x):
    trasa = [x]
    while x in przyszedl_z:
        x = przyszedl_z[x]
        trasa.insert(0, x)
    return trasa

# Wczytanie pliku
plik = input().strip()
with open(plik) as f:
    print("Ok1")
    # Wczytanie współrzędnych
    coords_raw = f.readline().strip()
    coords_raw2 = coords_raw.replace("(", "").replace(")", "").replace(",", " ")
    coords = np.fromstring(coords_raw2, sep=" ").reshape(-1, 2)
    # Wczytanie start i mety
    druga_linia = f.readline().strip()
    start, meta = map(int, druga_linia.split())
    start -= 1
    meta  -= 1
    # Wczytanie macierzy sąsiedztwa (czytamy z uchwytu 'f', bo 2 linie już pobrane)
    graf = np.loadtxt(f)

print("Ok2")
najlepsza_trasa, koszt = A_gwiazdka(start, meta, graf)
print("Ok3")
nazwa = os.path.basename(plik)
print("Ok4")

if najlepsza_trasa is None:
    print("Brak")
else:
    print(najlepsza_trasa)
