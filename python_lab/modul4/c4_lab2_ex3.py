''' “In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa
aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta in
sine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si
acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea.”

Se cere:
a. Numărarea literei introduse de către utilizator în textul de mai sus, indiferent daca
aceasta este o majuscula sau nu.
b. Crearea unei liste cu toate cuvintele din textul de mai sus cu ajutorul funcțiilor
split().
Documentatie: https://docs.python.org/3/library/stdtypes.html#str.split
c. Selectarea cuvintelor care incep cu litera s din lista creata anterior si afisarea
acestora. '''

text = '''In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa
aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta in
sine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si
acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea.'''


def num_litera(my_text):
    if (type(my_text) == str):
        nr_litere = 0
        for caracter in my_text:
            if caracter.isalpha() == True:
                nr_litere += 1
    print(f'numar litera = {nr_litere}')

num_litera(text)


def prel_cuvinte(my_text):
    cuvinte = my_text.split()
    print(cuvinte)
    for cuvant in cuvinte:
        prima_litera = cuvant[0]
        #print(prima_litera)
        if prima_litera == 's':
            print(cuvant)


prel_cuvinte(text)
