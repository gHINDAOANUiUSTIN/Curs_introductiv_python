import random
#1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
#Itereaza prin listă alte_numere
for numar in alte_numere:
    # Populează corect celelalte liste
    if numar < 0:
        numere_negative.append(numar)
    else:
        numere_pozitive.append(numar)
    if numar %2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
#Afișeaza cele 4 liste la final
print(f'E1: Lista numere negative: {numere_negative},\n'
      f'E1: Lista numere pozitive: {numere_pozitive},\n'
      f'E1: Lista numere pare: {numere_pare},\n'
      f'E1: Lista numere impare: {numere_impare}.')

#2. Aceeași listă:
#Ordonează crescător lista fară să folosești sort.
k=0
k = 0
for i in range(len(alte_numere)):
    for j in range(len(alte_numere)-1):
        if alte_numere[j] > alte_numere[j+1]:
            k = alte_numere[j]
            alte_numere[j] = alte_numere[j+1]
            alte_numere[j+1] = k
print(f'E2: {alte_numere}')


#3. Ghicitoare de număr:
#numar_secret = Generați un număr random între 1 și 30
numar_secret = random.randint (1,30)
#Numar_ghicit = None
numar_ghicit = None
#Folosind un while
while numar_ghicit != numar_secret:
    # User alege un număr
    numar_ghicit = int(input("E3: Ghiceste un numar intre 1 si 30: "))
    if numar_ghicit < numar_secret:
        # ● Nr secret e mai mare
        print("E3: Numarul secret este mai mare")
    elif numar_ghicit > numar_secret:
        # ● Nr secret e mai mic
        print("E3: Numarul secret este mai mic")
    else:
        # ● Felicitări! Ai ghicit!
        print("E3: Felicitari! Ai ghicit!")



#4. Alege un număr de la tastatură
numar = int(input("E4: Introduceti un numar: "))
#Scrie un program care să genereze în consolă următoarea piramidă
#Ex: 7
#1
#22
#333
#4444
#55555
#666666
#7777777
#Ex:3
#1
#22
#333
for i in range(1, numar+1):
    for j in range(i):
        print(i, end="")
    print('')

#5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
#Iterează prin listă 2d
print('E5: ')
for lista_nr in tastatura_telefon:
    for cifra in lista_nr:
        #Printează ‘Cifra curentă este x’
        print("Cifra curentă este", cifra)

