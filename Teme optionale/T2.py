import random

#E1: Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
print('E1: Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)')
x = int(input("E1: Introduceti un numar pentru verificare: "))
if x > 999:
    print(f'E1: Numarul introdus ({x}) este format din cel putin 4 cifre.')
else:
    print('E1: Numarul introdus (' + str(x) + ') este format din mai putin de 4 cifre.')

#E2: Verifica daca x are exact 6 cifre
print('E2: Verifica daca x are exact 6 cifre)')
x = int(input('E2: Introduceti un numar pentru verificare: '))
if x > 99999 and x < 1000000:
    print(f'E2: Numarul inrodus ({x}) este format din 6 cifre.')
elif x >= 1000000:
    print(f'E2: Numarul introdus ({x}) este format din mai mult de 6 cifre.')
else:
    print(f'E2: Numarul introdus ({x}) este format din mai putin de 6 cifre.')


#E3: Verifica daca x este numar par sau impar
print('E3: Verifica daca x este numar par sau impar')
x = int(input('E3: Introduceti un numar pentru verificare: '))
if x %2 == 0:
    print (f'E3: Numarul introdus ({x}) este par')
else:
    print(f'E3: Numarul introdus ({x}) este impar')

#E4: Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele.
print('E4: Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele.')
x = int(input('E4: Introduceti primul numar pentru verificare: '))
y = int(input('E4: Introduceti al doilea numar pentru verificare: '))
z = int(input('E4: Introduceti al treila numar pentru verificare: '))
if x > y and x > z:
    print(f'E4: Primul numar introdus ({x}) este cel mai mare.')
elif y > x and y > z:
    print(f'E4: Al doilea numar introdus ({y}) este cel mai mare.')
else:
    print(f'E4: Al treilea numar introdus ({z}) este cel mai mare.')

#E5: Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi)
print('E5: Presupunand ca a, b, c reprezinta unghiurile unui triunghi si x, y, z, dimensiunile laturilor acestuia, '
      'verifica si afiseaza daca triunghiul este valid sau nu: \n'
      '-un triunghi este valid daca: \n- suma tuturor unghiurilor este de 180; \n'
      '- suma lungimilor a oricaror doua laturi este mai mare decat lungimea celei de-a treia laturi')
a = int(input('E5: Introduceti dimensiunea primului unghi al triunghiului: '))
b = int(input('E5: Introduceti dimensiunea celui de-al doilea unghi al triunghiului: '))
c = int(input('E5: Introduceti dimensiunea celui de-al treila unghi al triunghiului: '))
x = int(input('E5: Introduceti dimensiunea primei laturi a triunghiului: '))
y = int(input('E5: Introduceti dimensiunea celei de-a doua laturi a triunghiului: '))
z = int(input('E5: Introduceti dimensiunea celei de-a treia laturi a triunghiului: '))
if a+b+c == 180:
    if x < y + z:
        print(f'E5: Triunghiul este valid deoarece:\n- suma unghiurilor x = {a} grade, y = {b} grade si z = {c} grade, este 180 de grade;\n'
              f'- suma laturilor y = {y} si z = {z} este mai mare decat latura x = {x}. ')
    elif y < x + z:
        print(f'E5: Triunghiul este valid deoarece:\n- suma unghiurilor x = {a} grade, y = {b} grade si z = {c} grade, este 180 de grade;\n'
              f'- suma laturilor x = {x} si z = {z} este mai mare decat latura y = {y}. ')
    elif z < x + y:
        print(f'E5: Triunghiul este valid deoarece:\n- suma unghiurilor x = {a} grade, y = {b} grade si z = {c} grade, este 180 de grade;\n'
              f'-suma laturilor x = {x} si y = {y} este mai mare decat latura z = {z}. ')
    else:
        print(f'E5: Triunghiul nu este valid deoarece:\n'
              f'-suma lungimilor a oricaror doua laturi nu este mai mare decat lungimea celei de-a treia. ')
else:
    print(f'E5: Triunghiul nu este valid deoarece:\n'
          f'-suma unghiurilor  x = {a} grade, y = {b} grade si z = {c} grade, nu este 180 de grade. ')

#E6: Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
#la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
#ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'
print (f"E6: Avand stringul: 'Coral is either the stupidest animal or the smartest rock';\n"
       f"Citește de la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere.\n"
       f"Ex: Dacă ați ales x = 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'")
string6 = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('E6: Introduceti un numar pentru verificare: '))
if x > len(string6) or x < 0:
    print(f'E6: Numarul introdus ({x}) depaseste numarul de caractere al stringului sau nu este valid.')
elif x == 0:
    print(f'E6: String-ul dat devine: "{string6}"')
else:
    print(f'E6: String-ul dat devine: "{string6[0: -x:]}"')

#E7: Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere + ultimele 5
print('E7: Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere + ultimele 5:')
string7 = string6[0: 5:] + string6[-5::]
print(f'E7: String-ul format este "{string7}"')

#E8: Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
#indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
#(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
#afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest animal or the smartest '
print('E8: Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start al cuvântului rock\n'
      '- adică poziția in string la care începe cuvântul rock (hint: este o funcție care te ajuta sa faci asta).\n'
      'Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant.\n'
      ' Output asteptat: "Coral is either the stupidest animal or the smartest "')
pozitie = string6.find("rock")
print(f'E8: Pozitia in string la care incepe cuvantul rock este: {pozitie}')
print((f'E8: Stringul citit pana la indexul aflat este: {string6[0:pozitie:]}'))

#E9: Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
#Se va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
#e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
#functie pentru a face string-ul case insensitive)
print(f"E9:Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se va folosi un assert.\n"
      f"Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul si ultimul caracter este la fel.\n"
      f"Hint: te poti folosi de o functie pentru a face string-ul case insensitive) ")
string9 = input('E9: Introduceti un string pentru verificare: ')
assert string9[0].casefold() != string9[-1].casefold(), 'Primul caracte din sir este la fel cu ultimul (insensitive case).'

# E10: Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare:
# Hint: foloseste slicing si controleaza afisarea in slicing cu slicing step.
print(f'E10: Avand stringul "0123456789" afiseaza doar numerele pare si apoi doar numerele impare:\n'
      f'Hint: foloseste slicing si controleaza afisarea in slicing cu slicing step.')
string10 = '0123456789'
string10_pare= ''
string10_impare= ''
for i in range(0, len(string10)):
    if int(string10[i]) % 2 == 0:
        string10_pare += ' ' + string10[i]
    else:
        string10_impare += ' ' + string10[i]
print(f'E10: Numerele pare din string sunt: {string10_pare}')
print(f'E10: Numerele impare din string sunt: {string10_impare}')

#B1: Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept inputuri urmatoarele informatii:
#a. Varsta
#b. Insotit de mama
#c. Insotit de tata
#d. Pasaport
#e. Act permisiune mama
#f. Act permisiune tata
#Conditii de imbarcare:
#1. Daca pers are varsta peste 18 ani si are pasaport
#2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
#3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
print('B1: Formular permisiune imbarcare: ')
varta = int(input('B1: Varsta?: '))
print('B1: Va rugam sa raspundeti cu "da" sau "nu" la urmatoarele intrebari: ')
pasaport = input('B1: Aveti pasaport?: ').casefold()
if varta >=18:
    if pasaport.find('da') != -1:
        print(f'Multumim frumos. Va rugam sa va imbarcati.')
    else:
        print(f'Nu aveti dreptul de a calatori deoarece nu aveti pasaport.')
else:
    if pasaport.find('da') != -1:
        insotit_mama = input('B1: Sunteti insotit/a de mama?: ').casefold()
        insotit_tata = input('B1: Sunteti insotit/a de tata?: ').casefold()
        if insotit_mama.find('da') != -1 and insotit_tata.find('da') != -1:
            print(f'Multumim frumos. Va rugam sa va imbarcati.')
        elif insotit_mama.find('da') != -1:
            act_permisiune_tata = input('B1: Aveti permisiunea tatalui?: ').casefold()
            if act_permisiune_tata.find('da') != -1:
                print(f'Multumim frumos. Va rugam sa va imbarcati.')
            else:
                print('Pentru a putea calatori este necesar sa aveti un act de permisiune din partea parintelui care nu va insoteste.')
        elif insotit_tata.find('da') != -1:
            act_permisiune_mama = input('B1: Aveti permisiunea mamei?: ').casefold()
            if act_permisiune_mama.find('da') != -1:
                print(f'Multumim frumos. Va rugam sa va imbarcati.')
            else:
                print('Pentru a putea calatori este necesar sa aveti un act de permisiune din partea parintelui care nu va insoteste.')
        elif insotit_tata.find('da') == -1 and insotit_mama.find('da') == -1:
            print("Nu aveti dreptul de a calatori deoarece nu sunteti insotit/a de niciun parinte.")
        else:
            print(f'Multumim frumos. Va rugam sa va imbarcati.')
    else:
        print(f'Nu aveti dreptul de a calatori deoarece nu aveti pasaport.')

#B2: Joc de noroc:
#- Cauta pe net si vezi cum se genereaza un numar random
#- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
#Numarul salvat va fi generat random cu metoda gasita in online
#- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
#- Verifica si afiseaza daca utilizatorul a ghicit numarul
#- Vor exista 3 optiuni care vor trebui tratate:
#● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
#● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
#● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
print('B2: Joc de noroc: ')
x = random.randint (1,6)
y = int(input('Incercati sa ghiciti ce zar va pica: '))
if y < x:
    print (f'Din pacate ai pierdut. Ai ales un numar mai mic ({y}). Zarul a picat {x}')
if y > x:
    print(f'Din pacate ai pierdut. Ai ales un numar mai mare ({y}). Zarul a picat {x}')
if y == x:
    print(f'Felicitari. Ai catigat. Zarul a picat numarul ales de tine ({y}).')