# Ex1: Având lista:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# Folosește un for că să iterezi prin toată lista și să afișezi;

# ● ‘Mașina mea preferată este x’.
for masina in range(0, len(masini)):
    print(f"Masina mea preferata este: {masini[masina]}")
print("Am ajuns la finalul listei")

# ● Fă același lucru cu un for each.
for masina in masini:
    print(f"Masina mea preferata este: {masina}")
print("Am ajuns la finalul listei")
i = 0

# ● Fă același lucru cu un while.
while i < len(masini):
    print(f"Masina mea preferata este: {masini[i]}")
    i += 1
print ("Am ajuns la finalul listei")

# Ex2: Aceeași listă: Folosește un for else:
# În for, modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul;
for x in range(1, len(masini)-1):
    masini[x] = masini[x].upper()
# În else, printează lista.
else:
    print(masini)


# Ex3: Aceeași listă:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Vine un cumpărător care dorește să cumpere un Mercedes.
i = 0
for i in range(0, len(masini)):  # Itereaza prin ea prin modalitatea aleasă de tine.
    if masini[i] == 'Mercedes':  # Dacă mașina e mercedes:
        print("Am gasit masina dorita de dumneavoastra")  # Printează ‘am găsit mașina dorită de dvs’
        break                    # Ieși din ciclu folosind un cuvânt cheie care face acest lucru
    else:# Altfel:
        print(f"Am gasit masina {masini[i]}. Mai cautam")   # Printează ‘Am găsit mașina X. Mai căutam‘


# Ex4: Aceași listă;
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Vine un cumpărător bogat dar indecis.
i=0
for i in range(0, len(masini)):
    # Îi vom prezenta toate mașinile inafara de Trabant și Lăstun
    if masini[i] != "Trabant" and masini[i] != "Lastun":
        print(f"S-ar putea sa va placa masina: {masini[i]}")
        # Printează: s-ar putea să vă placă mașina x.
        continue  # - Dacă mașina e Trabant sau Lăstun: da skip la ce urmează (nu trebuie else)
print("Acestea sunt toate masinile noastre. Pe care o doriti?")


# Ex5: Modernizează parcul de mașini:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# ● Crează o listă goală, masini_vechi.
masini_vechi = []
# ● Itereaza prin mașini.
for n in range(0, len(masini)):
    # ● Când găsesti Lăstun sau Trabant:
    # - Salvează aceste mașini în masini_vechi.
    # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
    if masini[n] == 'Trabant':
        masini_vechi.append(masini[n])
        masini[n] = 'Tesla'
    elif masini[n] == 'Lastun':
        masini_vechi.append(masini[n])
        masini[n] = 'Tesla'

# ● Printează Modele vechi: x.
print(masini_vechi)
# ● Modele noi: x.
print(masini)


# Ex6: Având dict:
pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
print(pret_masini)
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
masini_acces = []
for i in range (0, len(pret_masini.items())):
    pret = list(pret_masini.values())
    marca = list(pret_masini.keys())
    if pret[i] > 15000:
        continue
    else:
        masini_acces.append(marca[i])
print(f'Masinile pe care le puteti achizitiona in bugetul de 15000 euro sunt urmatoarele: {masini_acces}')


# Ex7: Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
k = 0
for i in range (0, len(numere)):
    if numere[i] == 3:
        k += 1

print (f'Numarul 3 apare de {k} ori.')
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).


# Ex8: Aceeași listă:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
s = 0
for i in range (0, len(numere)):
    s += numere[i]
print(f'Suma numerelor din lista este {s}.')


# Ex9: Aceeași listă:
# ● Iterează prin ea.
m = numere[0]
for i in range (0, len(numere)):
    if numere[i] > m:
        m = numere[i]
print(f'Cel mai mare numar din lista este {m}.')
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

# Ex10: Aceeași listă:
# ● Iterează prin ea.
for i in range (0, len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
        # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
        # Ex: dacă e 3, să devină -3
print(numere)
# ● Afișază noua listă.