"""
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
"""
#E1:
sir = input('E1: Introduceti un sir de litere de dimensiune impara: ')
if len(sir) % 2 == 0:
    print('E1: Sirul introdus este de dimensiune para.')
else:
    caracter_mijloc = sir[int(len(sir)/2)]
    print(f'E1: Caracterul din mijloc al sirului introdus este: {caracter_mijloc}')

"""
2. Folosind assert, verifică dacă un string este palindrom.
"""
#E2:
assert sir != sir[::-1], 'E2: Sirul este palindrom'
print('E2: Daca sirul de mai sus era palindrom, se primea un mesaj de eroare')
"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""
#E3:
for cuvant in list(input('E3: Introduceti o lista de cuvinte separate prin spatiu: ').split()):
    print(cuvant)

"""
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""

#E4:
string1 = input('E4: Introduceti un sir de cuvinte: ')
prima_litera = string1[0]
if prima_litera.isupper():
    prima_litera = prima_litera.lower()
string2 = '' + prima_litera
for litera in string1[0:-1]:
    if litera == prima_litera:
        string2 += litera.upper()
    else:
        string2 += litera
ultima_litera = string1[-1]
if ultima_litera.isupper():
    ultima_litera = ultima_litera.lower()
string2 += ultima_litera
print(f"E4: Conform cerintelor, sirul devine: {string2}")

"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""

user = input('E5: Intoruceti username-ul: ')
parola = input('E5: Introduceti parola: ')
parola_ascunsa = ''
for i in range (0, len(str(parola))):
    parola_ascunsa += '*'
print(f'E5: Parola introdusa pt user-ul {user} este {parola_ascunsa} si are {len(parola)} caractere')








