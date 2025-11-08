import os
import numpy as np
import ast

def heurystyka(meta, y, coords):
        odleglosc = np.sqrt(np.sum((coords[meta]-coords[y])**2))
        return odleglosc

def A_gwiazdka(start, meta, graf):
    przejrzane = set()
    rozpatrywane = {start}
    przyszedl_z = {}
    n_wierzcholkow = graf.shape[0] 
    g = {}
    for i in range(n_wierzcholkow):
        g[i] = float("inf")
    g[start] = 0
    f = {}
    for i in range(n_wierzcholkow):
        f[i] = float("inf")
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
            tymczasowe_g = g[x] + graf[x,y]
            if tymczasowe_g < g[y]:
                przyszedl_z[y] = x
                g[y] = tymczasowe_g
                f[y] = g[y] + heurystyka(meta, y, coords) 
                if y not in rozpatrywane:
                    rozpatrywane.add(y)
    return None

def zrekonstruuj_trase(przyszedl_z, x):
    trasa = [x]
    while trasa[-1] in przyszedl_z:
        obecny_wierzcholek = przyszedl_z[trasa[-1]]
        trasa.insert(0, obecny_wierzcholek)
    return trasa

#Wczytanie pliku
plik = input().strip()
with open(plik) as f:
    print("Ok1")
    #Wczytanie wspolrzednych
    coords_raw = f.readline().strip()
    #coords = np.array(ast.literal_eval("["+coords_raw.replace(") ","),")+"]"), dtype=float)
    coords =coords_raw.replace(") ","),")
    #Wczytanie start i mety
    druga_linia = f.readline().strip()
    start, meta = map(int, druga_linia.split())
    start -= 1
    meta  -= 1
    #Wczystanie macierzy sasiedztwa
    graf = np.loadtxt(plik, skiprows=2)
print("Ok2")
najlepsza_trasa, koszt = A_gwiazdka(start, meta, graf)
print("Ok3")
nazwa = os.path.basename(plik)
print("Ok4")
if najlepsza_trasa is None:
    print("Brak")
else:
    print(najlepsza_trasa) 
#    C:\Users\Surface\Desktop\2025_10_15_NMISI_Projekt_1_A_z_gwiazdka\Dane\1.txt