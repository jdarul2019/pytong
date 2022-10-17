plik = open("plansza.txt")
plansza = []

for linia in plik:
    plansza.append(linia.strip('\n'))
print(plansza)
kolumnaIlosc = 0
liczZnakow = 0
liczKolumn = 0
czarne = 0
biale = 0
for i in range(8):
    for j in range(8):
        if plansza[j][i].isupper():
            czarne += 1
        if plansza[j][i].islower():
            biale += 1
        if plansza[j][i] != '.':
            liczZnakow+= 1
    if liczZnakow > 1:
        kolumnaIlosc += 1
    if czarne!=0 and biale!=0:
        if czarne == biale:
            liczKolumn+=1
    liczZnakow = 0
    czarne = 0
    biale = 0
print(kolumnaIlosc, liczKolumn)
