import os
import numpy as np

def heurystyka(meta, y, coords):
    odleglosc = np.sqrt(np.sum((coords[meta] - coords[y])**2))
    return odleglosc

def A_gwiazdka(start, meta, graf, coords):
    przejrzane = set()
    rozpatrywane = {start}
    przyszedl_z = {}

    #Wypelninie g i f wartosciami inf
    n_wierzcholkow = graf.shape[0]
    g = {}
    for i in range(n_wierzcholkow):
        g[i] = float('inf')
    g[start] = 0.0

    f = {}
    for i in range(n_wierzcholkow):
        f[i] = float('inf')
    f[start] = heurystyka(meta, start, coords)

    while rozpatrywane:
        x = min(rozpatrywane, key=f.get)
        if x == meta:
            trasa = zrekonstruuj_trase(przyszedl_z, x)
            return trasa

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

    return None

def zrekonstruuj_trase(przyszedl_z, x):
    trasa = [x]
    while x in przyszedl_z:
        x = przyszedl_z[x]
        trasa.insert(0, x)
    return trasa

# Wczytanie pliku
plik = input().strip()
with open(plik) as f:
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

najlepsza_trasa = A_gwiazdka(start, meta, graf, coords)

if najlepsza_trasa is None:
    print("Brak")
else:
    najlepsza_trasa_1 = []
    for i in najlepsza_trasa:
        najlepsza_trasa_1.append(i+1)
    print(*najlepsza_trasa_1)
