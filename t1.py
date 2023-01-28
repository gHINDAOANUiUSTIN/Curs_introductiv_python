# Exercitii obligatorii

# Ex 1;
"""
Variabila este un recipient (o zona din memorie)
pe care il putem umple cu orice din categoria recipientului
De exemplu: daca recipientul este o sticla, atunci putem pune
in principal lichide (daca este un string, inregistram
in memorie siruri de caractere). Putem pune si obiecte
solide - pietre - insa nu vom avea acces la ele
precum am avea intr-un alt fel de recipient
(in string putem inregistra si numere (integer, float),
insa nu va fi posibil sa facem operatii specifice cu ele)
"""

# Ex 2;
angajat = "Zamfir Petru"
an_nastere = 1970
salariu_net = 3520.54
peste_1an = True

# Ex 3;
print(f'Tipul variabilei angajat este: {type(angajat)} \n'
      f'Tipul variabilei an_nastere este: {type(an_nastere)} \n'
      f'Tipul variabilei salariu_net este: {type(salariu_net)} \n'
      f'Tipul variabilei peste_1an este: {type(peste_1an)}')

# Ex 4;
salariu_net = round(salariu_net)
print(f'\nValoarea rotunjita a salariului net este: {salariu_net}\n'
      f'Tipul variabilei salariu_net a devenit: {type(salariu_net)}')

# Ex 5;
print(f'\n{angajat} este un angajat al companiei noastre de mai mult de un an ({peste_1an}). \n'
      f'Acesta a fost nascut in anul {an_nastere} si are salariul net de {salariu_net}. \n')

# sau

print(angajat + " este un angajat al companiei noastre de mai mult de un an ("
      + str(peste_1an) + ").\nAcesta a fost nascut in anul "
      + str(an_nastere) + " si are salariul net de " + str(salariu_net) + ".")

# Ex 6;
nume = input("Te rog introdu numele tau: ")
prenume = input("Te rog introdu prenumele tau: ")
print(f'Numele complet are {len(nume)+len(prenume)} caractere')

# Ex 7;
lungimea = int(input("Introduceti lungimea dreptunghiului: "))
latimea = int(input("Introduceti latimea dreptunghiului: "))
print(f'Aria dreptunghilui este {lungimea*latimea}')


# Ex 8-9;
sir = 'Coral is either the stupidest animal or the smartest rock'
print(f'\n{sir} \nSirul de mai sus contine cuvantul "the" de {sir.count(" the ")} ori\n')


# Ex 10;
assert sir.isnumeric() == True, "Acest sir de caractere nu contine doar numere"
print("Sirul contine doar numere")


# Exercitii Optionale:

# Ex 1;
sir_impar = input("Introduceti un cuvant format dintr-un numar impar de litere: ")
poz_centru = round(len(sir_impar)/2-1)
print(f'Litera din mijloc a cuvantului introdus este {sir_impar[poz_centru]}')


# Ex 2;
sir1 = input('Introduceti un sir de caractere: ')
assert sir1 == sir1[::-1],'Acesta nu este un palindrom'
print('Acesta este un palindrom')

