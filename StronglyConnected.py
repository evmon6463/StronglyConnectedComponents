from collections import defaultdict
from random import randrange
import matplotlib.pyplot as plt
import networkx as nx
import sys
import time


class Grafas:
    def __init__(self, virsunes):
        self.virsunes = virsunes
        self.grafas = defaultdict(list)

    def pridetiBriauna(self, u, v):
        self.grafas[u].append(v)

    def uzpildyti(self, v, aplankytas, stack):
        aplankytas[v] = True
        for i in self.grafas[v]:
            if aplankytas[i] == False:
                self.uzpildyti(i, aplankytas, stack)
        stack = stack.append(v)

    def atvirkstinis(self):
        g = Grafas(self.virsunes)
        for i in self.grafas:
            for j in self.grafas[i]:
                g.pridetiBriauna(j, i)
        return g

    def DFS(self, aplankyti, gr, stack):
        for i in range(self.virsunes):
            aplankyti = [False] * (self.virsunes)
        while stack:
            i = stack.pop()
            if aplankyti[i] == False:
                gr.aplankytiDFS(i, aplankyti)
                print(" ")

    def aplankytiDFS(self, v, aplankytas):
        aplankytas[v] = True
        print(v, end=" ")
        for i in self.grafas[v]:
            if aplankytas[i] == False:
                self.aplankytiDFS(i, aplankytas)

    def spausdinti(self):
        stack = []
        for i in range(self.virsunes):
            aplankyti = [False] * (self.virsunes)
        for i in range(self.virsunes):
            if aplankyti[i] == False:
                self.uzpildyti(i, aplankyti, stack)
        gr = self.atvirkstinis()
        g.DFS(aplankyti, gr, stack)


print(
    "Iveskite G, jeigu norite kad programa sugeneruotu grafa, I, jeigu patys norite įvesti grafo duomenis, N nuskaityti nuo tekstinio failo ")
argumentas = input()
if argumentas == "G":
    try:
        print('Iveskite kiek viršūnių turės orientuotas grafas. Iveskite skaičių nuo 2 iki 5: ')
        x = input()
        if (int(x) > 5):
            sys.exit(0)
        else:
            y = int(int(int(x) * 3) / 5)
            sarašo_dydziai = []
            laikas = []
            j = 1
            for j in range(6):
                G = nx.DiGraph()
                i = 1
                sarasas = []
                for i in range(int(x)):
                    sarasas.append((randrange(int(y)), randrange(int(y))))

                G.add_edges_from(sarasas)

                g = Grafas(int(y))
                for i, j in sarasas:
                    g.pridetiBriauna(i, j)
                print("")
                pradzia = time.process_time()
                g.spausdinti()
                pabaiga = time.process_time()

                print(
                    "Algoritmas " + str(len(sarasas)) + " dydzio liste atranda stipriai jungias kompenentes per " + str(
                        pabaiga - pradzia) + "s")
                x = int(x) * 5
                sys.setrecursionlimit(int(x) + 1)
                y = int(y) * 5
                sarašo_dydziai.append(x + y)
                laikas.append(pabaiga - pradzia)

            plt.xlabel('Sąrašo dydis')
            plt.ylabel('Laikas')
            plt.plot(sarašo_dydziai, laikas)
            plt.grid()
            plt.show()
    except:
        print("Klaidingai įvestas viršūnių skaičius")

elif argumentas == "I":
    try:
        print("Kiek briaunų turės grafas ")
        kiek = int(input())
        g = Grafas(kiek)
        for i in range(g.virsunes):
            print("Iveskite viršūnes: ")
            n, m = map(int, input().strip().split(" "))
            g.pridetiBriauna(n, m)
        print(" ")
        g.spausdinti()
    except:
        print("Klaidingai ivesta viršūnė skaičiai turi būti intervale nuo 0 iki " + str(kiek - 1))
elif argumentas == "N":
    try:
        f = open("grafas.txt")
        lines = f.readlines()
        count = len(lines)
        g = Grafas(count)
        for l in lines:
            x, y = [int(x) for x in l.split()]
            g.pridetiBriauna(x, y)
        g.spausdinti()
    except:
        print("Klaida")
else:
    print("Klaidingai įvestas atsakymas")
